#-*- coding: utf-8 -*-

import Image
import os
rootdir = "C:\Users\coolfire\Pictures\gongti"                  #待处理目录
outdir  = "C:\Users\coolfire\Pictures\gongti_copy"             #输出目录
#定义图像处理函数
def resize_image(file,outfile):
    im = Image.open(file)
    out = im.resize((1000,600),Image.ANTIALIAS)
    out.save(outfile)


for f in os.listdir(rootdir):
    file_path = os.path.join(rootdir,f)
    outfile_path = os.path.join(outdir,f)
    resize_image(file_path,outfile_path)