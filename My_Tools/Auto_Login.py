#-*- coding: utf-8 -*-
__author__ = "coolfire"

import urllib2
import urllib
import cookielib

headers = {
			'Connection':'keep-alive',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
		}
login_url = "http://slj.kuaixiaodi.net/admin/service.php"
pm_url = "http://slj.kuaixiaodi.net/admin/page.php?p=productManage"
username = "test"
password = "111111"
#创建cookie
cookie = cookielib.LWPCookieJar()
#创建cookie处理器
cookiehandler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookiehandler,urllib2.HTTPHandler)

post = {
	"m":"login",
	"p":"sys",
	"password":password,
	"username":username,
}

#登陆
post_data = urllib.urlencode(post)
request = urllib2.Request(login_url,post_data,headers)
response = opener.open(request)


#请求产品管理页面
response1 = opener.open(pm_url)
print response1.read()





