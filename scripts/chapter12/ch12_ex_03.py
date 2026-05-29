import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# count = None
# position = None

url = input('Enter url: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

count_input = input('Enter count: ')
count = int(count_input) if count_input else 4

position_input = input('Enter position: ')
position = int(position_input) if position_input else 3

ulst = list()
ulst.append(url)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

def namefinder():
    urlist = list()
    namelist = list()
    for tag in tags:
        urlist.append(tag.get('href', None))
        namelist.append(tag.contents[0])
    url = urlist[position - 1]
    name = namelist[position - 1]
    return url, name

ulst.append(namefinder()[0])

counts = count - 1
for tag in tags:
    if counts != 0:
        html = urllib.request.urlopen(namefinder()[0], context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        counts -= 1
        ulst.append(namefinder()[0])
    else:
        break

for i in ulst:
    print(i)
