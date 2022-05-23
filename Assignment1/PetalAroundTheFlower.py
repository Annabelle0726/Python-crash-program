#
# File: PetalsAroundTheRose.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 13/7/2021
# Description: Programming Assignment 1 - Petals Around the Rose
# The name of the game is 'Petals Around the Rose'.
# The name of the game is important.
# The computer will roll five dice and ask you to guess the score for the roll.
# The score will always be zero or an even number.
# Your mission, should you choose to accept it, is to work out how the computer calculates the score.
# If you succeed in working out the secret and guess correctly four times in a row, you become a Potentate of the Rose.
# This is my own work as defined by the University's
# Academic Misconduct policy
import random

from dice import display_dice

flag = False
game = 0
game_win = 0
game_lose = 0
win = 0
lose = 0

print('''Petals Around the Rose 
----------------------
The name of the game is 'Petals Around the Rose'.  
The name of the game is important.  
The computer will roll five dice and ask you to guess the score for the roll.  
The score will always be zero or an even number.  
Your mission, should you choose to accept it, is to work out how the computer calculates the score. 
If you succeed in working out the secret and guess correctly four times in a row, 
you become a Potentate of the Rose.''')
while not flag:
    try:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die3 = random.randint(1, 6)
        die4 = random.randint(1, 6)
        die5 = random.randint(1, 6)
        display_dice(die1, die2, die3, die4, die5)  # use the display_dice() func
        die_list = [die1, die2, die3, die4, die5]
        user_answer = int(input('Please enter your guess for the roll:'))  # ask the user to guess the number
        sum_flower = 0  # the result in one game
        for i in range(5):
            if die_list[i] % 2 == 0 or die_list[i] == 1:
                sum_flower += 0
            elif die_list[i] == 3:
                sum_flower += 2
            else:
                sum_flower += 4

        if user_answer == sum_flower:
            print('Well done! You guessed it!', end='\n' * 2)
            game_win += 1  # record the win times
            win += 1
            lose = 0
            if win % 4 == 0 and win > 1:  # the user must guess correctly four times in a row
                print('Congratulations! You have worked out the secret!'
                      'Make sure you don\'t tell anyone!')

        else:
            print(f'No sorry, it\'s {sum_flower}, not {user_answer}')
            if user_answer < 0:
                print('The answer is always a positive number or 0.')
            elif abs(user_answer) % 2 == 1:  # odd number
                print(f'The score is always even.')
            if lose % 4 == 0 and lose > 1:  # guess incorrectly four times in a row
                print(f'Hint: The name of the game is important... Petals Around the Rose.')

            game_lose += 1
            lose += 1
            win = 0

        game += 1
        print(end='\n' * 2)
        flag = False  # end

        q1 = input('Would you like to play Petals Around the Rose [\'yes\'|\'no\']?')
        while q1 != 'yes' and q1 != 'no':
            print('Please enter [\'yes\'|\'no\']', end='\n' * 3)
            q1 = input('Would you like to play Petals Around the Rose [\'yes\'|\'no\']?')

        if q1 == 'yes':  # use the def petal_flower()
            q2 = input('Would you want to roll dice again?[\'yes\'|\'no\']')  # question
            while q2 != 'no':
                while q2 != 'yes' and q2 != 'no':  # validation
                    print('Please enter [\'yes\'|\'no\']', end='\n' * 3)
                    q2 = input('Would you want to roll dice again?[\'yes\'|\'no\']')
                if q2 == 'yes':  # use the def petal_flower()

                    q2 = input('Would you want to roll dice again?[\'yes\'|\'no\']')

            print('\n\nGame Summary\n'  # quit and display the result
                  f'============'
                  f'You played {game} games:\n'
                  f'|--> Number of correct guesses:      {game_win}\n'
                  f'|--> Number of incorrect guesses:    {game_lose}\n'
                  f'Thanks for playing!')
            flag = True  # end

        elif q1 == 'no':  # quit
            print('No worries... another time perhaps... :)')
            flag = True  # end

    except ValueError:
        print('You should have a valid number!\n\n')
