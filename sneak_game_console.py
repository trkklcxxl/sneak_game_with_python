import os
import numpy as np
import time

# https://github.com/clear-code-projects/powershell-snake/blob/main/snake.py 

#zero -> space
#one -> barrier
#two -> sneak´s body

class Sneak:
    def __init__(self,size):
        self.size=size
        

class GameScreen:
    def __init__(self,sneak):
        self.sneak=sneak
    def CreateBoard(self):
        board=np.zeros((20,40))
        for i in range(20):
            for j in range(40):
                if(i==0):
                    board[i][j]=1
                if(i==19):
                    board[i][j]=1
                if(j==0):
                    board[i][j]=1
                if(j==39):
                    board[i][j]=1
                if(i==9 and j==19):
                    board[i][j]=2
        return board
    def PrintBoard(self,board):
        for i in range(20):
            for j in range(40):
                if(board[i][j]==1):
                    print("*",end="")
                elif(board[i][j]==0):
                    print(" ",end="")
                elif(board[i][j]==2):
                    print("x",end="")
            print("\n",end="")
                    


        
class GameEngiene:
    def __init__(self,board):
        self.board=board

    def Move():
        
            
def cls():
    os.system('cls')




    
screen=GameScreen("deneme")
board=screen.CreateBoard()
engiene=GameEngiene(board)
cls()
screen.PrintBoard(board)
time.sleep(0.5)
cls()
time.sleep(0.5)
screen.PrintBoard(board)

















