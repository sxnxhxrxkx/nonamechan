import os
from logging import getLogger, FileHandler, StreamHandler, Formatter, shutdown

def writelog(logname,systemname,msg):
    #logpath = 'C:\\Users\\EXPRESS\\Desktop\\python\\00_Python_Program\\PM\\log'
    logpath = 'log'
    if os.path.exists(logpath) == False:
        print("mkdir", logpath)
        os.makedirs(logpath)

    # ログの出力名を設定
    logger = getLogger(logname)
    msg = "[" + systemname + "]" + msg
    if logname == 'notest': #設定値の記録
        level = 0
    elif logname == 'debug': #動作確認の記録
        level = 10
    elif logname == 'info': #正常動作の記録
        level = 20
    elif logname == 'warning': #ログの記録
        level = 30
    elif logname == 'error': #エラーの記録
        level = 40
    # elif logname == 'critical': #停止の記録
    #    level = 50
    
    # ログレベルの設定
    logger.setLevel(level)
    # ログのファイル出力先を設定
    fh = FileHandler(logpath + os.sep + 'log.log')
    logger.addHandler(fh)
    # ログのコンソール出力の設定
    sh = StreamHandler()
    logger.addHandler(sh)
    # ログの出力形式の設定
    formatter = Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.log(level, msg)
    for h in logger.handlers:
        logger.removeHandler(h)
    return

def nonamelog(usrname, cmd, msg):
    logpath = 'log'
    if os.path.exists(logpath) == False:
        print("mkdir", logpath)
        os.makedirs(logpath)

    # ログの出力名を設定
    logname = 'info' #正常動作の記録
    logger = getLogger(logname)
    msg = "," + usrname + "," + cmd + "," + msg
    level = 20
    
    # ログレベルの設定
    logger.setLevel(level)
    # ログのファイル出力先を設定
    fh = FileHandler(logpath + '\\nonamelog.log')
    logger.addHandler(fh)
    # ログのコンソール出力の設定
    sh = StreamHandler()
    logger.addHandler(sh)
    # ログの出力形式の設定
    formatter = Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.log(level, msg)
    for h in logger.handlers:
        logger.removeHandler(h)
    return