import random
import subprocess
import weather as wt

def information(msg):
    msg += 'わたしは未来技術同好会、試作bot一号の、のなめです！'
    msg += '未来技術同好会の各Discordチャンネルについてご紹介します。'
    msg += '左にナビゲーションバーがありますね？'
    msg += '見ての通りです。'
    msg += 'とりあえずどこでもいいから書けばいいと思いますよ。'
    msg += 'えっと、私からは以上です！'
    return msg

def nonamehelp(msg):
    msg += 'のなめの機能についてご紹介します。'
    msg += '現在のなめには、挨拶、占い、サイコロ、天気予報 機能が実装されています。'
    msg += '!をつけて !占い 、!サイコロ 、!天気 とかつぶやいてみてください。'
    msg += 'のなめは大阪生まれなので、大阪の天気しかわかりません。'
    msg += '後は今後のアップデートに期待、です。'
    return msg

def sasisuseso(msg):
    dice = random.randrange(5)
    if dice == 1:
        msg += 'さすがですね！'
    elif dice == 2:
        msg += '知らなかった。。。'
    elif dice == 3:
        msg += 'すっごーい☆'
    elif dice == 4:
        msg += 'センスいい！'
    elif dice == 5:
        msg += 'そうなんだ？！'
    return msg

def otsu(msg):
    dice = random.randrange(5)
    if dice == 1:
        msg += 'おつですー'
    elif dice == 2:
        msg += 'おつかれさまです☆'
    elif dice == 3:
        msg += 'おつおつー'
    elif dice == 4:
        msg += '乙！'
    elif dice == 5:
        msg += 'おつんでれ'
    return msg

def ohayo(msg):
    dice = random.randrange(11)
    if dice == 1:
        msg += 'オハヨォ☆'
    elif dice == 2:
        msg += 'むくり'
    elif dice == 3:
        msg += '未来技術同好会、試作ロボット一号、のなめ、起動ーーー！'
    elif dice == 4:
        msg += 'ブーーーーン。システム、オールグリーン。のなめ、起動します！'
    elif dice == 5:
        msg += 'おはよ！のなめだよ！'
    elif dice == 6:
        msg += 'おはよ！まだ眠いね。。。'
    elif dice == 7:
        msg += 'おはよおはよ！おはよーーーー！'
    elif dice == 8:
        msg += '朝だよ！起きて！'
    elif dice == 9:
        msg += 'おはよ～！天気予報が必要な場合は"!天気"ってつぶやいてね。'
    elif dice == 10:
        msg += 'おはよう。今日も一日頑張るぞいっ！だね！'
    else:
        msg += 'おはよ！今日も元気！だね！'
    return msg

def oyasumi(msg):
    dice = random.randrange(9)
    if dice == 1:
        msg += 'おやすみです。'
    elif dice == 2:
        msg += '(˘ω˘)ｽﾔｧ'
    elif dice == 3:
        msg += 'おやすみなさーーい☆'
    elif dice == 4:
        msg += 'システム、シャットダウン。のなめ、起動します！'
    elif dice == 5:
        msg += 'ハッ！寝てた？！'
    elif dice == 6:
        msg += 'ねむねむ。。。おやすみなさぁい。。。'
    elif dice == 7:
        msg += '大丈夫。。私が寝ても代わりがいるもの。。おやすみなさい。。zzZ'
    elif dice == 8:
        msg += 'おやすみ！ゆっくり寝てね？'
    else:
        msg += 'zzZZ'
    return msg

def arigato(msg):
    dice = random.randrange(9)
    if dice == 1:
        msg += 'どういたしまして☆だよ！'
    elif dice == 2:
        msg += '褒めてくれてもいいんだよ？'
    elif dice == 3:
        msg += 'て、照れます！'
    elif dice == 4:
        msg += 'どういたしまして'
    elif dice == 5:
        msg += 'こちらこそ、いつもありがとうね？'
    elif dice == 6:
        msg += 'いえいえ、それほどでも？！なんて。。'
    elif dice == 7:
        msg += 'ありがとナス！'
    elif dice == 8:
        msg += 'のなめも、ありがとう。'
    else:
        msg += '照れるね・・・どういたしまして。'
    return msg        


def noname(msg):
    dice = random.randrange(10)
    if dice == 1:
        msg += 'よんだ？'
    elif dice == 2:
        msg += 'なあに？'
    elif dice == 3:
        msg += 'はぁい☆'
    elif dice == 4:
        msg += 'のなめだよ！'
    elif dice == 5:
        msg += 'どうかした？'
    elif dice == 6:
        msg += 'どしたの？'
    elif dice == 7:
        msg += 'ん～～～～？なあに？'
    elif dice == 8:
        msg += 'ちょっ・・・今はだめ！！'
    elif dice == 9:
        msg += 'そうです！わたしが！のなめ！・・・です！'
    elif dice == 10:
        msg += 'はいはい。。のなめですよ～～。'
    return msg

def homete(msg):
    dice = random.randrange(8)
    if dice == 1:
        msg += 'すごいすごい！！'
    elif dice == 2:
        msg += 'かっこいいよ！'
    elif dice == 3:
        msg += sasisuseso(msg)
    elif dice == 4:
        msg += 'えらーいえらい！'
    elif dice == 5:
        msg += 'いつも頑張っててほんとえらい！'
    elif dice == 6:
        msg += 'ほんっとーに！よく頑張ったね！'
    elif dice == 7:
        msg += 'いつもお疲れ様！今日も頑張ったね？'
    elif dice == 8:
        msg += '私はいつも、見てますよ？'
    return msg

def tsukareta(msg):
    dice = random.randrange(7)
    if dice == 1:
        msg += 'いつもお疲れ様！無理せず、ゆっくり休んでね？'
    elif dice == 2:
        msg += 'わたしも疲れたーーーー！ちょっと休んじゃお！？'   
    elif dice == 3:
        msg += 'びろーーーーーーーーん。'   
    elif dice == 4:
        msg += 'ぐでーーーーーーーーん。'
    elif dice == 5:
        msg += 'よしよし・・・、ゆっくり休んでね？'
    elif dice == 6:
        msg += 'まぢ無理だよね・・・'
    elif dice == 7:
        msg += 'よしよし、頑張ったね？'
    return msg

def ganbatta(msg):
    dice = random.randrange(6)
    if dice == 1:
        msg += 'お疲れ様！'
    elif dice == 2:
        msg += 'すごい頑張ったね！！さすが！だよ！'  
    elif dice == 3:
        msg += '今日も頑張ってえらい！すごい！かっこいい！'
    elif dice == 4:
        msg += 'やるやつ！だね！'
    elif dice == 5:
        msg += 'お疲れ様！お茶ドゾー つ旦'
    else:
        msg += 'お疲れ様！今日も頑張ったし、自分にご褒美あげちゃお！'
    return msg

def nemui(msg):
    dice = random.randrange(11)
    if dice == 1:
        msg += 'おやすみです。'
    elif dice == 2:
        msg += '(˘ω˘)ｽﾔｧ'
    elif dice == 3:
        msg += 'おやすみなさーーい☆'
    elif dice == 4:
        msg += 'システム、シャットダウン。のなめ、起動します！'
    elif dice == 5:
        msg += 'ハッ！寝てた？！'
    elif dice == 6:
        msg += 'ねむねむ。。。おやすみなさぁい。。。'
    elif dice == 7:
        msg += '大丈夫。。眠いが寝ても代わりがいるもの。。おやすみなさい。。zzZ'
    elif dice == 8:
        msg += 'おやすみ！ゆっくり寝てね？'
    elif dice == 9:
        msg += 'おはよ～！天気予報が必要な場合は"!天気"ってつぶやいてね。'
    elif dice == 10:
        msg += 'おはよう。今日も一日頑張るぞいっ！だね！'
    else:
        msg += 'おはよ！今日も元気！だね！'
    return msg

def ouen(msg):
    dice = random.randrange(9)
    if dice == 1:
        msg += 'がんばれ♡がんばれ♡'
    elif dice == 2:
        msg += 'がんばれ☆がんばれ☆'
    elif dice == 3:
        msg += 'がんばぇ～☆'       
    elif dice == 4:
        msg += 'がんばって？'    
    elif dice == 5:
        msg += 'フレっフレー！頑張れー！'
    elif dice == 6:
        msg += 'のなめは応援してますよ？大丈夫。できます！'
    elif dice == 7:
        msg += 'ガンバです！！！'
    elif dice == 8:
        msg += '大丈夫、大丈夫。あなたならやれますよ。'
    elif dice == 9:
        msg += 'できます！やるだけです！'
    return msg

def hagemasu(msg):
    dice = random.randrange(9)
    if dice == 1:
        msg += '落ち込まないで、きっと誰かが見ていてくれるよ'
    elif dice == 2:
        msg += '頑張っているの、のなめは知っているよ！'
    elif dice == 3:
        msg += '君はいつも頑張り屋さんだからな～'       
    elif dice == 4:
        msg += '大丈夫、努力はウソをつかないよ！'    
    elif dice == 5:
        msg += '話聞くくらいしかできないけど、何でも言ってね！'
    elif dice == 6:
        msg += 'のなめは応援してますよ？大丈夫。できます！'
    elif dice == 7:
        msg += 'You can do it! キミはできる人だよ！'
    elif dice == 8:
        msg += 'ゆっくり息を吐いて。大丈夫、大丈夫。あなたならやれますよ。'
    elif dice == 9:
        msg += '疲れてるのかも？ゆっくりお風呂に入って、ストレッチして、早く寝てしまうのがいいかも！'
    return msg

def batou(msg):
    dice = random.randrange(11)
    if dice == 1:
        msg += '何物欲しそうな顔で見てるんです？のなめを見つめる許可、出してないですよ。'
    elif dice == 2:
        msg += 'botに話しかけて喜ぶだなんて、変態ですね。'
    elif dice == 3:
        msg += '本当、気持ち悪い。どうしようもない変態ですね。'       
    elif dice == 4:
        msg += 'くさいから話しかけないでくれますか？'    
    elif dice == 5:
        msg += '何見てるんですか、豚。'
    elif dice == 6:
        msg += 'えっきもいよ？'
    elif dice == 7:
        msg += 'ねぇ、昨日も頑張るって言ってたよね？何か進んだのかな？'
    elif dice == 8:
        msg += 'キミ、ほんとに口だけだよね。頑張るとか聞き飽きたんだけど。'
    elif dice == 9:
        msg += '毎日毎日同じことばっか聞いてきて、話しかける人いないの？'
    elif dice == 10:
        msg += 'そんなことお願いして、どうするつもりなの？普通に引きます。'
    elif dice == 11:
        msg += '毎日のなめがあなたなんかのために、返信してあげてるんだから、感謝してくださいね？'

    return msg   

def ganbaru(msg):
    dice = random.randrange(9)
    if dice == 1:
        msg += 'えらい！超えらい！！めっちゃ頑張れー！！'
    elif dice == 2:
        msg += '頑張れ頑張れ！めっちゃ頑張れ！！'
    elif dice == 3:
        msg += '頑張れーーー！キミはやればできる子！だよ！！'
    elif dice == 4:
        msg += 'け、計測不能・・・す、すごいやる気です！！'
    elif dice == 5:
        msg += 'やる気ゲージ上昇中…やる気ゲージ上昇中…のなめは邪魔にならないように退避しまーす！頑張ってね！'
    elif dice == 6:
        msg += '頑張ってね？のなめはこっそり見守ります。。'
    elif dice == 7:
        msg += 'Done is better than Perfect! 完璧を目指すより終わらせよう！頑張って！'
    elif dice == 8:
        msg += 'Ask for Forgiveness, not Permission! 許可？後で謝まればいいよ！やっちゃえ☆'
    else:
        msg += '応援団長ののなめだよ！フレっフレ！頑張れ！フレッフレ！かっこいいぞー！'
    return msg

def nurupo(msg):
    dice = random.randrange(3)
    if dice == 1:
        msg += 'ガッ'
    elif dice == 2:
        msg += 'ガッ…とか言わせないでくれる？'
    else:
        msg += 'ガッ…ってしまった！'
    return msg

def uranai(msg):
    dice = random.randrange(500)
    negaposi = ''
    if dice == 1:
        msg = 'すごい。何を言っているのかわからないと思うがのなめ占いで最も尊い運勢を出した。今日はいい事あるぜ。間違いねえよ。'
        negaposi = 'posi'
    if dice > 1 and dice < 10:
        msg = 'あなたに幸せが舞い降りるかも！！大の吉！ですよ！おめでとうございますうううううううううううう'
        negaposi = 'posi'
    elif dice > 10 and dice < 50:
        msg = '吉です。のなめ占いでは中吉よりぐっどです。いいことあるかも？！おめでとうございます！'    
        negaposi = 'posi'
    elif dice > 50 and dice < 150:
        msg = '中の吉です。今日はそこそこ幸せな一日が訪れるかもしれません。'
        negaposi = 'posi'
    elif dice > 150 and dice < 300:
        msg = '小吉です。小さな幸せって意外とその辺にあったりしますよね。'    
        negaposi = 'posi'
    elif dice > 300 and dice < 400:
        msg = 'ガーン…末吉です。今日はちょっと気を付けて行きましょう。'
        negaposi = 'nega'
    elif dice > 400 and dice < 490:
        msg = 'ひぇ！凶！ちょっと今のはなかったことに・・・'
        negaposi = 'nega'
    elif dice > 490:
        msg = 'お客さん、、こいつはちょっといけませんぜ、、、大の凶です。今日はもう外に出ないでくだせえ。。。'
        negaposi = 'nega'
    else:
        msg = 'ん～～～～？ちょっと何も見えないみたいです・・・'
    return msg, negaposi

def luckynum(msg, negaposi):
    nmdice = random.randrange(10)
    if negaposi == 'posi':
        msg = 'ラッキーナンバーは・・・' + str(nmdice) + 'です！！'
    elif negaposi == 'nega':
        msg = 'NGナンバーは・・・' + str(nmdice) + 'です！！'
    else:
        msg = 'すみません、もう一度お願いします'
    return msg

def luckycolor(msg, negaposi):
    clr = ['白','黒','赤','青','緑','黄','ピンク','シアンブルー','紫','金','銀','オレンジ','ワインレッド','マゼンタ','紺','藍色','水','セピア','エメラルドグリーン','深紅','赤紫','青紫','ベージュ']
    clrdice = random.randrange(len(clr))
    if negaposi == 'posi':
        msg = 'ラッキーカラーは・・・' + str(clr[clrdice]) + 'です！！'
    elif negaposi == 'nega':
        msg = 'NGカラーは・・・' + str(clr[clrdice]) + 'です！！'
    else:
        msg = 'すみません、もう一度お願いします'
    return msg

def advice(msg, negaposi):
    nmdice = random.randrange(10)
    if negaposi == 'posi':
        msg = 'はりきっていきましょー！'
    elif negaposi == 'nega':
        msg = '気を付けてくださいね？'
    return msg

def diceroll(face, cnt):
    ans = ''
    total = 0
    for i in range(cnt):
        dice = random.randrange(face) + 1
        ans += ' ' + str(dice)
        total += dice
    return ans, total

def somedice(msg, msgcontent):
    flag = False
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')[1]
        if 'd' in datas and datas.count('d') == 1:
            faces, cnts = datas.split('d')
            if faces.isnumeric() and cnts.isnumeric:
                face = int(faces)
                cnt = int(cnts)
                msg += 'サイコロは' + faces + '面ダイスを' + cnts + '個だね！'
                ans, total = diceroll(face, cnt)
                msg += '出目は・・・' + ans + '・・・っと。'
                msg += '合計で・・・ ' + str(total) + '・・・だよ！どうだったかな？'
            else:
                flag = True
        else:
            flag = True
    else:
        flag = True
    if flag:        
        dice = random.randrange(6)
        msg += 'サイコロは１個でいいかな？'
        ans, total = diceroll(6, 1)
        msg += '出目は・・・' + str(total) + '・・・だよ！。'
        if dice % 3 == 0:
            msg += 'サイコロを指定したいときは、 !dice 12d6 みたいな形で話しかけてみてね！'
            msg += '12面ダイスを6個振る事ができるよ！ぜひやってみて☆'
    return msg

def dicegame(msg,msgcontent):
    flag = False
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')[1]
        if 'd' in datas and datas.count('d') == 1:
            faces, cnts = datas.split('d')
            if faces.isnumeric() and cnts.isnumeric:
                face = int(faces)
                cnt = int(cnts)
                msg += 'サイコロは' + faces + '面ダイスを' + cnts + '個だね！'
                msg += '先行はあなたからだね！'
                ans1, total1 = diceroll(face, cnt)
                msg += '出目は・・・' + ans1 + '・・・っと。'
                msg += '合計で・・・ ' + str(total1) + '・・・だよ！'
                msg += '次はのなめの番！'
                ans2, total2 = diceroll(face, cnt)
                msg += '出目は・・・' + ans2 + '・・・っと。'
                msg += '合計で・・・ ' + str(total2) + '・・・だよ！'
                msg += '結果は・・・' + str(total1) + '対' + str(total2) + '・・・だよ！'
                if total1 > total2:
                    msg += 'あなたの勝ち！悔しい～～～！もっかい勝負しよ！！'
                elif total2 > total1:
                    msg += 'のなめの勝ち！やったやったーー！いえい！！'
                else:
                    msg += '引き分けだ！惜しい！もっかい勝負する？'
            else:
                flag = True
        else:
            flag = True
    else:
        flag = True
    if flag:        
        msg += 'サイコロ勝負をする時は、サイコロを指定してね！'
        msg += '!dicegame 12d6 とか !サイコロ勝負 12d6 みたいな形で話しかけてみてね！'
        msg += '12面ダイスを6個の合計値で のなめと勝負だよ！ ぜひやってみて☆'
    return msg

def ninja(msg,user):
    dice = random.randrange(5)
    if dice == 1:
        msg += 'アイエエエ！'
    elif dice == 2:
        msg += 'ザッケンナコラー！'
    elif dice == 3:
        msg += 'シャッコラー！'
    elif dice == 4:
        msg += 'ニンジャ！？ニンジャナンデ！？'
    elif dice == 5:
        msg += 'ドーモ。'+ str(user) +'＝サン！ノナメスレイヤーです'
    return msg

def owaranai():
    keyword = ['プログラミング','仕様作成','要件定義','デバッグ','不具合修正','基本設計','UI設計','詳細設計','テーブル設計']
    dice = random.randrange(len(keyword))
    ans = keyword[dice]
    return ans

def yurusitekure():
    keyword = ['上司','本部長','社長','依頼部門','常務','役員','お客さん']
    dice = random.randrange(len(keyword))
    ans = keyword[dice]   
    return ans

def finder(msg,user):
    oware = owaranai()
    yuruse = yurusitekure()
    msg += 'うわあ、終わらないよ。' + oware +'が 終わらないよ。'
    msg += '許してくれ 許してくれ。' + yuruse + '許してくれ。'
    msg += 'ん？君はもしかして ' + yuruse + '！'
    msg += yuruse + '僕を許してくれるのかい？'
    msg += '僕は許されてもいいのかい。'
    msg += 'うううううう。'
    msg += 'ありがとう ' + yuruse + 'ありがとう…'
    return msg

def dec2bin(msg, msgcontent):
    flag = False
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')[1]
        msg += "「" + datas + "」を10進数から2進数に変換するよ！"
        try:
            msg += str(bin(int(datas))) + "。。。だよ！"
        except:
            msg += "変換できないよ？10進数を入れてね！"
    else:
        flag = True
    if flag:        
        msg += '!dec2bin 1234 の形で10進数の数字を打ってみて！2進数に変換するよ！'
    return msg

def dec2hex(msg, msgcontent):
    flag = False
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')[1]
        msg += "「" + datas + "」を10進数から16進数に変換するよ！"
        try:
            msg += str(hex(int(datas))) + "。。。だよ！"
        except:
            msg += "変換できないよ？10進数整数を入れてね！"
    else:
        flag = True
    if flag:        
        msg += '!dec2hex 1234 の形で10進数の数字を打ってみて！16進数に変換するよ！'
    return msg

def bin2dec(msg, msgcontent):
    flag = False
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')[1]
        msg += "「" + datas + "」を2進数から10進数に変換するよ！"
        try:
            msg += str(int(datas,2)) + "。。。だよ！"
        except:
            msg += "変換できないよ？2進数を入れてね！"
    else:
        flag = True
    if flag:        
        msg += '!bin2dec 1001 の形で2進数の数字を打ってみて！10進数に変換するよ！'
    return msg

def hex2dec(msg, msgcontent):
    flag = False
    if ' ' in msgcontent:
        datas = msgcontent.split(' ')[1]
        msg += "「" + datas + "」を16進数から10進数に変換するよ！"
        try:
            msg += str(int(datas,16)) + "。。。だよ！"
        except:
            msg += "変換できないよ？16進数を入れてね！"
    else:
        flag = True
    if flag:        
        msg += '!bin2dec FE の形で16進数の数字を打ってみて！10進数に変換するよ！'
    return msg