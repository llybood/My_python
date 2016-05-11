#-*- coding: utf-8 -*-
__author__ = 'coolfire'

import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org') #返回Ntpstats对象
    #ctime将一个时间戳转换为字符串
    print ctime(response.tx_time) #tx_time 系统时间戳

if __name__ == "__main__":
    print_time()
