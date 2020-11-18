# Work with Python 3.6
import discord
import numpy as np
import pandas as pd
import random
import subprocess
import weather as wt
from nlu_yahoo import nluservice
from MorseCode import morse
# from wc import noname_wc
#import softalk as sf
from calender import getCalender, getCalLink, getCommandList
from news import getNews
import noname_vocabulary as nnm
import traceback
from logger import writelog
from logger import nonamelog
from bs4 import BeautifulSoup
import requests

import configparser
config = configparser.ConfigParser()
config.read('noname.ini')
TOKEN = config['noname']['TOKEN']

client = discord.Client()

def getUser(message):
    usrname = str(message.author)
    return usrname

@client.event
async def on_message(message):
    msg = ''
    if message.author == client.user:
        return

    try:
        if message.content.__contains__('さしすせそ'): 
            msg = nnm.sasisuseso(msg)
            nonamelog(getUser(message),'sasisuseso', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('世界一かわいい'): 
            msg = nnm.okoku(msg)
            nonamelog(getUser(message),'okoku', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('ほめて') or message.content.__contains__('褒めて') : 
            msg += nnm.homete(msg)
            nonamelog(getUser(message),'homete', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('ばとうして') or message.content.__contains__('罵倒して') or message.content.__contains__('おしっこ') or message.content.__contains__('!ちんちん'): 
            msg += nnm.batou(msg)
            nonamelog(getUser(message),'batou', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('疲れた') or  message.content.__contains__('つかれた'): 
            msg += nnm.tsukareta(msg)
            nonamelog(getUser(message),'tsukareta', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('許して') or message.content.__contains__('ゆるして') or message.content.__contains__('許されたい'):
            msg += nnm.yurusite(msg)
            nonamelog(getUser(message),'yurusite', message.content)
            await message.channel.send( msg)

        if message.content.__contains__('頑張った') or message.content.__contains__('がんばった'):
            msg += nnm.ganbatta(msg)
            nonamelog(getUser(message),'ganbatta', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('応援'):
            msg += nnm.ouen(msg)
            nonamelog(getUser(message),'ouen', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('励まして') or message.content.__contains__('はげまして'):
            msg += nnm.hagemasu(msg)
            nonamelog(getUser(message),'hagemasu', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('頑張る') or message.content.__contains__('がんばる') or message.content.__contains__('がんがる') or message.content.__contains__('ガンガル'):
            msg += nnm.ganbaru(msg)
            nonamelog(getUser(message),'ganbaru', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('はじめまして'):
            msg += 'はじめまして！ {0.author.mention}'.format(message) + 'さん！'
            msg += nnm.information(msg)
            msg += '楽しんでいってくださいね！'
            nonamelog(getUser(message),'information', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('!help') or message.content.__contains__('!ヘルプ'):
            msg += nnm.nonamehelp(msg)
            nonamelog(getUser(message),'nonamehelp', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('hello'):
            msg += 'Hello {0.author.mention}'.format(message)
            nonamelog(getUser(message),'hello', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('こんにちわ'):
            msg += 'こんにちわ！ {0.author.mention}'.format(message) + 'さん！'
            nonamelog(getUser(message),'hello', message.content)
            await message.channel.send( msg)
            return

        if message.content.startswith('おはよ'):
            msg += nnm.ohayo(msg)
            nonamelog(getUser(message),'ohayo', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('おやす'):
            msg += nnm.oyasumi(msg)
            nonamelog(getUser(message),'oyasumi', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('!ありがと'):
            msg += nnm.arigato(msg)
            nonamelog(getUser(message),'arigato', message.content)
            await message.channel.send( msg)
            return

        if message.content.__contains__('おつ') or message.content.__contains__('お疲れ') or message.content.__contains__('!おつ'):
            msg += nnm.otsu(msg)
            nonamelog(getUser(message),'otsu', message.content)
            await message.channel.send( msg)

        if message.content.__contains__('!ぬるぽ') or message.content.__contains__('ぬるぽ'):
            msg += nnm.nurupo(msg)
            nonamelog(getUser(message),'nurupo', message.content)
            await message.channel.send( msg)
        
        if message.content.__contains__('!しりとり'):
            msg += 'しりとり、ですか？現在、その機能は使われておりません。ピピー！'
            await message.channel.send( msg)

        if message.content.__contains__('!占い') or message.content.__contains__('!運勢'):
            msg = 'じゃじゃーーん！！今日の運勢！ですね！'
            await message.channel.send( msg)
            msg, negaposi = nnm.uranai(msg)
            await message.channel.send( msg)
            msg = nnm.luckynum(msg, negaposi)
            await message.channel.send( msg)
            msg = nnm.luckycolor(msg, negaposi)
            await message.channel.send( msg)
            msg = nnm.advice(msg, negaposi)
            nonamelog(getUser(message),'uranai', message.content)
            await message.channel.send( msg)
        
        if message.content.__contains__('!ニンジャ') or message.content.__contains__('ニンジャ'):
            msg = nnm.ninja(msg,getUser(message))
            nonamelog(getUser(message),'ninja', message.content)
            await message.channel.send( msg)

        if message.content.startswith('ふぃんだー') or message.content.startswith('フィンダー'):
            msg = nnm.finder(msg,getUser(message))
            nonamelog(getUser(message),'finder', message.content)
            await message.channel.send( msg)

        if message.content.startswith('!dice') or message.content.startswith('!サイコロ') or message.content.startswith('!ダイス'):
            if message.content.startswith('!dicegame') or message.content.startswith('!サイコロ勝負') or message.content.startswith('!ダイス勝負'):
                msg = nnm.dicegame(msg, message.content)
                nonamelog(getUser(message),'dicegame', message.content)
            else:
                msg = nnm.somedice(msg, message.content)
                nonamelog(getUser(message),'somedice', message.content)
            await message.channel.send( msg)

        # if message.content.startswith('!ちんちろ') or message.content.startswith('!チンチロ'):
        #     msg = "ちんちろりんだね！サイコロを振るよ！"
        #     await message.channel.send( msg)
        #     msg, score, yaku, result_str, negaposi = nnm.tintiro(msg, message.content)
        #     nonamelog(getUser(message),'tintiro', message.content)
        #     await message.channel.send( msg)
        #     return

        if message.content.startswith('!ちんちろ') or message.content.startswith('!チンチロ'):
            msg = "ちんちろりんだね！役が出るまで3回サイコロを振るよ！"
            await message.channel.send( msg)
            cnt = 1
            msg = "１投目を振るよ！"
            await message.channel.send( msg)
            msg, score, yaku, result_str, reaction = nnm.tintiro(msg, message.content)
            await message.channel.send( msg)
            if yaku == "目なし":
                msg = "２投目を振るよ！"
                await message.channel.send( msg)
                msg, score, yaku, result_str, reaction = nnm.tintiro(msg, message.content)
                await message.channel.send( msg)
                cnt += 1 
            if yaku == "目なし":
                msg = "これが最後のチャンスだよ！"
                await message.channel.send( msg)
                msg, score, yaku, result_str, reaction = nnm.tintiro(msg, message.content)
                await message.channel.send( msg)
                cnt += 1 
            if yaku == "目なし":
                msg = '最後まで目なし…あまくないね！あなたの負けだよ！'
                await message.channel.send( msg)
            elif score >= 1:
                msg = '役を出すことができて何よりだよ！'
                await message.channel.send( msg)
            # msg += 'はじめまして！ {0.author.mention}'.format(message) + 'さん！'

            msg = '結果をまとめるね！'
            await message.channel.send( msg)
            # msg = '-------------------------------'
            # await message.channel.send( msg)
            # msg = 'あなたの結果'
            # await message.channel.send( msg)
            # msg = '回数　：' + str(cnt) + '投'
            # await message.channel.send( msg)
            # msg = '役　　：' + yaku
            # await message.channel.send( msg)
            # msg = 'スコア：' + str(score)
            # await message.channel.send( msg)
            # msg = '-------------------------------'
            # await message.channel.send( msg)

            # ヘッダ
            embed = discord.Embed(title="---ちんちろりん結果---", description='プレイヤ：{0.author.mention}'.format(message))
            embed.add_field(name="投数", value=str(cnt) + '投')
            embed.add_field(name="役", value=yaku)
            embed.add_field(name="スコア", value=str(score))
            await message.channel.send(embed=embed)

            msg = 'また遊んでね！'
            await message.channel.send( msg)
            nonamelog(getUser(message),'tintiro', message.content)
            return


        if message.content.startswith('!天気'):
            #msg += wt.weather()
            msg += wt.weather_geo(msg, message.content)
            nonamelog(getUser(message),'weather', message.content)
            await message.channel.send( msg)
        
        if message.content.startswith('!モールス') or message.content.startswith('!もーるす'):
            msg += morse(msg, message.content)
            nonamelog(getUser(message),'morse', message.content)
            await message.channel.send( msg)

        if message.content.startswith('!nlu'):
            msg += nluservice(msg, message.content)
            nonamelog(getUser(message),'nluservice', message.content)
            await message.channel.send( msg)

        if message.content.startswith('!dec2bin'):
            msg += nnm.dec2bin(msg, message.content)
            nonamelog(getUser(message),'dec2bin', message.content)
            await message.channel.send( msg)

        if message.content.startswith('!dec2hex'):
            msg += nnm.dec2hex(msg, message.content)
            nonamelog(getUser(message),'dec2hex', message.content)
            await message.channel.send( msg)  

        if message.content.startswith('!bin2dec'):
            msg += nnm.bin2dec(msg, message.content)
            nonamelog(getUser(message),'bin2dec', message.content)
            await message.channel.send( msg)  

        if message.content.startswith('!hex2dec'):
            msg += nnm.hex2dec(msg, message.content)
            nonamelog(getUser(message),'hex2dec', message.content)
            await message.channel.send( msg)

        if message.content.startswith('!半濁音'):
            msg += nnm.handakuon(msg, message.content)
            nonamelog(getUser(message),'handakuon', message.content)
            await message.channel.send( msg)

        if message.content.startswith('!濁音'):
            msg += nnm.dakuon(msg, message.content)
            nonamelog(getUser(message),'dakuon', message.content)
            await message.channel.send( msg)

        if message.content.startswith('!リピート'):
            msg += nnm.repeat(msg, message.content)
            nonamelog(getUser(message),'repeat', message.content)
            await message.channel.send( msg)

        # if message.content.startswith('!カレンダ'):
        #     msg = "幻影戦争のイベントカレンダーリンクだね！"
        #     await message.channel.send( msg)
        #     msg = nnm.ffbeCal(msg)#, message.content)
        #     await message.channel.send( msg)
        #     msg = "今はやっつけだからリンクだけだよ！参考になったかな？"
        #     nonamelog(getUser(message),'cal', message.content)
        #     await message.channel.send( msg)

        if message.content.startswith('!カレンダリンク'):
            nonamelog(getUser(message),'cal', message.content)
            msg = "幻影戦争のイベントカレンダーは以下のリンクだよ！"
            await message.channel.send( msg)
            msg = getCalLink(msg)
            await message.channel.send( msg)
            msg = "編集したい場合はここを見てね。参考になったかな？"
            await message.channel.send( msg)
            return

        if message.content.startswith('!カレンダ'):
            nonamelog(getUser(message),'cal', message.content)
            msg, df = getCalender( msg, message.content)
            await message.channel.send( msg)
            msg = "--------------------------------------"
            await message.channel.send( msg)
            for index, row in df.iterrows():
                msg = row['start'].strftime('%m/%d %H') + "' - " + row['end'].strftime('%m/%d %H') + "'" + " " + row['category'] + " " +  row['event']
                #msg = row['start'].strftime('%m/%d.%H') + "-" + row['end'].strftime('%m/%d.%H') + " " + row['category'] + " " +  row['event']
                await message.channel.send( msg)
            msg = "--------------------------------------"
            await message.channel.send( msg)
            msg = getCommandList(msg)
            await message.channel.send( msg)
            return

        # 幻影戦争お知らせの取得
        if message.content.startswith('!お知らせ'):
            nonamelog(getUser(message),'news', message.content)

            url_org = "https://players.wotvffbe.com"
            url = url_org + "/all/"
            msg = "幻影戦争のお知らせを取得するよ！"
            await message.channel.send( msg)

            msg, df = getNews(msg, message.content)
            await message.channel.send( msg)

            # ヘッダ
            embed = discord.Embed(title="FFBE 幻影戦争 お知らせ", description=f"FFBE 幻影戦争 のお知らせのURLは [こちら]({url}) です！")

            for index, row in df.iterrows():
                time = row['time']
                content = row['content']
                link = row['link']
                embed.add_field(name=time, value="[" + content +"](" + link + ")",inline=False)

            await message.channel.send(embed=embed)
            return

        # if message.content.startswith('!wc'):
        #     msg += noname_wc(msg, message.content)
        #     nonamelog(getUser(message),'wc', message.content)
        #     await client.send_file(message.channel, "temp.png", content="スクレイピングしたよ!", filename="send.png")

        # add -------
        if message.content.__contains__('のなめ') or message.content.__contains__('noname'):
            msg = nnm.noname(msg)
            nonamelog(getUser(message),'noname', message.content)
            await message.channel.send( msg)

        if message.content.startswith('exit'):
            await client.logout()

    except:
        msg += 'エラー。んん、、なんかおかしいかも。。logを出すね。。'
        nonamelog(getUser(message),'error', message.content)
        await message.channel.send( msg)
        msg = traceback.format_exc()
        await message.channel.send( msg)
    
    #sf.talk(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)