#!/usr/bin/env python3
#_*_coding:utf-8_*_3

import sys 
#import urllib
import urllib.request
import json 
import os 
import yuyinshibie

#reload(sys) 
#sys.setdefaultencoding("utf8")
import importlib
importlib.reload(sys)

def yuyinhecheng_api(tok,tex): 
    cuid = "B8-27-EB-BA-24-14" 
    spd = "4" 
    url = "http://tsn.baidu.com/text2audio?tex="+tex+"&lan=zh&cuid="+cuid+"&ctp=1&tok="+tok+"&per=3" 
#print url 
#response = requests.get(url) 
#date = response.read() 
    return url

def tts_main(filename,words,tok): 
    voice_date = yuyinhecheng_api(tok,words)

    f = open(filename,"wb")
    f.write(voice_date)
    f.close()
