from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
spn = soup('span')
numb = list()
for sp in spn:
    count += 1
    numb.append(sp.contents[0])

res = sum(int(x) for x in numb)

print(f'Count {count}')
print(f'Sum {res}')
