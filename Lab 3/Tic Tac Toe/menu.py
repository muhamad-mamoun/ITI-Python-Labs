#! /bin/python3

class Menu:
    def display_menu(self, *args):
        for index, option in enumerate(args):
            print(f'{index + 1}- {option}')
        while True:
            try:
                user_input = int(input('Enter your choice number: '))
                if user_input in range(1, len(args) + 1): return user_input
                else: raise Exception()
            except: print('Error: Invalid option number')
            else: break
