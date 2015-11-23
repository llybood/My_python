#-*- coding: utf-8 -*-
__author__ = "coolfire"

from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.cell import get_column_letter

import codecs
import os
import json
file_path = "F:\PycharmProjects\practise\student.txt"
dicts = json.load(open(file_path),encoding="utf-8")
#for k,v in dicts.iteritems():
dicts = sorted(dicts.iteritems(),key=lambda d:d[0],reverse=False)





def write_workbook():
    wb = Workbook()
    dest_filename = "student.xlsx"
    ws  = wb.active
    ws.title = "This is My test"
    #for row in range(1,len(dicts)+1):
    #for row in range(4):
    for k in dicts:
        data_list = (k[0],k[1][0],k[1][1],k[1][2],k[1][3])
        ws.append(list(tuple(data_list)))

    wb.save(filename= dest_filename)

write_workbook()




