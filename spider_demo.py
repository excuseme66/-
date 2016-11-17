#-*- coding=utf-8 -*-
import urllib2
from HTMLParser import HTMLParser
class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies=[]
    def handle_starttag(self, tag, attrs):
        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0]==attrname:
                    return attr[1]
            return None
        if tag =='li' and _attr(attrs,'data-title') and _attr(attrs,'data-category')=='nowplaying':
            movie={}
            movie['title']=_attr(attrs,'data-title')
            movie['score']=_attr(attrs,'data-score')
            movie['director']=_attr(attrs,'data-director')
            movie['actors']=_attr(attrs,'data-actors')
            self.movies.append(movie)
            print (('%(title)s|%(score)s|%(director)s|%(actors)s')%movie)





def nowplaying_movies(url):
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"}
    req=urllib2.Request(url,headers=headers)
    res=urllib2.urlopen(req)
    parser=MovieParser()
    parser.feed(res.read())
    res.close()
    return parser.movies
if __name__=='__main__':
    url='https://movie.douban.com/nowplaying/hangzhou/'
    movies=nowplaying_movies(url)
