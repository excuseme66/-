#coding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
#https://movie.douban.com/top250?start=50&filter=
class douban():
    def __init__(self):
        self.url='https://movie.douban.com/top250?start='
        self.headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"}
    def getPage(self,pageIndex):
        newurl=self.url+str(pageIndex)+'&filter='
        request=urllib2.Request(newurl,headers=self.headers)
        urlopen=urllib2.urlopen(request)
        response=urlopen.read().decode('utf-8')
        return response
    def getContents(self,pageIndex):
        contents=[]
        self.soup=BeautifulSoup(self.getPage(pageIndex),'html.parser')
        for items in self.soup.find_all('div',class_='item'):
            movie_name=items.span.contents[0]
            movie_Introduction=items.find('span',class_='other').contents[0]
            movie_grade=float(items.find('span',class_='rating_num').contents[0])
            print u'电影名称:%s\n电影介绍:%s\n电影评分:%s'%(movie_name,movie_Introduction,movie_grade)
    def getMoviename(self,pageIndex):
        contents=[]
        self.soup=BeautifulSoup(self.getPage(pageIndex),'html.parser')
        for items in self.soup.find_all('div',class_='item'):
            movie_name=items.span.contents[0]
            contents.append(movie_name)
        return contents                
    def savaTxt(self,pageIndex):
          file=open('douban.txt','w')
          file.write(self.getMoviename(pageIndex))
          file.close()
    

        
        
       
spider=douban()
spider.getContents(0)


     
            
        
        