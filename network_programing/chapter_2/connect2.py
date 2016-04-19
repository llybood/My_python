#-*- coding: utf-8 -*-
__author__ = "coolfire"

import socket

socket.timeout = 5

print "Creating socket"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "done"

print "Looking up the port"
port = socket.getservbyname('http','tcp')
print 'done'

print 'Connect the server'
s.connect(('www.baidu.com',80))
print 'done'