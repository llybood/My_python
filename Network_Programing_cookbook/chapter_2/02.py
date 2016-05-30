#-*- coding: utf-8 -*-
__author__ = "coolfire"

import os
import socket
import SocketServer
import threading


SERVER_HOST = "localhost"
SERVER_PORT = 0
BUF_SIZE = 1024

#create the client
def client(ip,port,message):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(ip,port)
	try:
		sock.sendall(message)
		response = sock.recv(BUF_SIZE)
		print "Client received: %s" % response
	finally:
		sock.close()

#create the server class
class ThreadTcpServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
	pass

#create the handle class
class ThreadTCPRequestHandler(SocketServer.BaseRequestHandler):
	#overriding its handle() method
	def handle(self):
		#receive the client data
		data = self.request.recv(BUF_SIZE)
		current_thread = threading.current_thread()
		response = "%s : %s" % (current_thread.name,data)
		self.request.sendall(response)

if __name__ == "__main__":
	server = ThreadTcpServer((SERVER_HOST,SERVER_PORT),ThreadTCPRequestHandler)
	ip,port = server.server_address
	server_thread = threading.Thread(target=server.serve.forever())
	server_thread.setDaemon(True)
	server_thread.start()
	print "Server loop running on thread: %s" % server_thread.name

	#Run clients
	client1 = client(ip,port,"Hello from client '1'")
	client2 = client(ip,port,"Hello from client '2'")
	client3 = client(ip,port,"Hello from client '3'")

    #Server cleanup
	server.shutdown()






