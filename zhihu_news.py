# -*- coding:utf-8 -*-
import re
import urllib2
import urllib
from bs4 import BeautifulSoup
class news():
    def __init__(self):
        self.titles=[]
        self.hrefs=[]
        self.url='http://daily.zhihu.com/'
        self.headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"}
    def getPage(self):
        req=urllib2.Request(self.url,headers=self.headers)
        res=urllib2.urlopen(req)
        html=res.read()
        return html
    def getTitle(self):
        soup=BeautifulSoup(self.getPage(),'html.parser')
        a=soup.find_all('div',class_='box')
        for item in a:
            news_title=item.span.string
            self.titles.append(news_title)
        return self.titles
    def getHref(self):
        soup=BeautifulSoup(self.getPage(),'html.parser')
        a=soup.find_all('div',class_='box')
        for item in a:
            news_href=item.a['href']
            self.hrefs.append('http://daily.zhihu.com'+news_href)
        return self.hrefs
    def getNews(self,num):
        for i in range(num):
            print '%s:%s'%(self.titles[i],self.hrefs[i])

zh=news()
zh.getTitle()
zh.getHref()
zh.getNews(10)
