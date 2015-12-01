#-*- coding: utf-8 -*-
__author__ = "coolfire"

import urllib
import urllib2
import MySQLdb
import os
import sys
import re
from openpyxl import Workbook

#编写快小递后台扩展功能,直接查询数据库获取一些数据信息,并按照一定规则来处理
#所以我们在这里把它封装成一个类,然后逐渐添加方法,来扩展我们的功能

class kuaixiaodi_extend:
    def __init__(self):
        #初始化一些变量
        self.user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        self.header={ "User_Agent" : self.user_agent }
        #手机号码归属地查询api接口地址
        self.ownership_api="https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel="
        #数据库变量
        #self.host="localhost"
        #self.user="test"
        #self.port=3306
        #self.password="test"

    #获取数据库数据,并且储存在xlsx文件中
    def Get_mysqldata(self,database,sql):
        #创建工作薄,用来保存数据
        wb = Workbook()
        ws1 = wb.active
        phone_list=[]
        try:
            #连接数据库
            conn = MySQLdb.connect(host=self.host,user=self.user,port=self.port,passwd=self.password,db=database)
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            row_count = cur.rowcount

            cur.close()
            for row_number in range(row_count):
                for row in rows:
                    ws1.append(row[:])
            wb.save("phone.xlsx")
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0],e.args[1])

    #查询手机号码归属地
    def Inquire_phoneownership(self,phone):
        url = self.ownership_api + phone
        request = urllib2.Request(url,headers=self.header)
        try:
            response = urllib2.urlopen(request,timeout=5)
            #读取页面内容后,需要先以GBK解码,然后再以utf-8编码
            page_data = response.read().decode("gbk").encode("utf-8")
            #print page_data
            pattern = re.compile(r".*carrier:'(.+?)'")
            m = pattern.search(page_data)
            if m:
                return m.group(1)
            else:
                return "None"
        except urllib2.URLError,e:
            if hasattr(e.reason):
                print "连接失败,失败原因: %s" % e.reason
                return None

    #批量查询手机号码归属地
    #def Batch_inquire_phone(self,)




test=kuaixiaodi_extend()
test.Get_mysqldata("kuaiyou","select phone from t_ad_active")
#test.Inquire_phoneownership("15010589936")


