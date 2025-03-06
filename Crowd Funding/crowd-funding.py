#! /bin/python3

import os
import users
import projects

def main_menu():
    is_valid = None
    while not is_valid:
        os.system('clear')
        print('Crowd Funding System\n')
        if is_valid == False: print('Invalid option, try again...')
        print('1- Login\n2- Register\n3- Exit\n')
        user_input = input('Enter your choice number: ')
        if(user_input.isdigit()): user_input = int(user_input)

        match user_input:
            case 1: return users.login()
            case 2: return users.register()
            case 3: exit()
            case _: is_valid = False

def user_menu(user_data):
    is_valid = None
    while not is_valid:
        os.system('clear')
        print(f'Welcome, {user_data[1]}!\n')
        if is_valid == False: print('Invalid option, try again...')
        print('1- Create project\n2- List projects\n3- Update project\n4- Delete project\n5- Exit\n')
        user_input = input('Enter your choice number: ')
        if(user_input.isdigit()): user_input = int(user_input)

        match user_input:
            case 1: projects.create(user_data[0])
            case 2: projects.list_all(user_data[0])
            case 3: projects.update(user_data[0])
            case 4: projects.delete(user_data[0])
            case 5: exit()
            case _: is_valid = False

if __name__ == '__main__':
    logged_in_user = main_menu()
    user_menu(logged_in_user)
