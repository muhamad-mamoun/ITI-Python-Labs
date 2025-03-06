#! /bin/python3

import os
from validation import validate_project

def create(user_id):
    is_valid = None
    while not is_valid:
        os.system('clear')
        print('Create Project\n')
        if is_valid == False: print('Invalid data, try again...')
        title = input('Title: ').strip()
        details = input('Details: ').strip()
        target = input('Target: ').strip()
        start_date = input('Start date: ').strip()
        end_date = input('End date: ').strip()

        is_valid = validate_project(title, target, start_date, end_date)
    
    write(user_id, title, details, target, start_date, end_date)

def list_all(user_id):
    os.system('clear')
    print('You projects: \n')
    for project in list(filter(lambda line: line.split(':')[1] == str(user_id), open('projects.txt', 'r').read().split('\n'))):
        print(' || '.join(project.split(':')))
    input('\nPress any key to exit')

def delete(user_id):
    project_id = input('Enter project ID: ')
    all_projects = open('projects.txt', 'r').read().split('\n')
    for index, project in enumerate(all_projects):
        if project_id == project.split(':')[0] and project.split(':')[1] == user_id:
            del all_projects[index]
            with open('projects.txt', 'w') as file:
                file.write('\n'.join(all_projects))
            return True
    else: return False

def update(user_id):
    if delete(user_id): create(user_id)
    else: return False

def write(user_id, *args):
    project_id = get_max_id() + 1
    users_file = open('projects.txt', 'a')
    users_file.write(f'\n{project_id}:{user_id}:{':'.join(args)}')
    users_file.close()

def get_max_id():
    try:
        projects_ids = list(map(lambda line: line.split(':')[0], open('users.txt', 'r').read().split('\n')))
        return int(projects_ids[-1])
    except: return -1
