# File: assignment2 part2.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 25/8/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
import profile
import list_function


def add_profile(profile_list):
    email = input('Please enter email address: ')
    # traverse the profile list to prove that there is no email in it
    if email not in [x.get_email() for x in profile_list]:
        given_name = input('Please enter given name: ')
        family_name = input('Please enter family name: ')
        gender = input('Please enter gender: ')
        status = input('Please enter current status: ')
        new_profile = profile.Profile()
        new_profile.set_given_name(given_name)
        new_profile.set_family_name(family_name)
        new_profile.set_email(email)
        new_profile.set_gender(gender)
        new_profile.set_status(status)
        profile_list.append(new_profile)
        print(f'Successfully added {email} to profiles.\n')

    else:
        print(f'{email} already exists in profiles.\n')
    return profile_list


def remove_profile(profile_list):
    email = input('Please enter email address: ')
    # judge whether email is in the list
    if email not in [x.get_email() for x in profile_list]:
        print(f'{email} is not found in profiles.\n')

    else:
        # find and delete email
        item = list_function.search(email, profile_list)
        profile_list = list_function.remove_index(item, profile_list)
        # find and delete mail in friend_list
        for people in profile_list:
            people.remove_friend(email)
        print(f'Successfully removed {email} from profiles.\n')
    return profile_list


def display_summary(profile_list):
    print(70 * '=')
    print('Profile Summary')
    print(70 * '=')
    print(70 * '-')
    for item in profile_list:
        string = f'{item.get_given_name()} {item.get_family_name()} ({item.get_gender()} | {item.get_email()})\n'
        string += f'- {item.get_status()}'

        if item.get_number_friends() == 0:
            string += '\n- No friends yet...\n'
        else:
            string += f'\n- Friends ({item.get_number_friends()})\n'
            for friend_email in item.get_friends_list():
                for f in profile_list:
                    f1 = f.get_email().strip()
                    friend_email = friend_email.strip()
                    if friend_email == f1:
                        string += f'{f.get_given_name()} {f.get_family_name()}\n'

        print(string, end='')
        print(70 * '-')
    print()


def find_profile(profile_list, email):
    if email not in [item.get_email() for item in profile_list]:
        return None
    else:
        item = list_function.search(email, profile_list)
        return item


def read_file(filename, profile_list):
    with open(filename, "r") as data:
        line = data.readline()
        while line:
            list_data = line.split()
            given_name = list_data[0]
            family_name = list_data[1]
            email = list_data[2]
            gender = list_data[3].strip()
            status = data.readline().strip()
            # add to the profile_list
            new_profile = profile.Profile(given_name, family_name, email, gender, status)
            number_of_friend = int(data.readline())
            list_friends = []
            for item in range(number_of_friend):
                friend = data.readline().strip()
                list_friends.append(friend)
            new_profile.set_friends_list(list_friends)
            profile_list.append(new_profile)
            # get the new line
            line = data.readline()
    return profile_list


def write_to_file(filename, profile_list):
    with open(filename, 'w') as file0:
        for item in profile_list:
            string = f'{item.get_given_name()} {item.get_family_name()} {item.get_email()} {item.get_gender()}\n'
            string += f'{item.get_status()}\n'
            string += f'{item.get_number_friends()}\n'
            for friend_email in item.get_friends_list():
                string += friend_email
            file0.write(string)


# Define a list to store Profile objects
profile_list = []

profile_list = read_file("profiles.txt", profile_list)

command = input('Please enter choice [summary|add|remove|search|update|quit]: ')
while command != 'quit':
    if command not in ['summary', 'search', 'update', 'add', 'remove']:
        print('Not a valid command - please try again.\n')
        command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

    elif command == 'summary':
        display_summary(profile_list)
        print()
        command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

    elif command == 'search':
        email = input('Please enter email address: ')
        index = find_profile(profile_list, email)
        if index != -1:
            count = 0
            for item in profile_list:
                if count == index:
                    string = f'{item.get_given_name()} {item.get_family_name()} ({item.get_gender()} | ' \
                             f'{item.get_email()})\n'
                    string += f'- {item.get_status()}\n'
                    if item.get_number_friends() == 0:
                        string += '- No friends yet...\n'
                    else:
                        string += f'- Friends ({item.get_number_friends()})\n'
                        for friend_email in item.get_friends_list():
                            for f in profile_list:
                                f1 = f.get_email().strip()
                                friend_email = friend_email.strip()

                                if friend_email == f1:
                                    string += f'{f.get_given_name()} {f.get_family_name()}\n'
                    print(string, end='')
                count += 1

        else:
            print(f'{email} is not found in profiles.\n')
        command = input('\nPlease enter choice [summary|add|remove|search|update|quit]: ')

    elif command == 'add':
        add_profile(profile_list)
        command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

    elif command == 'remove':
        profile_list = remove_profile(profile_list)
        command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

    elif command == 'update':
        email = input('Please enter email address: ')
        if find_profile(profile_list, email) == -1:
            print(f'{email} is not found in profiles.')
            command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

        else:
            index0 = find_profile(profile_list, email)
            if index0 != -1:
                count0 = 0
                for item in profile_list:
                    if count0 == index0:
                        command1 = input(f'Update {item.get_given_name()} [status|add_friend|remove_friend]: ')

                        if command1 not in ['status', 'add_friend', 'remove_friend']:
                            print('Not a valid command - returning to main menu.')
                            command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

                        elif command1 == 'status':
                            new_status = input('Please enter status update: ')

                            index = find_profile(profile_list, email)
                            if index != -1:
                                count = 0
                                for item in profile_list:
                                    if count == index:
                                        item.set_status(new_status)
                                        print(
                                            f'Updated status for {item.get_given_name()} {item.get_family_name()}:')
                                        string = f'{item.get_given_name()} {item.get_family_name()} ' \
                                                 f'({item.get_gender()} | {item.get_email()})\n'
                                        string += f'- {item.get_status()}\n'

                                        if item.get_number_friends() == 0:
                                            string += '- No friends yet...\n'
                                        else:
                                            string += f'- Friends ({item.get_number_friends()})\n'
                                            for friend_email in item.get_friends_list():
                                                for f in profile_list:
                                                    f1 = f.get_email().strip()
                                                    friend_email = friend_email.strip()

                                                    if friend_email == f1:
                                                        string += f'{f.get_given_name()} {f.get_family_name()}\n'

                                        print(string, end='')
                                        print()
                                        command = input('Please enter choice [summary|add|remove|search|update|quit]: ')
                                    count += 1

                            else:
                                print(f'{email} is not found in profiles.')
                                command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

                        elif command1 == 'add_friend':
                            new_friend_email = input('Please enter email address of friend to add: ')
                            if find_profile(profile_list, new_friend_email) == -1:
                                print(f'{new_friend_email} is not found in profiles.\n')
                                command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

                            else:
                                # find profile of email
                                index = find_profile(profile_list, email)
                                if index != -1:
                                    count = 0
                                    for i in profile_list:
                                        if count == index:
                                            if i.is_friend(new_friend_email):
                                                index_new_friend = find_profile(profile_list, new_friend_email)
                                                count1 = 0
                                                for p in profile_list:
                                                    if count1 == index_new_friend:
                                                        print(f'{p.get_given_name()} is already a friend.')
                                                        command = input(
                                                            'Please enter choice [summary|add|remove|search|update|'
                                                            'quit]: ')
                                                    count1 += 1

                                            else:
                                                # find given name of the new1 friend
                                                index_new_friend = find_profile(profile_list, new_friend_email)
                                                count1 = 0
                                                for p in profile_list:
                                                    if count1 == index_new_friend:
                                                        print(f'Added {p.get_given_name()}\n')

                                                    count1 += 1

                                                # add new1 friend and display new1 profile
                                                i.add_friend(new_friend_email)
                                                string = f'{i.get_given_name()} {i.get_family_name()} ' \
                                                         f'({i.get_gender()} | {i.get_email()})\n'
                                                string += f'- {i.get_status()}\n'
                                                string += f'- Friends ({i.get_number_friends()}):\n'
                                                # get every friend email in friend_list

                                                for friend_email in i.get_friends_list():
                                                    # get every email in profile_list
                                                    index_new_friend = find_profile(profile_list, friend_email)
                                                    count1 = 0
                                                    for p in profile_list:
                                                        if count1 == index_new_friend:
                                                            string += f'{p.get_given_name()} {p.get_family_name()}\n'
                                                        count1 += 1

                                                print('Updated profile is:')
                                                print(string)
                                                command = input(
                                                    'Please enter choice [summary|add|remove|search|update|quit]: ')
                                        count += 1

                        elif command1 == 'remove_friend':
                            new_friend_email = input('Please enter email address of friend to remove:')
                            if find_profile(profile_list, new_friend_email) == -1:
                                print(f'{new_friend_email} is not found in profiles.\n')
                                command = input('Please enter choice [summary|add|remove|search|update|quit]: ')

                            else:
                                # find profile of email
                                index = find_profile(profile_list, email)
                                if index != -1:
                                    count = 0
                                    for i in profile_list:
                                        if count == index:
                                            if i.is_friend(new_friend_email):
                                                i.remove_friend(new_friend_email)
                                                print(f'Removed {new_friend_email}\n')
                                                print('Updated profile is: ')
                                                string = f'{i.get_given_name()} {i.get_family_name()}' \
                                                         f' ({i.get_gender()} | {i.get_email()})\n'
                                                string += f'- {i.get_status()}\n'
                                                string += f'- Friends ({i.get_number_friends()}):\n'
                                                # get every friend email in friend_list
                                                for friend_email in i.get_friends_list():
                                                    # get every email in profile_list
                                                    index_new_friend = find_profile(profile_list, friend_email)
                                                    count1 = 0
                                                    for p in profile_list:
                                                        if count1 == index_new_friend:
                                                            string += f'{p.get_given_name()} {p.get_family_name()}\n'
                                                        count1 += 1
                                                print(string)
                                                command = input(
                                                    '\nPlease enter choice [summary|add|remove|search|update|quit]: ')
                                            else:
                                                index = find_profile(profile_list, email)
                                                if index != -1:
                                                    count = 0
                                                    for i in profile_list:
                                                        if count == index:
                                                            print(
                                                                f'{new_friend_email} is not '
                                                                f'{i.get_given_name()}\'s friend.')
                                                            command = input(
                                                                '\nPlease enter choice [summary|add|remove|search'
                                                                '|update|quit]: ')

                                        count += 1

                    count0 += 1

    write_to_file('new_profiles', profile_list)
print("-- Program terminating --")
