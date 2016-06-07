#-*- coding: utf-8 -*-
__author__ = "coolfire"

import argparse
import pcap
from construct.protocols.ipstack import ip_stack

def print_packet(pktlen,data,timestamp):
	"""
	Callback for printing the packet payload
	:param pktlen:
	:param data:
	:param timestamp:
	:return:
	"""
	if not data:
		return

	stack = ip_stack.parse(data)
	payload = stack.next.next.next
	print payload

def main():
	#setup commandline arguments
	parser = argparse.ArgumentParser(description="Packet Sniffer")
	parser.add_argument('--iface',action='store',dest="iface",default='eth0')
	parser.add_argument('--port',action='store',dest='port',type=int,default=80)
	#parse arguments
	given_args = parser.parse_args()
	iface,port = given_args.iface,given_args.port
	#start sniffing
	pc = pcap.pcapObject()
	pc.open_live(iface,1600,0,100)         #参数:设备名(设置为"any"或者为NULL时,则指定所有接口),数据包最大长度,是否设置为混杂模式(False则设置成混杂),超时时间ms)
	pc.setfilter('dst port %d' %port,0,0)  #参数:编译规则字符串,优化选项,网络掩码
	#netmask specifies the IPv4 netmask of the network on which packets are being captured; it is used only when checking for IPv4 broadcast addresses in the filter program. If the netmask of the network on which packets are being captured isn't known to the program, or if packets are being captured on the Linux "any" pseudo-interface that can capture on more than one network, a value of 0 can be supplied; tests for IPv4 broadcast addreses won't be done correctly, but all other tests in the filter program will be OK

	print 'Press CTRL+C to end capture'
	try:
		while True:
			pc.dispatch(1,print_packet)    #参数:返回前捕获多少数据包,回调函数
	except KeyboardInterrupt:
			print "Packet statistics: %d packets received, %d packets dropped,%d packets dropped by the interface" % pc.stats()

if __name__ == "__main__":
	main()
