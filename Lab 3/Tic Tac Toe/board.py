#! /bin/python3

class Board:
    def __init__(self):
        self.__board = [ str(index) for index in range(1,10)]

    @property
    def board(self):
        return self.__board

    def display_board(self):
        for row in range(0, 9, 3):
            print(' | '.join(self.__board[row:row+3]))
            if row != 6: print('---' * 3)

    def update_board(self, choice, symbol):
        if self.validate_move(choice):
            self.__board[choice - 1] = symbol
            return True
        else: return False

    def validate_move(self, choice):
        return choice in range(1,10) and self.__board[choice - 1] in [ str(index) for index in range(1,10)]

    def reset_board(self):
        self.__board = [ index for index in range(1,10)]
