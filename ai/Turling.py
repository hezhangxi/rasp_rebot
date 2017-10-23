#!/usr/bin/env python
#coding: utf-8

import requests
import json
import sys
#reload(sys)
import importlib

importlib.reload(sys)

#sys.setdefaultencoding("utf-8")


def Tuling(words):
    Tuling_API_KEY = "9d05122cbe3244fca6733994642978d4"

    #body = {"key":Tuling_API_KEY,"info":words.encode("utf-8")}
    body = {"key":Tuling_API_KEY,"info":words}

    url = "http://www.tuling123.com/openapi/api"
    r = requests.post(url,data=body,verify=True)

    if r:
        date = json.loads(r.text)
        print (date["text"])
        return date["text"]
    else:
        return None
