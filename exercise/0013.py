#-*- coding: utf-8 -*-
__author__ = "coolfire"

import re
import urllib
import os
import sys


def get_html_pic(url):
    html_file = urllib.urlopen(url)
    html = html_file.read()
    html_file.close()
    regex = re.compile(r'<img.*?src="(http://.+?)".*?>')    #定义正则表达式对象
    links_list = regex.finditer(html)                       #返回所有匹配子串的一个迭代器对象，用于迭代
    target_path = "F:\PycharmProjects\images"
    file_name = 0
    #判断路径是否存在,不存在则创建
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    def report(count,blockSize,totalSize):
        percent = int(count*blockSize*100/totalSize)
        sys.stdout.write("\r%d%%" % percent + "complete")
        sys.stdout.flush()



    for file_link in links_list:
        m = file_link.group(1)
        target_file = target_path + "\%s.jpg" % file_name
        sys.stdout.write('\rFetching....' + m + '.....\n')
        urllib.urlretrieve(m,target_file,reporthook=report)
        sys.stdout.write("\rDownload complete,saved as %s" % target_file + "\n\n")
        file_name += 1





get_html_pic("http://tieba.baidu.com/p/4164929765")


