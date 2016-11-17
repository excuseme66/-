#coding=utf-8

#代码不够完善，验证码有时候有有时候没有的问题也没有处理好。如果报错，就多运行几次，因为一开始没有验证码，本代码只支持有验证码的情况。并且手动输入验证码
import re

import requests
from bs4 import BeautifulSoup

login_url='https://accounts.douban.com/login'
formData={
          'redir':'https://www.douban.com',
          'form_email':'qq27001280@126.com',
          'form_password':'worinima1996',
          'login':'登录',
          'captcha-id':None,
         'captcha-solution':None
          }
headers={
         "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0",
         }
r=requests.post(login_url, data=formData, headers=headers)
page=r.text
soup=BeautifulSoup(page,'html.parser')
captchaAddr = soup.find('img',id='captcha_image')['src']
reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
captcha_ID = re.findall(reCaptchaID,page)
captcha_url=raw_input('please input solution %s'%captchaAddr)
if captcha_ID:
    formData['captcha-id']=captcha_ID
    formData['captcha-solution']=captcha_url
r=requests.post(login_url, data=formData, headers=headers) 
index_page=r.text
if r.url=='https://www.douban.com':
    print '豆瓣模拟登录成功'
reck=r'<input type="hidden" name="ck" value="(.*?)"/'
ck=re.findall(reck,index_page)
formData['ck']=ck
signature=raw_input('请输入你的签名')
formData['signature']=signature
r=requests.post('https://www.douban.com/people/152988640/',data=formData,headers=headers)
if r:
    print formData['ck'],formData['signature']
    print '修改成功'

    

    