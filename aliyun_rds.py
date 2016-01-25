#-*- coding: utf-8 -*-
__author__ = "coolfire"
#阿里云rds自动下载备份脚本,
#借鉴了阿里云官方提供的下载脚本,
#添加了下载进度条,便于在手动下载的时候显示下载进度
import sys,shutil
import re
import urllib,urllib2,socket
import datetime,time
import aliyun.api
aliyun.setDefaultAppInfo("********************","***********************")

#实例区域
my_region = "cn-beijing"
#实例名称
my_rdsname = "rds**********"
#要下载备份的开始时间,指定昨天
my_begintime = datetime.date.today() - datetime.timedelta(days=1)
#my_begintime = "2016-01-20"
#要下载备份的结束时间,指定当前时间
my_overtime = datetime.date.today()
#my_overtime = "2016-01-22"

a = aliyun.api.Rds20140815DescribeBackupsRequest()
a.RegionID = my_region
a.DBInstanceId = my_rdsname
a.StartTime = str(my_begintime) + "T00:00Z"
a.EndTime = str(my_overtime) + "T00:00Z"
#设置默认超时时间
socket.setdefaulttimeout(30)

#定义回调函数,用与显示下载进度
def down_progress(count,persize,totalsize):
	'''
    @count: 已经下载的数据块个数
	@persize: 每个数据块的大小
	@totalsize:    下载总数据量
	'''
	#pbar = ProgressBar(maxval=c).start()
	#while ( a*b <= c ):
	#	pbar.update(a*b)
	#pbar.finish()
	per = 100 * count * persize / totalsize
	if per > 100:
		per = 100
	sys.stdout.write("The progress: [%s%s] %i%%\r"  % ((int(per) * '#'),"-" * int(100-per),per))
	sys.stdout.flush()



try:
	f = a.getResponse()
	if ("Code" in f):
		print "False"
		print f['Code']
		print f["Message"]
	else:
		#用正则表达式匹配url,返回url列表
		f = str(f)
		my_re = re.compile(r"(http://.*?)',")
		url_list = my_re.findall(f)
		list_count = len(url_list)
		if (list_count == 0):
			print "无备份文件,程序即将退出"
			os._exit(2)
		else:
			print u"有%s个备份文件需要下载,正在下载,请稍后" % (list_count,)
			for m in url_list:
					urllib.urlretrieve(m,filename="f:\\RDS-Backup.tar.gz",reporthook=down_progress)
					now = time.strftime("%Y%m%d")
					newname = "f:\\" + now + "-RDS-Backup.tar.gz"
					shutil.move("f:\\RDS-Backup.tar.gz",newname)
					print "\n备份完成"
except Exception,e:
	print e
