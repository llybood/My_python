# -*- coding:utf-8 -*-
#生成激活码,并且保存到数据库中
import string
import random
import sys
import MySQLdb

coupon_length = 20                           #激活码的长度
coupon_count = 200                           #生成激活码的数量
coupon_seed=string.digits + string.letters   #生成激活码的种子
coupon_real = ""
host = "localhost"
user = "root"
password = "root"
#定义生成激活码的函数
def generate_coupon():
    coupon = []
    global coupon_real
    for i in range(coupon_length):
        coupon.append(random.choice(coupon_seed))
    coupon_real = "".join(coupon)
    return coupon_real

#if __name__ == "__main__":
#    for i in range(coupon_count):
#       print generate_coupon()
#定义操作数据库函数
def insert_mysql():
    conn = MySQLdb.connect(host,user,password,"practise",charset="utf8")
    cur = conn.cursor()
    sql = """INSERT INTO coupon (coupon) values("%s")""" % coupon_real
    try:
        cur.execute(sql)
        #conn.commit()
    except MySQLdb.Error,e:
        print "MySQL Error %d : %s" % (e.args[0],e.args[1])
        conn.rollback()

    conn.close()


for i in range(coupon_count):
    generate_coupon()
    insert_mysql()
