#! /bin/python3

import os
from validation import validate_user

def register():
    is_valid = None
    while not is_valid:
        os.system('clear')
        print('Register\n')
        if is_valid == False: print('Invalid data, try again...')
        first_name = input('First Name: ').strip()
        last_name = input('Last Name: ').strip()
        email = input('Email: ').strip()
        password = input('Password: ').strip()
        password_confirmation = input('Confirm Password: ').strip()
        mobile = input('Mobile: ').strip()

        is_valid = validate_user(first_name, last_name, email, password, mobile) and (password == password_confirmation) and (find(email, 3) == -1)
    
    write(first_name, last_name, email, password, mobile)

def login():
    user_id = None
    is_valid = None
    while not is_valid:
        os.system('clear')
        print('Login\n')
        if is_valid == False: print('Wrong email or password, try again...')
        email = input('Email: ').strip()
        password = input('Password: ').strip()

        user_id = find(email, 3)
        is_valid = (user_id != -1) and compare_password(password, user_id)

    print('Logged in successfully')
    return get_data(user_id)

def find(value, field_index):
    try:
        field_values = list(map(lambda line: line.split(':')[field_index], open('users.txt', 'r').read().split('\n')))
        return field_values.index(value)
    except: return -1

def get_data(user_id):
    return list(filter(lambda line: line.split(':')[0] == str(user_id), open('users.txt', 'r').read().split('\n')))[0].split(':')

def write(*args):
    user_id = get_max_id() + 1
    users_file = open('users.txt', 'a')
    users_file.write(f'\n{user_id}:{':'.join(args)}')
    users_file.close()

def get_max_id():
    try:
        users_ids = list(map(lambda line: line.split(':')[0], open('users.txt', 'r').read().split('\n')))
        return int(users_ids[-1])
    except: return -1

def compare_password(password, user_index):
    field_values = list(map(lambda line: line.split(':')[4], open('users.txt', 'r').read().split('\n')))
    return password == field_values[user_index]
