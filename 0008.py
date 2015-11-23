#-*- coding: utf-8 -*-
__author__ = "coolfire"

import re

file = open("baidu.html","r")

regex = re.compile(r'<body.*?>(.*)</body>',re.S)
#regex = re.compile(r'<p>(.+)<p>')
string = file.read()
m = regex.search(string)
if m:
    print m.group(1)
else:
    print 'Not match'

