import requests
import json
from logger import writelog
from logger import nonamelog
import configparser
config = configparser.ConfigParser()
config.read('noname.ini')

city_name = "osaka" # 主要な都市名はいけるっぽい。
API_KEY = config['weather']['APIKEY'] # xxxに自分のAPI Keyを入力。
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

def weather():
    url = api.format(city = city_name, key = API_KEY)
    response = requests.get(url)
    data = response.json()
    humid = data['main']['humidity']
    pressure = data['main']['pressure']
    temp_max = data['main']['temp_max']
    temp_min = data['main']['temp_min']
    weather = data['weather'][0]['description']
    if weather == 'rain':
        answether = '雨'
    elif weather == 'shower rain':
        answether = 'ちょびっと雨かも'
    elif weather == 'clouds':
        answether = 'くもり'
    elif weather == 'broken clouds':
        answether = 'すっごいくもり'
    elif weather == 'sunny':
        answether = 'たぶんはれ'
    else:
        answether = str(weather)

    print(weather)

    msg = "今日の大阪の天気は、、、"
    msg += str(answether) + "！"
    msg += "最高気温、" + str(temp_max) + "℃！"
    msg += "最低気温、" + str(temp_min)+ "℃！"
    msg += "湿度、" + str(humid)+ "%！"
    msg += "気圧、" + str(pressure)+ "Pa！"
    msg += "だよ！！"
    # 気温 ----------------
    if temp_max > 30:
        msg += "とっても暑いよ！ヤダー！"
    elif temp_max > 25:
        msg += "ちょっと暑いかも？！"
    elif temp_max > 20:
        msg += "すごしやすい温度だよ！"
    elif temp_max > 10:
        msg += "ちょっと肌寒いよ！"
    elif temp_max > 0:
        msg += "とっても寒いよ！布団で寝よう！"
    else:
        msg += "もはや人間は生きられないよ…"
    # 天気 ----------------
    if  (weather == 'rain') or (weather == 'shower rain'):
        msg += "傘を持ってでかけてね！"
    elif weather == 'cloud':
        msg += "雨降らないといいなぁ"
    return msg