#!/usr/bin/env python

import cgi
import random

form=cgi.FieldStorage()    # (1)

dic = {"1":"Rock","2":"Scissors","3":"Paper"}

user = form.getfirst('janken')
user_choice = dic[user]

choice_list = ['1','2','3']
pc = dic[random.choice(choice_list)]

draw = '<font color="#32CD32">DRAW</font>'
win = '<font color="#FF7F50">You Win!!</font>'
lose = '<font color="#0000FF">You lose!!</font>'

if user_choice == pc:
    judge = draw
else:
    if user_choice == "Rock":
        if pc == "":
            judge = win
        else:
            judge = lose
            
    elif user_choice == "Scissors":
        if pc == "Paper":
            judge = win
        else:
            judge = lose
            
    else:
        if pc == "Rock":
            judge = win
        else:
            judge = lose              


html_body = """
<html><body><center><br><br><br>
You chose %s<br><br>
Computer chose　%s<br><br>
<font size="5">　%s </font><br><br>
<A Href ="http://127.0.0.1:8000/janken.html">back</A>
</center></body></html>"""%(user_choice,pc,judge)



print("Content-type: text/html\n")
print(html_body)