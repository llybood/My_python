#-*- coding: utf-8 -*-
__author__ = "coolfire"

import socket

print "Creating socket"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Done"

print "Connect the server"
s.connet(("www.baidu.com",80))
print "done"