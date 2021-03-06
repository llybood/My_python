#-*- coding: utf-8 -*-
__author__ = "coolfire"

import socket
import sys

import argparse

#host = 'localhost'

def echo_client(host,port):
	"""
	A simple echo clinet
	:param port:
	:return:
	"""
	#Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#Connect the socket to the server
	server_address = (host,port)
	print "Connect to %s port %s" % server_address
	sock.connect(server_address)

	#Send data
	try:
		# Send data
		message = "Test message,This will be echoed"
		print "Sending %s" % message
		sock.sendall(message)
		#Look for the response
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print "Received: %s" % data
	except socket.errno,e:
		print 'Socket error: %s' %str(e)
	except Exception, e:
		print "Other exception: %s" %str(e)
	finally:
		print "Closing connection to the server"
		sock.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Socket Server Example")
	parser.add_argument("--port",action="store",dest="port",type=int,required=True)
	parser.add_argument("--host",action="store",dest="host",required=True)
	given_args = parser.parse_args()
	host = given_args.host
	port = given_args.port
	echo_client(host,port)
