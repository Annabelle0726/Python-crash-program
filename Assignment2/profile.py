#
#  PSP Assignment 2 (Part 2) - Provided module profile.py.
#
#  class Profile
#
#  DO NOT modify this file.
#


class Profile:

    def __init__(self, given_name='', family_name='', email='', gender='', status=''):
        '''Initialises the Profile object.
        To call this method you may write:
        my_friend = Profile('Bruce', 'Wayne', 'batman@batcave.com', 'm', 'I am the night') 
        '''
        self.__given_name = given_name
        self.__family_name = family_name
        self.__email = email
        self.__gender = gender
        self.__status = status
        self.__number_friends = 0
        self.__friends_list = []

    def set_given_name(self, name):
        self.__given_name = name

    def get_given_name(self):
        return self.__given_name

    def set_family_name(self, name):
        self.__family_name = name

    def get_family_name(self):
        return self.__family_name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def set_number_friends(self, no_friends):
        self.__number_friends = no_friends

    def get_number_friends(self):
        return self.__number_friends

    def set_friends_list(self, friends_list):
        self.set_number_friends(len(friends_list))
        self.__friends_list = friends_list

    def get_friends_list(self):
        return self.__friends_list

    def add_friend(self, email):
        '''Adds the argument email to the friends_list only if it does not already exist.
        Returns True if successful, otherwise False.
        '''
        if self.is_friend(email):
            return False

        # If not already friends, add friend and increment number_friends count
        self.__friends_list.append(email)
        self.__number_friends += 1
        return True

    def remove_friend(self, email):
        '''Removes the argument email from the friends_list if found.
        Returns True if successful, otherwise False.
        '''
        if self.is_friend(email) == False:
            return False

        # If is friend is True, remove friend and decrement number_friends count
        self.__friends_list.remove(email)
        self.__number_friends -= 1
        return True

    def is_friend(self, email):
        '''Searches friend list for argument email.
        Returns True if found, otherwise False.
        '''
        found = False
        for email_address in self.__friends_list:
            if email == email_address:
                found = True
        return found

    def __str__(self):
        '''Returns a string representation of the object.
        '''
        string = self.__given_name + ' ' + self.__family_name + ' ' + self.__email + ' ' + self.__gender + '\n'
        string += self.__status + '\n'
        string += str(self.__number_friends) + '\n'
        for friend_email in self.get_friends_list():
            string += friend_email + '\n'
        return string

    def __repr__(self):
        '''Returns a string representation of the object that
        will be displayed if printed in a list.
        '''
        return 'Profile: ' + self.__email

    def __eq__(self, email):
        '''Returns True if the argument email matches this object's email.
        Overrides the == operator, so that this method is called using:
        profile_obj == email
        '''
        if self.get_email() == email:
            return True
        return False
