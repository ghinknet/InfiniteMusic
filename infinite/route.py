'''
   Copyright Ghink Network Studio © 2014
   MIT Fengming High School Techy Group & Radio Station
   Website: https://www.ghink.net, https://radio.fmhs.club, https://techy.fmhs.club
   Main Program by Bigsk (https://www.xiaxinzhe.cn)
'''

from __init__ import *

import json, time

def ping():
   return json.dumps({
      "ping": "pong",
      "time": time.time()
   },
   ensure_ascii = False,
   sort_keys = True,
   indent = 4,
   separators = (',', ':'))

APP.add_url_rule("/ping", view_func = ping)