'''
   Copyright Ghink Network Studio © 2014
   MIT Fengming High School Techy Group & Radio Station
   Website: https://www.ghink.net, https://radio.fmhs.club, https://techy.fmhs.club
   Main Program by Bigsk (https://www.xiaxinzhe.cn)
'''

from __init__ import *

import route

import os, json
from threading import Thread
from flask import Flask
from urllib.request import urlopen

# Define network check function
def network(source = r"http://www.baidu.com", retry = 3):
    flag = False
    for _ in range(retry):
        try:
            fp = urlopen(source)
            fp.read(100).decode()
            fp.close()
        except:
            pass
        else:
            flag = True
    return flag
# Define json check function
def check_json(content):
    try:
        json.loads(content)
    except:
        return False
    else:
        return True
    finally:
        return False
# Define main function
def main():
    APP.run("127.0.0.1", 8000)

if __name__ == "__main__":
    main()