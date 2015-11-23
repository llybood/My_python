#-*- coding: utf-8 -*-

import os
#统计某一目录下所有代码文件的代码行数,每个文件分别列出行数

rootdir="F:\git_code\wechat_dxm.git\web"

def count_code(file):
    lines = 0
    files = open(file,"r")
    for line in files.readlines():
        lines += 1
    print file + " have %s rows" % lines
    files.close()


def countcode_dir(dir):
    for f in os.listdir(dir):
        file_path = os.path.join(dir,f)
        if os.path.isfile(file_path):
            count_code(file_path)
        else:
            countcode_dir(file_path)

countcode_dir(rootdir)







