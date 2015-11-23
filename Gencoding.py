#-*- coding: utf-8 -*-
__author__ = "coolfire"

import urllib2
import re
import sys
import wx
def get_address(x,y):

    #调用百度地图API接口,查询坐标对应的详细地址

    ak="axsMNgP4OEXycFoBIRCrIjTC"          #申请的百度ak
    localtion_x = x                        #要查询的维度值
    localtion_y = y                        #要查询的经度值
    url = "http://api.map.baidu.com/geocoder/v2/?ak=" + ak + "&callback=renderReverse&location=" + str(localtion_x) + "," + str(localtion_y) + "&output=json&pois=0"
    req = urllib2.Request(url)
    address_data = urllib2.urlopen(req).read()
    m  = re.search(r'formatted_address":"(.+?)",',address_data)
    if m:
        return m.group(1)
    else:
        print "Null"


def inquire(event):
    local_x = x_contents.GetValue()
    local_y = y_contents.GetValue()
    display_contents.SetValue(get_address(local_x,local_y).decode("utf8"))

app = wx.App()
win = wx.Frame(None,title=u"经纬度坐标查询工具",size=(500,500))
win.Show()

inquire_button = wx.Button(win,label=u"查询",pos=(400,10),size=(80,25))
inquire_button.Bind(wx.EVT_BUTTON,inquire)
wx.StaticText(win,label=u"请输入维度坐标",pos=(5,10),size=(100,25))
x_contents = wx.TextCtrl(win,pos=(150,10),size=(200,25))
wx.StaticText(win,label=u"请输入经度坐标",pos=(5,50),size=(100,25))
y_contents = wx.TextCtrl(win,pos=(150,50),size=(200,25))
display_contents = wx.TextCtrl(win,pos=(1,100),size=(500,400))
app.MainLoop()





