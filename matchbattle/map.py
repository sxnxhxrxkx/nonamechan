# Work with Python 3.6
import discord
import numpy as np
import pandas as pd
import random
import subprocess
import traceback
import configparser
config = configparser.ConfigParser()
# config.read('noname.ini')
# TOKEN = config['noname']['TOKEN']

#path = "https://github.com/sxnxhxrxkx/nonamechan/tree/master/matchbattle/maps"
path = "https://raw.githubusercontent.com/sxnxhxrxkx/nonamechan/master/matchbattle/maps"

# 幻影戦争のマッチバトルのマップリストを取得する
def getMapList():
    maps = pd.read_csv('matchbattle/map_list.csv', encoding="shift-jis")
    maps['filepath'] = path + "/" + maps['filename'] 
    return maps

# 幻影戦争幻影戦争のマッチバトルのマップリストを取得する
def getTargetMap():
    maps =getMapList()
    map_counts = len(maps)
    dice = random.randrange(map_counts)
    target_map_name = maps['map'][dice]
    target_map_path = maps['filepath'][dice]
    return target_map_name, target_map_path

def getMap():
    map_name, map_path = getTargetMap()
