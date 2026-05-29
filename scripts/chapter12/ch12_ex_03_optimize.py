"""
ch12_ex_03_optimize.py — Web link traversal (Chapter 12 assignment)

Task:
    Starting from a given URL, find the anchor tag at a specified position
    on the page, follow that link, and repeat the process a given number
    of times. Report the last name found.

Sample run:
    Start:    http://py4e-data.dr-chuck.net/known_by_Fikret.html
    Count:    4
    Position: 3
    Result:   Anayah   (sequence: Fikret → Montgomery → Mhairade → Butchi → Anayah)
"""

import urllib.request
from bs4 import BeautifulSoup
import ssl

# ---------------------------------------------------------------------------
# SSL context
# By default Python verifies HTTPS certificates. The training pages on
# py4e-data.dr-chuck.net use a self-signed certificate, so we disable
# hostname checking and certificate verification to allow the connection.
# ---------------------------------------------------------------------------
ctx = ssl.create_default_context()
ctx.check_hostname = False   # do not verify that the hostname matches the cert
ctx.verify_mode = ssl.CERT_NONE  # accept any certificate without validation


def get_links(url):
    """Fetch a web page and return all anchor links it contains.

    Prints "Retrieving: <url>" before making the HTTP request so the user
    can follow the traversal progress in the terminal.

    Args:
        url (str): The full URL of the page to fetch.

    Returns:
        list[tuple[str, str]]: A list of (href, link_text) pairs for every
        <a> tag on the page that has an href attribute. Tags without href
        are skipped. Link text is stripped of leading/trailing whitespace.
    """
    print(f'Retrieving: {url}')

    # Download the raw HTML bytes from the URL using our custom SSL context
    html = urllib.request.urlopen(url, context=ctx).read()

    # Parse the HTML with BeautifulSoup so we can search it with selectors
    soup = BeautifulSoup(html, 'html.parser')

    # Build a list of (href, visible_text) for each <a href="..."> tag.
    # tag.get('href') returns None for tags without href — those are filtered out.
    # tag.get_text(strip=True) is safer than tag.contents[0] because it works
    # even when the anchor contains nested HTML elements (e.g. <a><b>Name</b></a>).
    return [(tag.get('href'), tag.get_text(strip=True))
            for tag in soup('a') if tag.get('href')]


# ---------------------------------------------------------------------------
# User input
# If the user presses Enter without typing anything, the default test values
# from the assignment description are used instead.
# ---------------------------------------------------------------------------

# Starting URL — the first page to load
url = input('Enter URL: ').strip() or 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

# Number of times to follow a link (= number of pages loaded after the first)
count = int(input('Enter count: ').strip() or 4)

# 1-based position of the anchor tag to follow on each page
position = int(input('Enter position: ').strip() or 3)

# ---------------------------------------------------------------------------
# Traversal
# ---------------------------------------------------------------------------

# Fetch the starting page and get its list of links.
# This counts as the first "Retrieving" step.
links = get_links(url)

# Will hold the visible text (name) of the last link we followed.
# Initialised to None so the program fails clearly if count == 0.
name = None

for _ in range(count):
    # Pick the link at the requested 1-based position.
    # links[position - 1] returns (href, link_text) for that position.
    url, name = links[position - 1]

    # Follow the link: fetch the next page and update the links list
    # so the next iteration works on the new page.
    links = get_links(url)

# After all iterations, `name` holds the link text of the last page we
# navigated to — that is the answer to the assignment.
print(f'\nThe answer is "{name}"')
