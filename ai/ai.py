#!/usr/bin/env python3
# coding: utf-8

import os
import time
import yuyinhecheng
import Turling
import yuyinshibie


tok = yuyinshibie.get_access_token()
url = "http://tsn.baidu.com/text2audio?tex=您好，我是何帅,有什么可以帮到您的吗！&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
os.system('mpg123 "%s"'%url)

switch = True
while switch:
    #开始录音
    os.system('echo "Linux2008" | sudo -S arecord -D "plughw:CARD=PCH" -f S16_LE -r 16000 -d 3 /home/pi/Desktop/voice.wav')
    time.sleep(0.5)
    #将语音文件转换成为文字
    info = str(yuyinshibie.asr_main("/home/pi/Desktop/voice.wav",tok))

    if 'b\\' in info:
        continue

    if '关闭' in info:
        while True:
            os.system('echo "Linux2008" | sudo -S arecord -D "plughw:CARD=PCH" -f S16_LE -r 16000 -d 3 /home/pi/Desktop/voice.wav')
            time.sleep(10)

            info = str(yuyinshibie.asr_main("/home/pi/Desktop/voice.wav",tok))
            if '开启' in info:
                break

        url = "http://tsn.baidu.com/text2audio?tex=开启成功&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
        os.system('mpg123 "%s"'%url)


    elif '暂停' in info:
        url = "http://tsn.baidu.com/text2audio?tex=开始暂停&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
        os.system('mpg123 "%s"'%url)
        time.sleep(10)

        url = "http://tsn.baidu.com/text2audio?tex=暂停结束&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
        os.system('mpg123 "%s"'%url)
        continue


    else:
        #将百度从语音转换过来的文字提交给图灵机器人后台进行分析，并将答案以文字的形式赋值给tex变量
        tex = Turling.Tuling(info)

        '''
        mystr = "那就换个方式"

        mystr2 = "亲爱的，当天请求次数已用完"
        if mystr2 in tex:
            url = "http://tsn.baidu.com/text2audio?tex=对不起，我今天说话太多，被百度禁言了，明天再见了，主人！&lan=zh&cuid=B8-27-EB-BA-24-14&ctp=1&tok="+tok+"&per=3"
            os.system('mpg123 "%s"'%url)
            continue
            
        if mystr in tex:
            continue
        '''
        #将文字提交给百度语音后台转换成为语音文件，并将语音文件完整路径赋值给url变量
        url = yuyinhecheng.yuyinhecheng_api(tok,tex)
        #调用系统mpg123播放器，播放url路径的语音文件
        os.system('mpg123 "%s"'%url)
        time.sleep(0.5)
