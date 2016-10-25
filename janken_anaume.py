#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""問１：1がグー２がチョキ３がパーとなる辞書をつくってください"""

dic = {}

print(u"じゃーんけーん")
print(u"1=グー　2=チョキ　3=パー　を入力")
user = input('>>>  ')

try:
    """問2：userが入力した数字からdicを使ってグーかチョキかパーの文字を取得してください"""
    user_choice = ''

    choice_list = ['1','2','3']
    """問3：import したrandomを使って、PCに数字をチョイスさせて、
    且つグーかチョキかパーの文字列を取得してください"""
    pc = 0

    draw = 'DRAW'
    win = 'You Win!!'
    lose = 'You lose!!'

    """問4：ユーザの手とPCの手を比較して結果を取得してください
    結果はjudgeという変数を作成して上記のdraw win loseのいずれかを
    変数にいれてください。"""

    print(u"あなた選んだのは " + user_choice)
    print(u"コンピュータが選んだのは " + pc)
    print(u"結果は " + judge)
except:
    print(u"1か２か３を入力してください。")
