#-*- coding: utf-8 -*-
__author__ = "coolfire"

import mechanize
import cookielib



def login():
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	#setting
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_debug_http(True)
	br.addheaders = [('User-agent',"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0")]
	br.set_handle_refresh(mechanize._http.HTTPRefererProcessor(),max_time=1)
	#open the login page
	br.open('https://pay.weixin.qq.com/index.php/home/login')
	br.select_form(nr = 0)
	# br.form.set_all_readonly(False)
	#获取ecc_csrf_token
	for ck in cj:
		if ck.name == "ecc_csrf_cookie":
			ecc_csrf_token = ck.value
	br['username'] = ""
	br['password'] = ""
	#br['ecc_csrf_token'] = ecc_csrf_token
	resp = br.submit()
	print resp.read()

	def get_urls(url):
		browser = br.open(url)
		return browser

br = login()

