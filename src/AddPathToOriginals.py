# -*- coding: utf-8 -*-

import sys,os,inspect
from pyfbsdk import *

system = FBSystem()
systemUIIdle = system.OnUIIdle

systemUIIdle.RemoveAll()

check = -1
def AddPathToOriginals(arg1:FBSystem, arg2:FBEvent):
    # 再度AddPathToOriginals関数が実行された時のためにcheckの値で分岐
    global check
    if check == -1:
        check = 0

        # 現在のパスを取得（配布プラグインをダウンロードしてもらう指定先）
        CurrentFilePath = inspect.currentframe().f_code.co_filename
        CurrentDir = os.path.dirname(CurrentFilePath)

        # 指定先フォルダ下においている、pathを追加したいフォルダへとモジュール検索パスを通す  
        # ここではOriginalSctiptsとしています
        targetPath = os.path.join(CurrentDir,"OriginalScripts")
        sys.path.append(targetPath)

    else:
        systemUIIdle.Remove(AddPathToOriginals)

systemUIIdle.Add(AddPathToOriginals)