# -*- coding: utf-8 -*-
__author__ = 'coolfire'
#生成激活码或者优惠券
import string
import random
import sys

coupon_length = 20
coupon_count = 200
coupon_seed=string.digits + string.letters   #生成优惠码或者激活码的种子

#定义生成优惠码的函数
def generate_coupon():
    coupon = []
    for i in range(coupon_length):
        coupon.append(random.choice(coupon_seed))
    return "".join(coupon)

if __name__ == "__main__":
    for i in range(coupon_count):
        print generate_coupon()