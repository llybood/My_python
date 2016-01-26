
# -*- coding: utf-8 -*-
import sys
import Image
import ImageDraw
import ImageFont

#打开要处理的图片
im = Image.open("C:\Users\coolfire\Pictures\haizw.jpg")
#print im.format,im.size,im.mode
# txt = '4'
#设置字体
font = ImageFont.truetype('C:\Windows\Fonts\Tahoma.ttf',36)
draw = ImageDraw.Draw(im)
draw.text((180,10),"4",font=font,fill=(255,0,0))
#保存文件
im.save("C:\Users\coolfire\Pictures\\target.png")

