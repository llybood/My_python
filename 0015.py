#-*- coding: utf-8 -*-
__author__ = "coolfire"
import json
from collections import OrderedDict

city_data = json.load(open("city.txt"),encoding="utf8",object_pairs_hook=OrderedDict)
print city_data
