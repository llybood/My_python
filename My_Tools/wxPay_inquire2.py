#-*- coding: utf-8 -*-
__author__ = "coolfire"
import os,time
import selenium
import win32api
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains

#创建一个模拟登陆爬虫类,
#利用自动化测试工具selenium，
#启动firefox获取需要的内容
class SimLand():

	def __init__(self):
		#设置firefox路径变量
		self.firefoxBin = os.path.abspath(r"D:\Program Files\Mozilla Firefo\firefox.exe")
		os.environ["webdriver.firefox.bin"] = self.firefoxBin
		#设置firefox用户配置文件
		self.profileDir = os.path.abspath(r"C:\Users\coolfire\AppData\Roaming\Mozilla\Firefox\Profiles\9v1jywsn.default")
		self.profile = webdriver.FirefoxProfile(self.profileDir)



	def Getbaidu(self):
		driver = webdriver.Firefox()
		driver.get("http://www.baidu.com")
		assert(u"百度" in driver.title)
		elem = driver.find_element_by_name("wd")
		elem.send_keys("selenium")
		elem.send_keys(Keys.RETURN)
		driver.close()
		driver.quit()

	def wxPayLogin(self):
		driver = webdriver.Firefox(self.profile)
		driver.get("https://pay.weixin.qq.com/index.php/home/login")
		assert(u"微信支付" in driver.title)
		elem_username = driver.find_element_by_id("idUserName")
		elem_username.send_keys("")
		time.sleep(1)
		elem_password = driver.find_element_by_id("idPassword")
		ActionChains(driver).double_click(elem_password).perform()
		win32api.keybd_event(ord('a'),0,0,0)

		time.sleep(2)
		driver.find_element_by_id("do_login").click()
		#driver.close()
		#driver.quit()




test=SimLand()
test.wxPayLogin()
