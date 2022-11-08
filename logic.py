# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random

currentPlayer = random.choice(['X', '0'])
winner = None
def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', '0', or None."""
    if checkDig(board) or checkRow(board) or checkHorizon(board) :
        print(f"The dig winner is {winner}")
        print(board)   
    return winner


def other_player():
    """switch the global variable currentplayer """
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    elif currentPlayer == "0":
        currentPlayer = "X"
    else:
        print("player not x or 0!")


#take player input
def playerInput(board):
    print(currentPlayer, "Enter a number 1-9: ")
    position = int(input())
    if position >= 0 and position <= 8:
        currentSpot = board[position // 3][position - (position // 3) * 3]
        if currentSpot != None:
            print("This spot is aleady taken")
        else: board[position // 3][position - (position // 3) * 3] = currentPlayer
        #printBoard(board)
    else:
        print("only input 0-8")

#check for win or tie

def checkRow(board):
    global winner
    for i in range(3):
        if board[0][i] == None:
            return False
        player = board[0][i]
        if board[1][i] == player and board[2][i] == player:
            winner = player
            return True
    return False

    
def checkHorizon(board): 
    global winner
    for i in range(3):
        if board[i][0] == None:
            return False
        player = board[i][0] 
        if board[i][1] == player and board[i][2] == player:
            winner = player
            return True
    return False 

def checkDig(board):
    global winner
    if board[1][1] == None:
         return False
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return True
    return False
