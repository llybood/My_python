#-*- coding: utf-8 -*-
__author__ = "coolfire"
import socket
import sys

def reuse_socket_addr():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print "Old sock state: %s" % old_state

	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print "New sock state: %s" % new_state
	