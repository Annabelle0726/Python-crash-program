#
# File: homework2.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 03/07/2021
# Description: This is my program.
# First I need to check if user's input is correct;
# Next, print out the user's first word in his name.
# Then print out the local time.
# Forth, check user's birthday whether it's out of range.
# Fifth, check user's yes or no question.
# Finally, print out the year in his birth.
# This is my own work as defined by the University's
# Academic Misconduct policy
import time

finished = False
while not finished:
    try:
        fullName = input('Please tell me your fullname\n')  # full name
        name = fullName.split()
        print(f'OK, {name[0].title()}...\nNow, I am going to guess your birth of year...\n')

        print('Today\'s date is:', time.strftime('%d/%m/%Y'))  # the current time
        userAge = int(input('How old are you?\n'))
        while userAge > 120 or userAge < 0:
            print('You should recheck your input age!')  # invalid age
            userAge = int(input('How old are you?\n'))
        year = int(time.localtime().tm_year)
        ifBirthday = input('Have you had a birthday this year?(yes/no)\n')
        while ifBirthday != 'yes' and ifBirthday != 'no':  # validation
            print('Your input is not correct')
            ifBirthday = input('Have you had a birthday this year?(yes/no)\n')

        # result
        if ifBirthday == 'yes':
            print('You were born in the year', year - userAge)
        else:
            print('You were born in the year', year - userAge - 1)
        finished = True

    except IndexError:  # no empty name
        print('You can\'t have an empty name')
    except ValueError:  # int
        print('You have to input an int')
