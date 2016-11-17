#coding=utf-8
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
class QSBK:
    def __init__(self):
        self.pageIndex=1
        self.user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"
        self.headers={'User-Agent':self.user_agent}
        self.stories=[]
        self.enable=False
    def getPage(self,pageIndex):
        try:
            url='http://www.qiushibaike.com/8hr/page/'+str(pageIndex)
            request=urllib2.Request(url,headers=self.headers)
            response=urllib2.urlopen(request)
            pageCode=response.read().decode('utf-8')
            soup=BeautifulSoup(pageCode,'html.parser')
            return soup
        except urllib2.URLError,e:
            if hasattr(e, 'reason'):
                print u"连接糗事百科失败,错误原因",e.reason
                return None
    def getPageItems(self,pageIndex):
        pageCode=self.getPage(pageIndex)
        if not pageCode:
            print '页面加载失败'
            return None
        pagestores=[]
        for items in self.getPage(pageIndex).find_all('div',class_='article block untagged mb15'):
            pagestores.append(items.span.string)
            return pagestores
    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pagestores=self.getPageItems(self.pageIndex)
                if pagestores:
                    self.stories.append(pagestores)
                    self.pageIndex+=1
    def getOneStory(self,pagestores,page):
        for story in pagestores:
            input=raw_input()
            self.loadPage()
            if input=='Q':
                self.enable=='False'
                return
            print u'糗事:%s'%story
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
spider=QSBK()
spider.start()
             
        
        
        
        
        
        