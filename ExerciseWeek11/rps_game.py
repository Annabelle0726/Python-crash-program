#
# File: exercise.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 31/8/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
import random

num_games = 0
choice = ['rock', 'scissors', 'paper']


def generate_number():
    player = int(input('Rock(1), Scissors(2) or Paper(3)?'))
    player -= 1
    return player


x = generate_number()


def determine_winner(p):
    global num_games
    hPlayer = choice[p]
    print(f'You choose {hPlayer}')
    computer = random.randint(0, len(choice) - 1)
    cPlayer = choice[computer]
    print(f'Computer chooses {cPlayer}')
    play = p - computer

    if play % 3 == 1:
        print(f'{cPlayer} beats {hPlayer}\nYou lose')
    elif play % 3 == 2:
        print(f'{hPlayer} beats {cPlayer}\nYou win')
    else:
        print('Draw!')
    num_games += 1
    print(end='\n\n')


def play_game():
    determine_winner(x)
    q = input('Play again (y|n)?')
    while q != 'y' and q != 'n':
        print('Error\n')
        q = input('Play again (y|n)?')

    while q == 'y':
        generate_number()
        determine_winner(x)
        q = input('Play again (y|n)?')


if __name__ == '__main__':
    play_game()

    def display_details(n):
        if n == 1:
            print("\n\nYou played", n, "game!")
        else:
            print("\n\nYou played", n, "games!")


    display_details(num_games)