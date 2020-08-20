#!/usr/bin/env python
# coding: utf-8

# In[140]:

import tldextract
from urllib.parse import unquote, urlparse
import requests
from bs4 import BeautifulSoup
import sys
input_url = sys.argv[1]
processed_url = tldextract.extract(input_url)

TLD = processed_url.suffix
Domain = processed_url.domain+"."+processed_url.suffix
Hostname = urlparse(input_url).netloc
Path = urlparse(input_url).path

print("TLD: "+TLD)
print("DOMAIN: "+Domain)
print("HOSTNAME: "+Hostname)
print("PATH: "+Path)

#Find all the links in the page
page = requests.get(input_url)    
data = page.text
soup = BeautifulSoup(data, features="html.parser")
same_hostname = []
same_domain = []
different_domain = []
for link in soup.findAll('a'):
    url = link.get('href')
    if not url:
        continue
    if Hostname in url: 
        same_hostname.append(url)
    elif Domain in url:
        same_domain.append(url)
    else:
        different_domain.append(url)
print("Links: ")
print("\t"+"Same Hostname: ")
for i in same_hostname:
    print("\t\t"+i)
print("\t"+"Same Domain")
for i in same_domain:
    print("\t\t"+i)
print("\t"+"Different Domain: ")
for i in different_domain:
    print("\t\t"+i)


# In[ ]:




