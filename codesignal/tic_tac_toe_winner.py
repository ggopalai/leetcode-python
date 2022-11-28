#passed 12 out of 14.
import numpy as np 

def solution(board):
    n = len(board)
    nb = []
    #convert to list of lists
    for i in range(n):
        t = []
        for j in board[i]:
            t.append(j)
        nb.append(t)
    board = nb
    
    #check if user wins by rows 
    def checkRows(board):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0
    
    #check if user wins by diagonal
    def checkDiagonals(board):
        #main diagonal 
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return f'{board[0][0]} WIN'
        #anti-diagonal
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return f'{board[0][len(board)-1]} WIN'
        # if neither has won, and empty spaces on board
        for i in board:
            for j in i:
                if j == ".":
                    return 'ONGOING'
        return 'TIE'
    
    def checkWin(board):
        for newBoard in [board, np.transpose(board)]:
            result = checkRows(newBoard)
            if result:
                return f'{result} WIN'
        return checkDiagonals(board)
    
    return checkWin(board)
    
    
    
    
    
    
