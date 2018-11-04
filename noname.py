# Work with Python 3.6
import discord
import numpy as np
import pandas as pd
import random
import subprocess
import weather as wt
from nlu_yahoo import nluservice
from MorseCode import morse
#import softalk as sf
import noname_vocabulary as nnm
import traceback
from logger import writelog
from logger import nonamelog
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
        if message.content.startswith('のなめ') or message.content.startswith('noname'):
            msg += nnm.noname(msg)
            nonamelog(getUser(message),'noname', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!さしすせそ') or message.content.startswith('さしすせそ'): 
            msg += nnm.sasisuseso(msg)
            nonamelog(getUser(message),'sasisuseso', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!ほめて') or message.content.startswith('ほめて') or message.content.startswith('褒めて') : 
            msg += nnm.homete(msg)
            nonamelog(getUser(message),'homete', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!罵倒して') or message.content.startswith('ばとうして') or message.content.startswith('罵倒して') : 
            msg += nnm.batou(msg)
            nonamelog(getUser(message),'batou', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!疲れた') or message.content.startswith('疲れた') or  message.content.startswith('つかれた'): 
            msg += nnm.tsukareta(msg)
            nonamelog(getUser(message),'tsukareta', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('頑張った') or message.content.startswith('がんばった'):
            msg += nnm.ganbatta(msg)
            nonamelog(getUser(message),'ganbatta', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!応援') or message.content.startswith('応援'):
            msg += nnm.ouen(msg)
            nonamelog(getUser(message),'ouen', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!励まして') or message.content.startswith('励まして') or message.content.startswith('!はげまして') or message.content.startswith('はげまして'):
            msg += nnm.hagemasu(msg)
            nonamelog(getUser(message),'hagemasu', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('頑張る') or message.content.startswith('がんばる') or message.content.startswith('がんがる') or message.content.startswith('ガンガル'):
            msg += nnm.ganbaru(msg)
            nonamelog(getUser(message),'ganbaru', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!はじめまして') or message.content.startswith('hello'):
            msg += 'はじめまして！ {0.author.mention}'.format(message) + 'さん！'
            msg += nnm.information(msg)
            msg += '楽しんでいってくださいね！'
            nonamelog(getUser(message),'information', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!help') or message.content.startswith('!ヘルプ'):
            msg += nnm.nonamehelp(msg)
            nonamelog(getUser(message),'nonamehelp', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!hello') or message.content.startswith('hello'):
            msg += 'Hello {0.author.mention}'.format(message)
            nonamelog(getUser(message),'hello', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!こんにちわ') or message.content.startswith('こんにちわ'):
            msg += 'こんにちわ！ {0.author.mention}'.format(message) + 'さん！'
            nonamelog(getUser(message),'hello', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!おは') or message.content.startswith('おは'):
            msg += nnm.ohayo(msg)
            nonamelog(getUser(message),'ohayo', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!おやす') or message.content.startswith('おやす'):
            msg += nnm.oyasumi(msg)
            nonamelog(getUser(message),'oyasumi', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!ありがと'):
            msg += nnm.arigato(msg)
            nonamelog(getUser(message),'arigato', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('おつ') or message.content.startswith('お疲れ') or message.content.startswith('!おつ'):
            msg += nnm.otsu(msg)
            nonamelog(getUser(message),'otsu', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!ぬるぽ') or message.content.startswith('ぬるぽ'):
            msg += nnm.nurupo(msg)
            nonamelog(getUser(message),'nurupo', message.content)
            await client.send_message(message.channel, msg)
        
        if message.content.startswith('!しりとり'):
            msg += 'しりとり、ですか？現在、その機能は使われておりません。ピピー！'
            await client.send_message(message.channel, msg)

        if message.content.startswith('!占い') or message.content.startswith('!運勢'):
            msg = 'じゃじゃーーん！！今日の運勢！ですね！'
            await client.send_message(message.channel, msg)
            msg, negaposi = nnm.uranai(msg)
            await client.send_message(message.channel, msg)
            msg = nnm.luckynum(msg, negaposi)
            await client.send_message(message.channel, msg)
            msg = nnm.luckycolor(msg, negaposi)
            await client.send_message(message.channel, msg)
            msg = nnm.advice(msg, negaposi)
            nonamelog(getUser(message),'uranai', message.content)
            await client.send_message(message.channel, msg)
        
        if message.content.startswith('!ニンジャ') or message.content.startswith('ニンジャ'):
            msg = nnm.ninja(msg,getUser(message))
            nonamelog(getUser(message),'ninja', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('ふぃんだー') or message.content.startswith('フィンダー'):
            msg = nnm.finder(msg,getUser(message))
            nonamelog(getUser(message),'finder', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!dice') or message.content.startswith('!サイコロ') or message.content.startswith('!ダイス'):
            if message.content.startswith('!dicegame') or message.content.startswith('!サイコロ勝負') or message.content.startswith('!ダイス勝負'):
                msg = nnm.dicegame(msg, message.content)
                nonamelog(getUser(message),'dicegame', message.content)
            else:
                msg = nnm.somedice(msg, message.content)
                nonamelog(getUser(message),'somedice', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!天気'):
            msg += wt.weather()
            nonamelog(getUser(message),'weather', message.content)
            await client.send_message(message.channel, msg)
        
        if message.content.startswith('!モールス') or message.content.startswith('!もーるす'):
            msg += morse(msg, message.content)
            nonamelog(getUser(message),'morse', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!nlu'):
            msg += nluservice(msg, message.content)
            nonamelog(getUser(message),'nluservice', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!dec2bin'):
            msg += nnm.dec2bin(msg, message.content)
            nonamelog(getUser(message),'dec2bin', message.content)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!dec2hex'):
            msg += nnm.dec2hex(msg, message.content)
            nonamelog(getUser(message),'dec2hex', message.content)
            await client.send_message(message.channel, msg)  

        if message.content.startswith('!bin2dec'):
            msg += nnm.bin2dec(msg, message.content)
            nonamelog(getUser(message),'bin2dec', message.content)
            await client.send_message(message.channel, msg)  

        if message.content.startswith('!hex2dec'):
            msg += nnm.hex2dec(msg, message.content)
            nonamelog(getUser(message),'hex2dec', message.content)
            await client.send_message(message.channel, msg)
        
        # add -------
        if message.content.startswith('$thumb'):
            msg = await client.send_message(message.channel, 'React with thumbs up or thumbs down.')

            def check(reaction, user):
                e = str(reaction.emoji)
                return e.startswith(('👍', '👎'))

            res = await client.wait_for_reaction(message=msg, check=check)
            await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))

        if message.content.startswith('$start'):
            await client.send_message(message.channel, 'Type $stop 4 times.')
            for i in range(4):
                msg = await client.wait_for_message(author=message.author, content='$stop')
                fmt = '{} left to go...'
                await client.send_message(message.channel, fmt.format(3 - i))

            await client.send_message(message.channel, 'Good job!')

        if message.content.startswith('$cool'):
            await client.send_message(message.channel, 'Who is cool? Type $name namehere')

            def check2(msg):
                return msg.content.startswith('$name')

            message = await client.wait_for_message(author=message.author, check=check2)
            name = message.content[len('$name'):].strip()
            await client.send_message(message.channel, '{} is cool indeed'.format(name))

        if message.content.startswith('$test'):
            await client.send_message(message.channel, 'ttstest.', tts=True)

        if message.content.startswith('exit'):
            await client.logout()

    except:
        msg += 'エラー。んん、、なんかおかしいかも。。logを出すね。。'
        nonamelog(getUser(message),'error', message.content)
        await client.send_message(message.channel, msg)
        msg = traceback.format_exc()
        await client.send_message(message.channel, msg)
    
    #sf.talk(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)