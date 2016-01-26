#-*- coding: utf-8 -*-
__author__ = "coolfire"

import urllib
import urllib2
import re
import socket
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Get_Proxy:
    #定义一些初始化变量,
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        self.headers = { 'User-Agent' : self.user_agent }
        #self.High_hide = is_High_hide
        #self.pageIndex = 1

    #获取页面数据
    def getPage(self,proxy_url,pageindex=1):
        url = "http://www.xicidaili.com/wn/" + str(pageindex)
        request = urllib2.Request(url,headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            page_data = response.read()
            return page_data
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "连接失败,失败原因:" + e.reason
                return None

    #获取每页的地址列表,并且写入到文件中,以逗号分隔
    def getIplist(self):
        page_content = self.getPage()
        file_name = "proxy_list.txt"
        file = open("proxy_list.txt","w+")

        #print page_content
        pattern = re.compile(r'<td><img.*?alt=.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
        items = pattern.finditer(page_content)
        #print items
        for item in items:
             line_data = item.group(1)+ "," + item.group(2) + "," + item.group(3).strip() + "," + item.group(4).strip() + "," + item.group(5).strip() + "\n"
             try:
                file.writelines(line_data)
             except IOError,err:
                 print "打开文件错误:" + str(err)

        file.close()


    #检测代理ip的状态,需要传入代理ip,和端口号
    def CheckIpStatus(self,ip,port):
        #定义一个测试请求地址
        check_url = urllib2.Request("http://www.kuaiyoukuaidi.com")
        #创建proxyhandler
        handler = urllib2.ProxyHandler({"http": r'http://%s:%s' % (ip,port)})
        opener = urllib2.build_opener(handler)
        #添加头部
        opener.addheaders = [('User-Agent',self.user_agent)]
        try:
            response = opener.open(check_url,timeout=5)
        except:
            return False
        else:
            return True


    #检测代理ip列表文件,需要传入文件路径
    def Checkproxyfile(self,file_path):
         try:
            proxy_file = open(file_path)
            for line in proxy_file:
                ip_list = line.split(",")
                #调用检测函数,检测代理ip的有效性
                proxy_status = self.CheckIpStatus(ip_list[0],ip_list[1])
                if proxy_status:
                    print ip_list[0],ip_list[1]
                else:
                    print "%s is invalid" % (ip_list[0])
            proxy_file.close()
         except IOError,err:
             print "打开文件错误,原因\n%s" % (err,)





proxy = Get_Proxy()
#proxy.getIplist()
#proxy.CheckIpStatus("111.11.184.51",9999)
proxy.Checkproxyfile("F:\PycharmProjects\My_python\prox_list.txt")