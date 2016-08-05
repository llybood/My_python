#-*- coding: utf-8 -*-
__author__ = 'coolfire'

login_url = 'http://testmanage.hybtco.com/office/index'
username = "admin"
password = "admin@321.com"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get(login_url)
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_css_selector(css_selector="a.ui.fluid.large.teal.button").click()

#点击会员管理
try:
	element = WebDriverWait(driver,60).until(EC.title_is(u"系统管理"))
except:
	print u"系统异常"
	driver.quit()
finally:
	driver.find_element_by_css_selector(css_selector="#nav > div:nth-child(3) > div.panel-header.panel-header-noborder.accordion-header > div.panel-title.panel-with-icon").click()
	driver.find_element_by_css_selector(css_selector="#nav > div:nth-child(3) > div.panel-body.panel-body-noborder.accordion-body > div > ul > li:nth-child(3) > div > a > span.nav").click()
