#! python3
# newsbot.py - get a title of news and make a link.

import datetime
import requests
import bs4

def time_check():
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

def get_news():
    res = requests.get('http://news.yahoo.co.jp')
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text)
    html = soup.select('.ttl a')

    for i in range(0, 8):
        html[i].find('span').decompose()
        title = html[i].text
        links = html[i].get('href')
        if title.endswith('new'):
            print(title.replace('new', ''))
        else:
            print(title)
        print(links)

get_news()
time_check()
