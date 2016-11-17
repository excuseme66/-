# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
headers={
     'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
}
proxies = {
  "http": "http://114.215.101.42:3128",
  "https": "http://114.215.101.42:1080",
}
url='http://ip.chinaz.com/'
s=requests.session()

html=s.get(url,proxies=proxies,headers=headers)
soup=BeautifulSoup(html.content,'html.parser')
for item in soup.find_all('div',class_='IpMainWrap-Get mt10'):
    ip=item.find('p',class_='getlist pl10')
    print ip