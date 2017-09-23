#! python3
# newsbot.py - get a title of news and make a link.

import datetime
import requests
import bs4
from requests_oauthlib import OAuth1Session

def hour_check():
    now = datetime.datetime.now()
    if now.hour == 0:
        return True
    elif now.hour == 6:
        return True
    elif now.hour == 12:
        return True
    elif now.hour == 18:
        return True
    else:
        return False

def minute_check():
    now = datetime.datetime.now()
    if now.minute == 0:
        return True
    elif now.minute % 5 == 0:
        return True
    else:
        return False

def con_web():
    res = requests.get('http://news.yahoo.co.jp')
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text)
    html = soup.select('.ttl a')
    return html

def get_news():
    html = con_web()
    for i in range(0, 8):
        html[i].span.decompose()
        title = html[i].text
        links = html[i].get('href')
        if title.endswith('new'):
            print(title.replace('new', ''))
        else:
            print(title)
        print(links)

def get_stock():
    res = request.get('http://finance.yahoo.co.jp')

def con_twitter():
    CON_KEY = ''
    CON_SEC_KEY = ''
    ACC_TOKEN = ''
    ACC_TOKEN_SEC = ''

    url = 'https://api.twitter.com/1.1/statuses/update.json'

    html = con_web()
    now = datetime.datetime.now()
    for i in range(0, 10):
        if now.minute / 5 == i:
            html[i].span.decompose()
            title = html[i].text
            links = html[i].get('href')
        else:
            return False

    params = {'status': title + links}
    print(params)
    twitter = OAuth1Session(CON_KEY, CON_SEC_KEY, ACC_TOKEN, ACC_TOKEN_SEC)
    request = twitter.post(url, params=params)

    if request.status_code == 200:
        print('OK!')
    else:
        print('Error:' % request.status_code)

con_twitter()
