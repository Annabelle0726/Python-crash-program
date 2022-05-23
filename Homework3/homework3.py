#
# File: homework3.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 28/06/2021
# Description: This is my program.
# It is about hiring employee and firing them.
# And you can not hire the staff name with an empty name
# You can not hire the staff with duplication of name
# You can not fire the staff does not exit;
# Every time when hiring, the employee list will be shown. And you can quit if you want.
# If you get an incorrect choice, you can start again.
# If at the end there's no staff in your staff list, print out the sentence "You have no staff"
# This is my own work as defined by the University's
# Academic Misconduct policy

import re
import time

staffList = []
q1 = input('Would you like to hire, fire or quit:\n')
while q1 != 'quit':
    while q1 != 'quit' and q1 != 'hire' and q1 != 'fire':  # validation
        print(f'{q1} is an invalid choice!\n\n')
        q1 = input('Would you like to hire, fire or quit:\n')

    if q1 == 'hire':
        name = input('Enter their name:\n')
        staff_name = re.compile(r'[a-zA-Z]+(\s[a-zA-Z]+)*|[a-zA-Z]$')  # check if the name is a person's name
        result = re.match(staff_name, name)
        while result is None:
            print(f'{name} is an incorrect staff name!')
            name = input('\nEnter their name:\n')  # loop again
            result = re.match(staff_name, name)

        if len(name) > 0:
            print(f'{name} is waiting to be hired...')
            time.sleep(2)

            if name in staffList:  # already in the staffList
                print(f'{name} has been hired already!')

            else:
                staffList.append(name)  # add the person into staffList
                msg = f'{name} has been hired.'
                print(msg)
                print('\nEmployee'.center(20, '-'))
                for i in range(len(staffList)):
                    print(str(i + 1) + '.', staffList[i])
        else:
            print('Please get a staff!')  # empty input
        q1 = input('\n\nWould you like to hire, fire or quit:\n')

    elif q1 == 'fire':
        name = input('Enter their name:\n')
        if len(name) > 0:
            print(f'{name} is waiting to be fired...')
            time.sleep(2)
            if name not in staffList:  # not in the staffList
                print(f'{name} can not be found')

            else:
                staffList.remove(name)
                msg = f'{name} has been fired.'
                print(msg)
                if len(staffList) == 0:
                    print('You have no employee!')
                else:
                    print('Employee'.center(20, '-'))
                    for i in range(len(staffList)):
                        print(str(i + 1) + '.', staffList[i])

        else:
            print('Please get a staff!')  # empty input
        q1 = input('\n\nWould you like to hire, fire or quit:\n')  # loop again

else:
    print('Thank you')
