#! /bin/python3

import os
from player import Player
from board import Board
from menu import Menu

class Game:
    def __init__(self):
        self.__current_palyer_index = 0
        self.__players = [Player(), Player()]
        self.__board = Board()
        self.__menu = Menu()
    
    def init(self):
        choice = self.__menu.display_menu('Start game', 'Quit game')
        self.clear_screen()
        if choice == 1:
            self.setup_players()
            self.start_game()
        elif choice == 2: self.quit_game()

    def setup_players(self):
        for index, player in enumerate(self.__players):
            print(f'Player {index + 1} setup:')
            player.choose_name()
            player.choose_symbol()
            self.clear_screen()
        
    def start_game(self):
        while True:
            self.clear_screen()
            self.__board.display_board()
            self.play_turn()
            if self.check_draw() or self.check_win():
                self.clear_screen()
                print('Game over!\n')
                choice = self.__menu.display_menu('Restart game', 'Quit game')
                if choice == 1: self.restart_game()
                elif choice == 2: self.quit_game()
                break
            else: pass

    def play_turn(self):
        while True:
            try:
                cell_number = int(input(f'{self.__players[self.__current_palyer_index].name}\'s turn, choose a cell [1-9]: '))
                if cell_number not in range(1,10): raise Exception()
            except: print('Invalid cell number')
            else:
                self.__board.update_board(cell_number, self.__players[self.__current_palyer_index].symbol)
                self.__current_palyer_index ^= 1
                break

    def check_win(self):
        win_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]

        for case in win_cases:
            if self.__board.board[case[0]] == self.__board.board[case[1]] == self.__board.board[case[2]] and self.__board.board[case[0]] != str(case[0] + 1):
                return self.__players[self.__current_palyer_index]
        return None

    def check_draw(self):
        return all(list(map(lambda value: value.isalpha(), self.__board.board)))

    def restart_game(self):
        self.__board.reset_board()
        self.__current_palyer_index = 0
        self.init()

    def quit_game(self):
        print('Thank you for playing!')
        exit(0)

    @staticmethod
    def clear_screen():
        os.system( 'clear' if os.name == 'posix' else 'cls')