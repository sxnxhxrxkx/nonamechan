import requests
import json
import urllib
from logger import writelog
from logger import nonamelog
import configparser
config = configparser.ConfigParser()
config.read('noname.ini')

yahoo_KEY = config['yahoo']['clientid'] # xxxに自分のAPI Keyを入力。

def splitmsg(msgcontent):
    if ' ' in msgcontent:
        data = msgcontent.split(' ')[1]
    else:
        data = False
    return data

def nluservice(msg, msgcontent):
    msg += 'Yahooが提供する自然言語理解APIのテストだよ！'
    msgdata = splitmsg(msgcontent)
    if msgdata == False:
        msg += 'メッセージがないよ… !nlp テスト みたいな形でスペースを一つ入れて文章を投げてね'
    else:
        msg_quote = urllib.parse.quote(msgdata)
        api = "https://jlp.yahooapis.jp/NLUService/V1/analyze?appid={key}&intext={word}"
        url = api.format(key = yahoo_KEY, word = msg_quote )
        response = requests.get(url)
        data = response.json()
        msg += '解析の結果だよ！' + str(data) + '…参考になったかな？'
    return msg