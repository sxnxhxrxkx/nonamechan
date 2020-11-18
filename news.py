from __future__ import print_function
import datetime
from dateutil.relativedelta import relativedelta
import pickle
import os.path
import pandas as pd
from bs4 import BeautifulSoup
import requests

# Google カレンダーに接続しイベントを取得しDataFrameとして取得
def getNewsDf():
    # Define
    url_org = "https://players.wotvffbe.com"
    url = url_org + "/all/"

    # DataFrameの定義
    df = pd.DataFrame(columns=['time','content','link'])

    # コンテンツの取得
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml") #文字化け対策
    arts = soup.find_all('article')

    for art in arts:
        time = art.find('time').get_text().replace('\n','').replace('\t','').strip()
        content = art.find('h2').get_text().replace('\n','').replace('\t','')
        link = url_org + art.find('a').get('href')
        df = df.append({'time':time, 'content': content,'link': link}, ignore_index=True)

    # 次のページ以降
    #https://players.wotvffbe.com/all/page/2/
    return df

def getNewsDfDetail():
    # Define
    url_org = "https://players.wotvffbe.com"
    url = url_org + "/all/"
    cnt = 10

    # DataFrameの定義
    df = pd.DataFrame(columns=['time','content','link'])

    # コンテンツの取得
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml") #文字化け対策
    arts = soup.find_all('article')

    for art in arts:
        time = art.find('time').get_text().replace('\n','').replace('\t','').strip()
        content = art.find('h2').get_text().replace('\n','').replace('\t','')
        link = url_org + art.find('a').get('href')
        df = df.append({'time':time, 'content': content,'link': link}, ignore_index=True)

    # 次のページ以降
    #https://players.wotvffbe.com/all/page/2/

    try:
        for i in range(cnt):
            url_page = url + "page/" + str(i + 2) +"/"
            res = requests.get(url_page)
            soup = BeautifulSoup(res.content, "lxml") #文字化け対策
            arts = soup.find_all('article')
            for art in arts:
                time = art.find('time').get_text().replace('\n','').replace('\t','').strip()
                content = art.find('h2').get_text().replace('\n','').replace('\t','')
                link = url_org + art.find('a').get('href')
                df = df.append({'time':time, 'content': content,'link': link}, ignore_index=True)
    except:
        pass
    return df

# お知らせの取得
def getNews(msg, msgcontent):
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')
        if '直近' in datas:
            msg = '直近のお知らせだね！'
            df = getNewsDf()
        elif '過去' in datas:
            msg = '過去のお知らせだね！'
            df = getNewsDfDetail()
            df = df[:50]
        else:
            msg = '過去のお知らせを取得するね…'
            df = getNewsDfDetail()
            msg += '【' + datas[1] + '】でフィルタリングするよ！'
            df = df[df['content'].str.contains(datas[1])]

        if len(datas) > 2:
            msg += '【' + datas[2] + '】でフィルタリングするよ！'
            df = df[df['content'].str.contains(datas[2])]
    else:
        msg = 'とりあえず直近のお知らせを取得するね！'
        df = getNewsDf()
    return msg, df