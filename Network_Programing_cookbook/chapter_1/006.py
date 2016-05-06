#-*- coding: utf-8 -*-
__author__ = "coolfire"
import socket

def test_socket_modes():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setblocking(1)
	s.settimeout(2)
	s.bind(("127.0.0.1",9999))

	socket_address = s.getsockname()
	print "Trival Service launched on-socket: %s" % str(socket_address)
	while 1:
		s.listen(1)

if __name__ == "__main__":
	test_socket_modes()