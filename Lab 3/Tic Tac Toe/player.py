#! /bin/python3

import re as regex

class Player:
    def __init__(self):
        self.__name = ''
        self.__symbol = ''

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        pattern = r'^[A-Za-z\ ]+$'
        if bool(regex.fullmatch(pattern, name)): self.__name = name
        else: raise Exception('Invalid player name')

    @property
    def symbol(self):
        return self.__symbol
    
    @symbol.setter
    def symbol(self, symbol):
        if symbol in ['x', 'X', 'o', 'O']: self.__symbol = symbol.upper()
        else: raise Exception('Invalid player symbol')

    def choose_name(self):
        while True:
            try: self.name = input('Please enter your name: ')
            except Exception as error: print(f'Error: {error}')
            else: break

    def choose_symbol(self):
        while True:
            try: self.symbol = input(f'{self.name}, Please choose a symbol [X - O]: ')
            except Exception as error: print(f'Error: {error}')
            else: break
