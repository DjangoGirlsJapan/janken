#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

dic = """問１：1がグー２がチョキ３がパーとなる辞書をつくってください"""

print(u"じゃーんけーん")
print(u"1=グー　2=チョキ　3=パー　を入力")
user = input('>>>  ')

try:
    user_choice = """問2：userが入力した数字からdicを使ってグーかチョキかパーの文字を取得してください"""

    choice_list = ['1','2','3']
    pc = """問3：import したrandomを使って、PCに数字をチョイスさせて、且つグーかチョキかパーの文字列を取得してください"""

    draw = 'DRAW'
    win = 'You Win!!'
    lose = 'You lose!!'

    """問4：ユーザの手とPCの手を比較して結果を取得してください
    結果はjudgeという変数を作成して上記のdraw win loseのいずれかを
    変数にいれてください。"""

    print(u"あなた選んだのは %s"%user_choice)
    print(u"コンピュータが選んだのは %s"%pc)
    print(u"結果は%s"%judge)
except:
    print(u"1か２か３を入力してください。")
