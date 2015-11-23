#-*- coding: utf-8 -*-
__author__ = "coolfire"

import fileinput
import re

for line in fileinput.input("test.html"):
    regex = re.compile(r'href="(http:.+?)"')
    #m = regex.search(line)
    m = regex.finditer(line)       #re.finditer() 返回RE匹配的所有子串,并把它们作为一个迭代器返回,无匹配，则返回空列表
    for links in m:
        print links.group(1)
    else:
        pass