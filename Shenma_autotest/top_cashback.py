#-*- coding: utf-8 -*-
__author__ = 'coolfire'

login_url = 'http://testmanage.hybtco.com/office/index'
username = "admin"
password = "admin@321.com"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
	element1 = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#nav > div:nth-child(3) > div.panel-body.panel-body-noborder.accordion-body > div > ul > li:nth-child(3) > div > a > span.nav")))
	driver.find_element_by_css_selector(css_selector="#nav > div:nth-child(3) > div.panel-body.panel-body-noborder.accordion-body > div > ul > li:nth-child(3) > div > a > span.nav").click()
	driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="tabPanel-35"]/iframe'))
	elem = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"body > div.article > table > tbody > tr:nth-child(2) > td:nth-child(9)")))
	rowCount = driver.find_element_by_css_selector(css_selector="body > div.article > table > tbody")
	#charge = driver.find_element_by_css_selector(css_selector="body > div.article > table > tbody > tr:nth-child(3cd j) > td:nth-child(9)").text
