#!/usr/bin/env python3
#_*_coding:utf-8_*_

import sys
import json 
import urllib
import urllib.request
import base64
import requests

#reload(sys) 
import importlib
importlib.reload(sys)
#sys.setdefaultencoding("utf-8")

def get_access_token(): 
    url = "https://openapi.baidu.com/oauth/2.0/token" 
    body = { 
    "grant_type":"client_credentials", 
    "client_id" :"uV9sk3dsVPLtpumoarkY13Eh", 
    "client_secret":"e2ea6a3db3eea70b5c263f75efb7f99c", 
            }   

    r = requests.post(url,data=body,verify=True)
 #   respond = json.loads(r.txt)
    respond = json.loads(r.text)
    return respond["access_token"]
def yuyinshibie_api(audio_data,token): 
    speech_data = base64.b64encode(audio_data).decode("utf-8") 
    speech_length = len(audio_data) 
    post_data = { 
    "format" : "wav", 
    "rate" : 16000, 
    "channel" : 1, 
    "cuid" : "B8-27-EB-BA-24-14", 
    "token" : token, 
    "speech" : speech_data, 
    "len" : speech_length 
                }

    url = "http://vop.baidu.com/server_api"
    json_data = json.dumps(post_data).encode("utf-8")
    json_length = len(json_data)
#print(json_data)

    #req = urllib.Request(url, data=json_data)
    req = urllib.request.Request(url, data=json_data)
    req.add_header("Content-Type", "application/json")
    req.add_header("Content-Length", json_length)

#print("asr start request\n")
    #resp = urllib.urlopen(req)
    resp = urllib.request.urlopen(req)
#print("asr finish request\n")
    resp = resp.read()
    resp_data = json.loads(resp.decode("utf-8"))   
    if resp_data["err_no"] == 0:
        return resp_data["result"]
    elif resp_data["err_no"] == 3301:
        print("麦克风没有检测到有效声音，可能没有人与机器人说话")
        return None
    else:
        print(resp_data)
        return None
def asr_main(filename,tok): 
    try: 
        f = open(filename, "rb") 
        audio_data = f.read() 
        f.close() 
        resp = yuyinshibie_api(audio_data,tok) 
        return resp[0] 
    except Exception as e: 
        #print (e)
        return "识别失败".encode("utf-8")
