#!/usr/bin/env python

import random

dic = {"1":"Rock","Paper", "Scissors"}

Print "Rock, Paper, Scissors!"

pc_choice = random.choice(dic)
human_choice = raw_input("\nPick one from Rock,Paper or Scissors")

if pc_choice == human_choice:
    print "DRAW"
elif pc_choice == "Rock" and human_choice == "Paper"
    print "You WIN"
elif pc_choice == "Paper" and human_choice == "Scissors"
    print "You WIN"
elif pc_choice == "Scissors" and human_choice == "Paper"
    print "You WIN"
