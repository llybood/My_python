#-*- coding: utf-8 -*-
__author__ = 'coolfire'

import socket
import struct
import sys
import time

NTP_SERVER = '0.uk.pool.ntp.org'
TIME1970 = 2208988800L  #1970年1月1日NTP时间戳


def sntp_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'  #\0相当于\x00,客户端发送给NTP服务器的数据,总共48字节数据,后面47位以数据0填充
    client.sendto(data,(NTP_SERVER,123))
    data,address = client.recvfrom(1024)
    if data:
        print "Response received from: ",address
    t = struct.unpack('!12I',data)[10] #用struct函数处理二进制数据
    t -= TIME1970
    print '\tTime=%s' % time.ctime()


if __name__ == '__main__':
    sntp_client()
