#
# File: homework4.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 2/7/2021
# Description: This is my program.
# This is my own work as defined by the University's
# First, I need to check whether the file is exited or not;
# Second, open the file, read lines, ignore the space and the newline, store the wordlist in a list;
# Third, use the random module to choose the word in random wordlist, and split the word;
# Fourth, use dashes to hide the split word;
# Fifth, give user 10 incorrect guessing chance; if he's guess is correct, show the letter instead of using the dash;
# If user's input is not a small case letter print error;
# If the user get the right answer in 10 times, the loop break, print he wins;
# Otherwise, print out the right word, and say he lose!
# Academic Misconduct policy

import random
import re
finished = False
while not finished:
    try:
        def read_file(txt):
            with open(txt, "r", encoding='utf-8') as rStream:  # open the file
                lines = rStream.readlines()
            wordlist = []
            for line in lines:
                wordlist.append(line.strip())
            return wordlist


        txt1 = r'words.txt'


        def select_random_word(wordlist):
            random_list = random.choice(wordlist)  # randomly select the line
            words = random_list.split()
            random_letter = random.choice(words)  # randomly select the letter
            return random_letter


        letters = select_random_word(read_file(txt1))


        def create_dashes(random_letter):
            dashes = []
            for i in random_letter:
                dashes.append('-')  # use the dash to cover the letter
            return dashes


        dash = create_dashes(letters)
        dash_list = ''
        for item in dash:
            dash_list += item
        guessing = 10
        while guessing > 0 and dash_list != letters:
            print('\n', dash_list, sep='', end='\n'*2)
            choiceLetter = input('Enter a letter:')
            match = re.match(r'[a-z]$', choiceLetter)  # if it's the lowercase
            if not match:
                print('You should get a lowercase letter!')
            if choiceLetter in letters:
                for i in range(len(letters)):
                    if choiceLetter == letters[i]:
                        dash[i] = choiceLetter
                        dash_list = ''.join(dash)
            else:
                guessing = guessing - 1
                print(f'You guessed wrong! Your {guessing} miss remaining')  # not correct guessing

        # result
        if dash_list == letters:
            print(f'The word was {letters}, You win!')
            guessing = -1
            finished = True
        else:
            print(f'The word was {letters}\nYou lost!')
            finished = True

    except FileNotFoundError:  # no such file
        print('The file is not exited!')
