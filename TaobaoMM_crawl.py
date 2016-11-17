#coding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import os
class spider:
    def __init__(self):
        self.siteURL='http://mm.taobao.com/json/request_top_list.htm'
        self.imgs=[]
    def getPage(self,pageIndex):
        url=self.siteURL+'?page='+str(pageIndex)
        print url
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        pageCode=response.read().decode('gbk')
        soup=BeautifulSoup(pageCode,'html.parser')
        return soup
    def getContents(self,pageIndex):
        soup=self.getPage(pageIndex)
        for items in soup.find_all('div',class_='list-item'):
            mm_name=items.find('a',class_='lady-name').string
            mm_area=items.span.string
            mm_url=items.a['href']
            mm_img=items.img['src']
            print mm_url,mm_name,mm_area,mm_img
    def getImgs(self,pageIndex):
        soup=self.getPage(pageIndex)
        for imgs in soup.find_all('div',class_='list-item'):
            mm_img=imgs.img['src']
            print mm_img
            self.imgs.append(mm_img)
        return self.imgs
    def saveImgs(self,pageIndex):
        self.getImgs(pageIndex)
        i=0
        while True:
            if i<len(self.imgs):
                contens=urllib2.urlopen('http:'+self.imgs[i]).read()
                f=open(str(i)+'.jpg','w')
                f.write(contens)
                f.close()
                i+=1
            else:
                break
    def start(self,start_page,end_page):
        for i in range(start_page,end_page):
            self.saveImgs(i)
        
            
spider=spider()
spider.start(1,4)
    