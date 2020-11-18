#ClientID
#713695703931-96evkgsumethcakcjq8bmte1blrafv9m.apps.googleusercontent.com
#ClientSecret
#rrh1rtOBXMYXeQQBZtifayGP

from __future__ import print_function
import datetime
from dateutil.relativedelta import relativedelta
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
    # Calendarの取得
    print('connect & get calllender')
    events_result = service.events().list(calendarId=config['calender']['id'],
                                        timeMin=now,
                                        #maxResults=10, 
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
    #print(df)
    return df

# DataFrameを指定の期間でフィルタリング
# 一部期間内	s.end > e.start and s.end < e.end
# 期間内	s.start > e.start and s.end < e.end
# 一部期間内	s.start > e.start and s.start < e.end
# 期間内	e.start > s.start and e.end < s.end

def getSpanDf(df, start, end):
    st = start.strftime('%Y/%m/%d %H:%M:%S')
    ed = end.strftime('%Y/%m/%d %H:%M:%S')
    print(st, ed)

    df = df[
            ((ed > df['start']) & (ed < df['end']))|
            ((st > df['start']) & (ed < df['end']))|
            ((st > df['start']) & (st < df['end']))|
            ((df['start'] > st) & (df['end'] < ed))
             ]
    return df

# 抜粋
def getCol(start, end):
    df = getEventsDf()
    df_span = getSpanDf(df, start, end)
    #col = ['start','end','event']
    return df_span#[col]
#--------------------------------------------------------------------
# 今日
def getTodayCal():
    # 今日
    dt = datetime.datetime.today()
    start = datetime.date(dt.year, dt.month, dt.day)
    end = start + datetime.timedelta(days=1)
    #print(start, end)
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
    start = start + datetime.timedelta(days=-start.weekday(), weeks=1)
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
    start = start + relativedelta(day=1, months=1)
    end = start + relativedelta(day=1, months=2)
    df = getCol(start, end)
    return df

# 今後のイベント
def getNextCal():
    # 今日
    dt = datetime.datetime.today()
    start = datetime.date(dt.year, dt.month, dt.day)
    end = start + relativedelta(day=1, months=12)
    df = getCol(start, end)
    return df

# 過去のイベント
def getPrevCal():
    # 今日
    dt = datetime.datetime.today()
    end = datetime.date(dt.year, dt.month, dt.day)
    start = end - relativedelta(day=1, months=12)
    df = getCol(start, end)
    return df

# カレンダー
def getCalender(msg, msgcontent):
    calenderName = config['calender']['name']
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')
        if '今日' in datas:
            msg = '今日の' + calenderName + 'のイベントカレンダーだね！'
            df = getTodayCal()
        elif '今週' in datas:
            msg = '今週の' + calenderName + 'のイベントカレンダーだね！'
            df = getThisWeekCal()
        elif '来週' in datas:
            msg = '来週の' + calenderName + 'のイベントカレンダーだね！'
            df = getNextWeekCal()
        elif '今月' in datas:
            msg = '今月の' + calenderName + 'のイベントカレンダーだね！'
            df = getThisMonthCal()
        elif '来月' in datas:
            msg = '来月の' + calenderName + 'のイベントカレンダーだね！'
            df = getNextMonthCal()
        elif '今後' in datas:
            msg = '今後の' + calenderName + 'のイベントカレンダーだね！'
            df = getNextCal()
        elif '過去' in datas:
            msg = '過去の' + calenderName + 'のイベントカレンダーだね！'
            df = getPrevCal()
        else:
            msg = 'とりあえず今日の' + calenderName + 'のイベントカレンダーを取得するね…'
            df = getTodayCal()
            msg += '【' + datas[1] + '】でフィルタリングするよ！'
            #df = df[df['category'] == datas[1]]
            df = df[df['category'].str.contains(datas[1])]

        if len(datas) > 2:
            msg += '【' + datas[2] + '】でフィルタリングするよ！'
            #df = df[df['category'] == datas[2]]
            #df = df[df['category'].str.contains(datas[2])]
            df = df[(df['category'].str.contains(datas[2]))|(df['event'].str.contains(datas[2]))]
    else:
        msg = 'とりあえず今日の' + calenderName + 'のイベントカレンダーを取得するね！'
        df = getTodayCal()
    return msg, df

def getCalLink(msg):
    msg = config['calender']['url']
    #    "https://calendar.google.com/calendar/u/0?cid=MzRsMzVwZGoxZmg4cDZkam10azZqZ2JyZTRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ"
    return msg

def getCommandList(msg):
    msg = '!カレンダ 今日(or 今週/来週/今月/来月/今後/過去) キーワード に対応しているよ。'
    msg += 'カレンダの編集元が見たい場合は !カレンダリンク で打ってみてね！'
    return msg