# coding:utf-8
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import MeCab as mc
import numpy as np
from PIL import Image
import os

def mecab_analysis(text):
    print('mecab_analysis_start')
    t = mc.Tagger ("-Ochasen") # + r"C:\Program Files (x86)\MeCab\dic\ipadic\user.dic")
    t.parse('')
    node = t.parseToNode(text) 
    output = []
    while(node):
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞", "動詞","名詞", "副詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    print('mecab_analysis_end',len(output))
    return output
    
def get_wordlist(url):
    print('get_wordlist_start')
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    text = soup.find('body').get_text().replace('\n','').replace('\t','')
    print('get_wordlist_end', len(text))
    return mecab_analysis(text)
    
def create_wordcloud(text):
    # 環境に合わせてフォントのパスを指定する。
    fpath = "C:\\WINDOWS\\FONTS\\YUGOTHB.TTC"

    # ストップワードの設定
    stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']
    
    #alice_mask = np.array(Image.open("noname_mask.png"))
    #wordcloud = WordCloud(background_color="black",font_path=fpath,stopwords=set(stop_words),  max_words=1000, mask=alice_mask).generate(text)
    wordcloud = WordCloud(background_color="black",font_path=fpath,stopwords=set(stop_words),  max_words=1000).generate(text)
    return wordcloud

def get_wordcloud(url):
    wordlist = get_wordlist(url)
    wordcloud = create_wordcloud(" ".join(wordlist))
    img = np.array(wordcloud)
    pil_im = Image.fromarray(img)
    pil_im.save("temp.png")
    return

def noname_wc(msg, msgcontent):
    flag = False
    if ' ' in msgcontent:
        url = msgcontent.split(' ')[1]
        print(url)
        msg +=  "url をスクレイピングしてword cloudを出力するよ！"
        try:
            get_wordcloud(url)
        except:
            msg += "変換できないよ？スクレイピングしたいurlを入れてね！"
    else:
        flag = True
    if flag:        
        msg += '!wc url の形でスクレイピングしたいurlを打ってみて！word cloudを作成するよ！'
    return msg