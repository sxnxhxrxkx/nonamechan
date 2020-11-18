#ClientID
#713695703931-96evkgsumethcakcjq8bmte1blrafv9m.apps.googleusercontent.com
#ClientSecret
#rrh1rtOBXMYXeQQBZtifayGP

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
import configparser
config = configparser.ConfigParser()
config.read('calender.ini')
#TOKEN = config['noname']['TOKEN']

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Google カレンダーに接続しイベントを取得しDataFrameとして取得
def getEventsDf():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=config['calender']['id'],
                                        timeMin=now,
                                        maxResults=10, 
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    # DataFrameの定義
    df = pd.DataFrame(columns=['etag','eid','start','end','category','event'])

    # event のDataFrame格納
    for event in events:
        eTag = event['etag']
        eId = event['id']
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        try:
            category, event = event['summary'].split("：")
        except:
            category = 'その他'
            event = event['summary']
            
        df = df.append({'etag':eTag, 'eid': eId,'start': start, 'end': end, 'category': category, 'event': event}, ignore_index=True)
        
    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])
    df = df.drop_duplicates()
    print(df)
    return df

# DataFrameを指定の期間でフィルタリング
def getSpanDf(_df, st, ed):
    _df = _df[(
                (_df['start'] >= st)
                & (df['start'] < ed)
                )|(
                (_df['end'] >= st)
                & (df['end'] < ed)
                )
             ]
    return _df

# 抜粋
def getCol(start, end):
    df = getEventsDf()
    df_span = getSpanDf(df, start, end)
    col = ['start','end','event']
    df_span[col]
    return df_span[col]
#--------------------------------------------------------------------
# 今日
def getTodayCal():
    # 今日
    dt = datetime.datetime.today()
    start = datetime.date(dt.year, dt.month, dt.day)
    end = start + datetime.timedelta(days=1)
    df = getCol(start, end)
    return df

# 今週いっぱいのイベント
def getThisWeekCal():
    # 今日
    dt = datetime.datetime.today()
    start = datetime.date(dt.year, dt.month, dt.day)
    end = start + datetime.timedelta(days=-start.weekday(), weeks=1)
    df = getCol(start, end)
    return df

# 来週いっぱいのイベント
def getNextWeekCal():
    # 今日
    dt = datetime.datetime.today()
    start = datetime.date(dt.year, dt.month, dt.day)
    end = start + datetime.timedelta(days=-start.weekday(), weeks=2)
    df = getCol(start, end)
    return df

# 今月いっぱいのイベント
def getThisMonthCal():
    # 今日
    dt = datetime.datetime.today()
    start = datetime.date(dt.year, dt.month, dt.day)
    end = start + relativedelta(day=1, months=1)
    df = getCol(start, end)
    return df

# 来月のイベント
def getNextMonthCal():
    # 今日
    dt = datetime.datetime.today()
    start = datetime.date(dt.year, dt.month, dt.day)
    #start = datetime.date(dt.year, dt.month, dt.day)
    start = start + relativedelta(day=1, months=1)
    end = start + relativedelta(day=1, months=2)
    df = getCol(start, end)
    return df

def getCalender(msg, msgcontent):
    flag = False
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')[1]
        if '今日' in datas:
            msg = '今日の幻影戦争イベントカレンダーだね！'
            df = getTodayCal()
        elif '今週' in datas:
            msg = '今週の幻影戦争イベントカレンダーだね！'
            df = getThisWeekCal()
        elif '来週' in datas:
            msg = '来週の幻影戦争イベントカレンダーだね！'
            df = getNextWeekCal()
        elif '今月' in datas:
            msg = '今月の幻影戦争イベントカレンダーだね！'
            df = getThisMonthCal()
        elif '来月' in datas:
            msg = '来月の幻影戦争イベントカレンダーだね！'
            df = getNextMonthCal()
        else:
            msg = 'そのコマンドは対応してないよ… 今日の幻影戦争イベントカレンダーを取得するね…'
            df = getNextMonthCal()
    else:
        msg = 'とりあえず今日の幻影戦争イベントカレンダーを取得するね！'
        df = getTodayCal()
        flag = True
    if flag:        
        msg += '!カレンダ 今日 の形でを打ってみて！幻影戦争のイベントカレンダを取得するよ！'
    return msg, df

def getCalLink(msg):
    msg = config['calender']['url']
    #    "https://calendar.google.com/calendar/u/0?cid=MzRsMzVwZGoxZmg4cDZkam10azZqZ2JyZTRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ"
    return msg