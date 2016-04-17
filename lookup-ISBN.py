import urllib2
import re

title="Pantaleon i wizytanki"

#https://www.google.pl/search?q=isbn+%22Aferzy%C5%9Bci+i+inne+opowiadania%22

qtitle=urllib.quote_plus(title)
url="https://www.google.pl/search?q=isbn+%22"+qtitle+"%22"
print url

# ISBN formats
# 8321603564
# 83-216-0356-4
# 

reISBN=re.compile("ISBN[^0-9]*([\d\-]{10,13})")

req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })

response = urllib2.urlopen(req)
html = response.read()

print re.findall(reISBN,html)
