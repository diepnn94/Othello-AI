# Ngoc Nguyen ID# 72114439 Project 4 Lab 3

import copy

class Othello_Game_State:
    def __init__(self, ROW:int, COL:int, topLeft:'str', turn: 'str'):
        ''' Initializes the gameboard based on the row and column number, top-left disc and the first player turn.'''
        
        self._board = []
        self._COL = COL
        self._ROW= ROW
        self._topLeft= topLeft
        self._turn= turn
        
        for row in range(self._ROW):
            self._board.append([])
            
        for col in range(self._COL):
            for item in range(len(self._board)):
                self._board[item].append(' ')
                
        if self._topLeft== "B":
            
            self._board[int((self._ROW)/2)-1][int((self._COL)/2)-1]="B"
            self._board[int((self._ROW)/2)][int((self._COL)/2)]="B"
            self._board[int((self._ROW)/2)-1][int((self._COL)/2)]="W"
            self._board[int((self._ROW)/2)][int((self._COL)/2)-1]="W"
        else:
            self._board[int((self._ROW)/2)-1][int((self._COL)/2)-1]="W"
            self._board[int((self._ROW)/2)][int((self._COL)/2)]="W"
            self._board[int((self._ROW)/2)-1][int((self._COL)/2)]="B"
            self._board[int((self._ROW)/2)][int((self._COL)/2)-1]="B"
    
    def gameboard(self):
        return self._board

class TOP:

    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''
        
       
        try:
            for row_num in range(1,row):
                
                if self._gameboard[row - row_num - 1][col-1]== opposite_turn(self._turn):
                    pass
                    
                elif self._gameboard[row-row_num-1][col-1] == self._turn:
                    self._gameboard[row-row_num-1][col-1]= self._turn
                    

                    for item in range(row-row_num -1, row):
                        self._gameboard[item][col-1]= self._turn

                    return self._gameboard
                elif self._gameboard[row-row_num-1][col-1]== ' ':
                    return self._gameboard
            return self._gameboard
        except:
            
            return self._gameboard




class BOTTOM:

    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''
        

        try:
            
            for row_num in range(1,(len(self._gameboard)+1)- row):
                
                if self._gameboard[row + row_num-1][col-1]== opposite_turn(self._turn):
                    pass
        
                    
                elif self._gameboard[row + row_num - 1][col-1] == self._turn:
                    self._gameboard[row-1][col-1]= self._turn

                    for item in range(row , row + row_num -1):
                        self._gameboard[item][col-1] = self._turn
                    return self._gameboard
                
                elif self._gameboard[row + row_num -1][col-1]== ' ':
                    return self._gameboard
            return self._gameboard
        
        except:
            
            return self._gameboard


    
class RIGHT:

    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''

        len_col = 0

        for ROW in self._gameboard:
            len_col = len(ROW)
            
        try:
        
            for col_num in range(1,len_col - col+1):
                
                if self._gameboard[row -1 ][col_num + col -1] == opposite_turn(self._turn):
                    pass
                    
                elif self._gameboard[row - 1][col_num + col -1] == self._turn:
                    self._gameboard[row-1][col-1]= self._turn

                    for item in range(col, col_num + col -1):
                        self._gameboard[row-1][item]= self._turn
                    return self._gameboard
                
                elif self._gameboard[row-1][col_num + col -1]== ' ':
                    
                    return self._gameboard
                
            return self._gameboard
        except:
            return self._gameboard
        
        

class LEFT:
    
    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''
        
        try:
    
            for col_num in range(1,col):
                
                if self._gameboard[row -1 ][col - col_num-1] == opposite_turn(self._turn):
                    pass
                    
                elif self._gameboard[row - 1][col- col_num-1 ] == self._turn:
                    
                    self._gameboard[row-1][col-1]= self._turn

                    for item in range(col - col_num-1, col):
                        self._gameboard[row-1][item]= self._turn
                    return self._gameboard
                
                elif self._gameboard[row-1][col - col_num-1]== ' ':
                    
                    return self._gameboard
            return self._gameboard
        
        except:
            return self._gameboard

class TOP_LEFT:

    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''

        
        try:


            for row_col in range(1, min(row, col)):
                
                if self._gameboard[row - row_col -1 ][col - row_col-1] == opposite_turn(self._turn):
                    pass
                        
                    
                elif self._gameboard[row - row_col - 1][col- row_col-1 ] == self._turn:
                    
                    self._gameboard[row-1][col-1]= self._turn

                    for item in range(1, min(row, col)- min(row-row_col-1, col- row_col -1)):
                        self._gameboard[row -1 - item][col -1 - item]= self._turn
                    return self._gameboard
                
                elif self._gameboard[row-row_col -1][col - row_col -1]== ' ':
                    return self._gameboard
            return self._gameboard
        except:
            return self._gameboard

class TOP_RIGHT:

    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''

        
        try:

            for row_col in range(1, max(row, col)):
                
                if self._gameboard[row - row_col -1 ][col + row_col-1] == opposite_turn(self._turn):
                    pass       
                    
                elif self._gameboard[row - row_col - 1][col+ row_col-1 ] == self._turn:
                    
                    self._gameboard[row-1][col-1]= self._turn

                    for item in range(1, max(row, col)- min(row-row_col-1, col+ row_col -1)):
                        self._gameboard[row - 1 - item][col -1 + item]= self._turn
                    return self._gameboard
                
                elif self._gameboard[row-row_col -1][col + row_col -1]== ' ':
                    return self._gameboard
            return self._gameboard
        except:
            return self._gameboard



class BOTTOM_LEFT:

    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''

        
        try:

            for row_col in range(1, max(row, col)):
                
                if self._gameboard[row + row_col -1 ][col - row_col-1] == opposite_turn(self._turn):
                    pass       
                    
                elif self._gameboard[row + row_col - 1][col- row_col-1 ] == self._turn:
                    
                    self._gameboard[row-1][col-1]= self._turn

                    for item in range(1, max(row, col)- min(row+row_col-1, col- row_col -1)):
                        self._gameboard[row - 1 + item][col -1 - item]= self._turn
                    return self._gameboard
                
                elif self._gameboard[row + row_col -1][col - row_col -1]== ' ':
                    return self._gameboard
            return self._gameboard
        except:
            return self._gameboard
    
class BOTTOM_RIGHT:
    
    def __init__(self, gameboard: list, turn: str):
        self._gameboard = gameboard
        self._turn = turn
        
    def flip(self,row: int, col: int)-> list:
        ''' Return an updated gameboard if the row and col are valid inputs; else return the original gameboard.'''
        row_size = 0
        col_size = 0

        for ROW in self._gameboard:
            row_size = len(ROW)
            for COL in self._gameboard:
                col_size = len(COL)

        
        try:

            for row_col in range(1, min(row_size, col_size)):
                
                if self._gameboard[row + row_col -1 ][col + row_col-1] == opposite_turn(self._turn):
                    pass       
                    
                elif self._gameboard[row + row_col - 1][col + row_col-1 ] == self._turn:
                    
                    self._gameboard[row-1][col-1]= self._turn

                    for item in range(1, max(row+row_col, col+ row_col)- max(row, col)):
                        self._gameboard[row - 1 + item][col -1 + item]= self._turn
                    return self._gameboard
                
                elif self._gameboard[row + row_col -1][col + row_col -1]== ' ':
                    return self._gameboard
            return self._gameboard
        except:
            return self._gameboard

def flip_disc(moves: ['move'], gameboard: list, row: int, col: int, turn: str)-> list:
    ''' Return an updated gameboard in all direction if the row and col number are valid; else return the original gameboard.'''

    new_gameboard=[]

    for move in moves:
        
        if move == "TOP":
            item = TOP(gameboard, turn)
            
        if move == "BOTTOM":
            item = BOTTOM(gameboard, turn)
            
        if move == "RIGHT":
            item = RIGHT(gameboard, turn)
            
        if move == "LEFT":
            item = LEFT(gameboard, turn)
            
        if move == "BOTTOM_LEFT":
            item = BOTTOM_LEFT(gameboard, turn)
            
        if move == "BOTTOM_RIGHT":
            item = BOTTOM_RIGHT(gameboard, turn)
            
        if move == "TOP_RIGHT":
            item = TOP_RIGHT(gameboard, turn)
            
        if move == "TOP_LEFT":
            item = TOP_LEFT(gameboard, turn)
            
        new_gameboard = item.flip(row, col)
        
    return new_gameboard

        
        
def count(gameboard: list)-> tuple:
    ''' Return a tuple that contain the number of white and black player in the gameboard.'''
    
    Black_total=0
    White_total=0

    for row in gameboard:
        for column in row:
            if column=="B":
                Black_total+=1
            elif column=="W":
                White_total+=1
                
    return (Black_total, White_total)      

def win_choice(gameboard: list, choice: str)-> str:
    '''Return a string that represents the winner of the gameboard; the winner is chosen depends how the winning method is defined, either
       with most discs or least discs on the gameboard.   
    '''  
    
    winner = None
    total= count(gameboard)
    if choice == 'MOST':
        if total[0]> total[1]:
            winner = "Black"
        elif total[0] < total[1]:
            winner = "White"

        else:
            winner='Tie'
            
    elif choice == "LEAST":
        if total[0]< total[1]:
            winner = "Black"
        elif total[0]> total[1]:
            winner= "White"
        else:
            winner= "Tie"
    return winner
        
    

def opposite_turn (turn: str)-> str:
    '''Return a string that is either B or W, if the input is B, then the function return W and vice versa.
    '''
    if turn == 'B':
        return 'W'
    else:
        return 'B'

def check_move( gameboard: list, row_num: int, column_num: int, turn: str) -> list:
    ''' Return a list of direction that contains all possible directions (if that direction have a disc that is opposite to the
        turn) of the given row and column'''
    
    ROW= row_num-1
    COL= column_num-1
    valid_move=[]
    
    try:
        if gameboard[ROW][COL+1]== opposite_turn(turn):
            valid_move.append('RIGHT')
    except:
        pass
    
    try:
        if gameboard[ROW+1][COL+1]== opposite_turn(turn):
            valid_move.append('BOTTOM_RIGHT')
    except:
        pass
        
    try:
        if gameboard[ROW+1][COL]== opposite_turn(turn):
            valid_move.append('BOTTOM')
    except:
        pass
    
    try:
        
        if gameboard[ROW+1][COL-1]== opposite_turn(turn):
            valid_move.append('BOTTOM_LEFT')
    except: pass

    try:
    
        if gameboard[ROW][COL-1]== opposite_turn(turn):
            valid_move.append('LEFT')
    except:
        pass

    try:
        
        if gameboard[ROW-1][COL-1]== opposite_turn(turn):
            valid_move.append('TOP_LEFT')
    except:
        pass

    try:
                          
        if gameboard[ROW-1][COL]== opposite_turn(turn):
            valid_move.append('TOP')
    except:
        pass

    try:
        
        if gameboard[ROW-1][COL+1]== opposite_turn(turn):
            valid_move.append('TOP_RIGHT')
    except:
        pass
    
    return valid_move





def game_over(gameboard: list, turn: str)-> bool:
    ''' Return True if there is no valid move for the given turn; else, return False'''

    possible_moves = []
    valid_move = []
    row_col=[]
    new_gameboard = []
    gameboard_checking = copy.deepcopy(gameboard)
    
    for row in range(len(gameboard)):
        for col in range(len(gameboard[row])):
            if gameboard[row][col]== ' ':
                possible_moves.append((row, col))

    for move in possible_moves:
        if check_move(gameboard, move[0]+1,move[1]+1,turn)!= []:
            valid_move.append((check_move(gameboard, move[0]+1,move[1]+1,turn), move[0]+1,move[1]+1))
    
    for item in valid_move:
        
        new_gameboard.append((flip_disc(item[0], copy.deepcopy(gameboard), item[1], item[2], turn)))

        
    for valid_flip in new_gameboard:
        if valid_flip != gameboard:
            return False
    return True
            
        
    
    
def print_gameboard(gameboard: list)->None:
    '''Print the gameboard with row numbers and column numbers starting from 1 to the end. For each empty space, it's represented by '.')
    '''

    try:
    
        print('  ', end=' ')
        
        for col in range(len(gameboard[0])):
                
                
            if col+1>9:
                print(col+1, end=' ')
            else:
            
                print(col+1, end='  ')     
        print()
        
        for row in range(len(gameboard)):
            
            if row+1>9:
                print(row+1, end='')
            else:
                print(row+1, end=' ')
            for column in range(len(gameboard[row])):

                if gameboard[row][column]== ' ':
                    print(' ' + '.', end=' ')
                else:
                    
                    print(' ' + (gameboard[row][column]), end=' ')
            print()
    except:
        pass



    

        
    
    
    
                
        
        
