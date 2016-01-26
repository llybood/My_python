#-*- coding: utf-8 -*-
#生成图片验证码

import Image
import ImageDraw
import ImageFont
import ImageFilter
import random
import string

#生成随机颜色
def rancolor():
    return (random.randint(30,240),random.randint(30,240),random.randint(30,240))

#生成文本随机颜色
def rantextcolor():
    return (random.randint(60,100),random.randint(60,100),random.randint(60,100))

#生成随机字符
def ranstr():
    return str(random.choice(string.letters))

width = 60 * 4
height = 100
font = ImageFont.truetype("C:\Windows\Fonts\Tahoma.ttf",48)

im = Image.new("RGB",(width,height),(255,255,255))
draw = ImageDraw.Draw(im)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rancolor())

for t in range(4):
    draw.text(((60 * t ) + 10,20),text=ranstr(),font=font,fill=rantextcolor())

image = im.filter(ImageFilter.BLUR)
image.save("test.jpeg","jpeg")