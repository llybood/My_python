#-*- coding: utf-8 -*-
__author__ = 'coolfire'


from math import sin, cos, pi ,radians , acos
import MySQLdb

#此脚本获取快小递系统内代理人与发展的用户之间的经纬度坐标，然后计算两者当时的距离


#定义函数,计算两点之间的距离(经纬度)
######算法:(计算球面间两点间的距离)
######R -----> 地球半径
######R*acos(cos(lat1*pi/180 )*cos(lat2*pi/180)*cos(lng1*pi/180 -lng2*pi/180)+
###### sin(lat1*pi/180 )*sin(lat2*pi/180))

def get_distance(LatA,LonA,LatB,LonB):
    #把经纬度转换成弧度
    R = 6370996.81 #地球半径(单位:m)
    radLatA,radLonA,radLatB,radLonB = map(radians,[LatA,LonA,LatB,LonB])
    distance = R * acos(cos(radLatA) * cos(radLatB) * cos(radLonA-radLonB) + sin(radLatA) * sin(radLatB))

    return distance

#get_distance(39.852795,116.593842,39.961948,116.463234)

def select_data(agent_name,scantime,area):
    #获取原始数据(连接远程数据库)
    conn = MySQLdb.connect(host="localhost",user="test",passwd="test",db="test",charset="utf8")
    cur = conn.cursor()
    #拼接sql语句,限定代理人姓名和日期为选择条件
    sql= "select userId,user_location_x,user_location_y,agent_location_x,agent_location_y from t_scan_qrcode where agentid=(select id from 用户 where real_name='%s') and date(FROM_UNIXTIME(scantime))='%s'" % (agent_name,scantime)
    #print sql
    cur.execute(sql)
    rows = cur.fetchall()
    #conn.close()
    human_count = 0                  #符合区域查询到的用户人数
    total_redpack_count = 0          #该代理人发展用户总的领取红包个数
    for row in rows:
        #print row
        #调用get_distance函数,获取距离,因为数据库存的是乘以1000000后的数字,所以需要换算
        #乘以浮点数,避免四舍五入
        distance = get_distance(row[1]/1000000.00,row[2]/1000000.00,row[3]/1000000.00,row[4]/1000000.00)
        #distance = get_distance(row[1]/1000000.00,row[2]/1000000.00,39.989956,116.323066)
        sql1 = "select count(*) from t_exchange_code_record where userOpenId=(select openid from 用户 where id='%s') and date(useTime)='%s'" % (row[0],scantime)
        #print distance
        #print sql1
        if distance <= area:
            human_count += 1
            #执行sql1语句,查询该代理人发展的每个用户领取红包数，并且累计
            cur.execute(sql1)
            peruser_redpack_count = cur.fetchone()[0]
            total_redpack_count += peruser_redpack_count


    print "扫码人数: %s\n用户领取红包数: %s" % (human_count,total_redpack_count)
    conn.close()
#select_data(agent_name="刘永明",scantime="2015-11-29",area=10000.00)


