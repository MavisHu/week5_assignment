# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logic

# printing the game board 
def printBoard(board):
    print(str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2]))

if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    while winner == None:

#Check for win or tie again
        printBoard(board)
        logic.playerInput(board)
        winner = logic.get_winner(board)
        logic.other_player()


    