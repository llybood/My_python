#-*- coding: utf-8 -*-
__author__ = "coolfire"

import urllib
import urllib2
import re
import thread
import time


#糗事百科爬虫类
class QSBK:

    #初始化方法,定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放段子的变量,每一个元素是每一页的段子
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    #传入某一页面的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url,headers = self.headers,)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request,timeout=10)
            #将页面转化为UTF-8编码
            pageCode = response.read()
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print "连接糗事百科失败,错误原因",e.reason
                return None

    #传入某一页代码,返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        #print pageCode
        if not pageCode:
            print '页面加载失败....'
            return None
        pattern = re.compile('<div.*?author.*?alt="(.*?)".*?content">(.*?)</div>.*?number">(.*?)</i>',re.S)

        items = re.findall(pattern,pageCode)
        #用来存储每页的段子
        pageStories = []
        #遍历正则表达式匹配的信息
        for item in items:
            #print item[0],item[1],item[2]
            #print item
            #是否含有图片
            #haveImg = re.search("img",item[3])
            #如果不含有图片,把它加入list中
            #if not haveImg:
            #    replaceBR = re.compile('<br/>')
            #    text = re.sub(replaceBR,"\n",item[1])
                #item[0]是一个段子的发布者,item[1]是内容,item[2]是发布时间,item[4]是点赞人数
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    #加载并提取页面的内容,加入到列表中
    def loadPage(self):
        #如果当前未看的页面数少于2,则加载新的一页:
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新的一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完以后页码索引加一,表示下次读取下一页
                    self.pageIndex += 1
                    print self.pageIndex



    #调用该方法,每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        #遍历一页的帖子
        for story in pageStories:
            #等待用户输入:
            input = raw_input()
            #每当输入回车一次,判断下次是否也加载新页面
            self.loadPage()
            #如果输入Q则程序结束
            if input == "Q":
                self.enable = False
                return
            print "第%d页\t发布人:%s\t赞:%s\n%s" % (page,story[0],story[2],story[1])

    #开始方法
    def start(self):
        print "正在读取糗事百科,按回车查看新帖子,Q退出"
        #使变量为True,程序可以正常运行
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #局部变量,控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                #从全部list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage += 1
                #将全部list中第一个元素删除,因为已经取出
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
#spider.getPage(1)
#spider.getPageItems(1)
spider.start()
#spider.loadPage()
