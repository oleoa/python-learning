import random

import os
clear = lambda: os.system('clear')

possible_answers = ["apple", "maybe", "never", "union", "house"]
template = list("_____")
chances = 10
answer = possible_answers[random.randrange(len(possible_answers))]
over = False

def new_game():
    global template, chances, answer, over
    template = list("_____")
    chances = 10
    answer = possible_answers[random.randrange(len(possible_answers))]
    over = False

def try_letter(letter):
    if letter in answer:
        for i in range(len(answer)):
            if answer[i] == letter:
                template[i] = letter
    else:
        global chances
        chances -= 1

def new_round():
    clear()
    print("".join(template))
    print("Chances: ", chances)
    user_try = input("Try to guess a letter: ")
    try_letter(user_try)

def check_if_player_won():
    if "_" not in template:
        clear()
        print("".join(template))
        print("You won!")
        global over
        over = True
        game_over()

def check_if_player_lost():
    if chances == 0:
        clear()
        print("".join(template))
        print("You lost!")
        global over
        over = True
        game_over()

def start_game():
    while not over:
        new_round()
        check_if_player_won()
        check_if_player_lost()

def game_over():
    restart = input("Press 'Enter' to restart ")
    if restart == "":
        clear()
        new_game()

start_game()
