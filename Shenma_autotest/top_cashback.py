#-*- coding: utf-8 -*-
__author__ = 'coolfire'

login_url = 'http://testmanage.hybtco.com/office/index'
username = "admin"
password = "admin@321.com"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get(login_url)
now_handle = driver.current_window_handle
print now_handle
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_css_selector(css_selector="a.ui.fluid.large.teal.button").click()
#点击会员管理
driver.find_element_by_css_selector(css_selector="#nav > div:nth-child(3) > div.panel-header.panel-header-noborder.accordion-header > div.panel-title.panel-with-icon").click()
driver.find_element_by_css_selector(css_selector="#nav > div:nth-child(3) > div.panel-body.panel-body-noborder.accordion-body > div > ul > li:nth-child(3) > div > a > span.nav").click()
#driver.find_element_
