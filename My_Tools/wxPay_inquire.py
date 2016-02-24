#-*- coding: utf-8 -*-
__author__ = "coolfire"

import urllib2
import urllib
import cookielib
import re
import webbrowser

#模拟登陆微信支付商户后台类:
class wxPay:
	#初始化方法
	def __init__(self):
		#首页url
		self.HomeURL = "https://pay.weixin.qq.com/index.php/home/login"
		#登陆url
		self.loginURL = "https://pay.weixin.qq.com/index.php/home/d_login"
		#资金流水url
		self.cashurl = 'https://pay.weixin.qq.com/index.php/cashmanage/QueryFlow?g_ty=ajax'
		#设置头部信息
		#self.user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"
		#self.headers = { 'User-Agent' : self.user_agent }
		self.headers = {
			'Connection':'keep-alive',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
		}
		#设置登陆时POST发送的用户信息
		self.username = ""
		#用户密码,此处为加密过后的密码
		self.password = ""
		self.mmpayPwdEdit_editName = ""
		#self.ecc_csrf_token = "b71b402c3aae7b25d459981a2e422db4"
		#self.post = {
		#	"ecc_csrf_token":self.ecc_csrf_token,#
		#	"mmpayPwdEdit_editName":self.mmpayPwdEdit_editName,
		#	"password":self.password,
		#	"username":self.username
		#}
		#self.postData = "username=libo001%401241244402&password=313435353630313836336C30FE3CE33057A9F2CAE54EC5E3C76D2E557561A\
#15CD02ABC3FAFF5A5A41AEBE5936CEDDCB153698E9853C657F80211FB9B5186069F31D402B62382245F53CDE2A41C5AB05E8\
#7B3F9CD21F7C8619334CA1102A1997A069562BB0BF2592C5170C3C13229C4EF9A1B5D018D7A37A9FC53D44278F815E30F39BCA99E34614D4E0B\
#&mmpayPwdEdit_editName=&ecc_csrf_token=b71b402c3aae7b25d459981a2e422db4"

		#print self.postData
		#设置cookie
		self.cookie = cookielib.LWPCookieJar()
		#设置cookie处理器
		self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie)
		#设置登陆时用的opener,它的open方法相当于urllib2.urlopen
		self.opener = urllib2.build_opener(self.cookieHandler,urllib2.HTTPHandler)

    #获取ecc_csrf_token
	def GetHomePage(self):
		request = urllib2.Request(self.HomeURL,headers=self.headers)
		response = self.opener.open(request)
		for ck in self.cookie:
			if ck.name == "ecc_csrf_cookie":
				self.ecc_csrf_token = ck.value



	def Login(self):
		#获取ecc_csrf_token

		self.post = {
			"ecc_csrf_token":self.ecc_csrf_token,
			"mmpayPwdEdit_editName":self.mmpayPwdEdit_editName,
			"password":self.password,
			"username":self.username
		}
		#将POST的数据进行编码
		self.postData = urllib.urlencode(self.post)
		#登陆商户后台
		request = urllib2.Request(self.loginURL,self.postData,self.headers)
		response = self.opener.open(request)
		#获取页面内容
		content = response.read()
		status = response.getcode()
		if status == 200:
			print "请求成功"

	def GetCashinfo(self):
		#直接发送ajax请求,获取json数据
		post = {
			'beginAmount':"0",
			'beginTime':"1452960000",
			'businessNo':"",
			'chargeType':"0",
			'ecc_csrf_token':self.ecc_csrf_token,
			'endAmount':"0",
			'endTime':"1455638399",
			'page':"1"
		}

		postdata = urllib.urlencode(post)
		print postdata
		request = urllib2.Request(self.cashurl,postdata,self.headers)
		response = self.opener.open(request)
		status = response.getcode()
		if status == 200:
			print "请求成功"
			print response.read()




test = wxPay()
test.GetHomePage()
test.Login()
test.GetCashinfo()

