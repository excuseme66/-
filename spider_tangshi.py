#-*-coding=utf-8-*-
import re
from bs4 import BeautifulSoup
import urllib2

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"}
def getPage(pageIndex):
    url='http://so.gushiwen.org/type.aspx?p='+str(pageIndex)
    req=urllib2.Request(url,headers=headers)
    res=urllib2.urlopen(req)
    html=res.read()
    return html
def savePoem(pageIndex):
    poem_title=[]
    poem_article=[]
    soup=BeautifulSoup(getPage(pageIndex),'html.parser')
    for item in soup.find_all('div',class_='sons'):
        title=item.p.string
        article=item.find('p',style='margin-bottom:0px;').get_text()
        poem_title.append(title)
        poem_article.append(article)
    for i in range(0,10):
        try:
            print '正在保存 %s Loading'%poem_title[i]
            print '保存成功'
            f=open(poem_title[i]+'.txt','wb')
            f.write(poem_article[i])
            f.close()
        except EOFError,e:
            print e
    print '第%s页古诗保存完毕'%pageIndex
def cPoem(startIndex,endIndex):
    for i in range(startIndex,endIndex):
        savePoem(i)





if __name__=='__main__':
    cPoem(1,5)