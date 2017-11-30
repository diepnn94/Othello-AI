# Ngoc Nguyen ID# 72114439 Project 4 Lab 3

import reversi_logics
import copy

def number_check(row_col: str)-> int:
    ''' Return a number that is in the range of 4 to 16 and is an even number.
    '''
    while True:
        try:
            number = int(input('Please enter the number of {}: '.format(row_col)))

            if (4 <= number and number <= 16) and number%2 == 0:
                return int(number)
            else:
                print('The number must be an even interger between 4 and 16.')
        except:
            print('The input is invalid. Please try again.')

            
def winning_method()-> str:
    
    '''Return a string that is either 'MOST' or 'LEAST; else prompt the user to try again.'''
    
    while True:
        user_input = input('Please specify a winning method (LEAST or MOST): ')
        choice = user_input.strip().upper()
        
        if choice == 'MOST' or choice.upper() == "LEAST":
            return choice.upper()
        else:
            print('The winning method is invalid. Please try again.')
            
        
def turn_check(description: str)->str:
    ''' Return a string that is either 'B' or 'W'; else prompt the user to try again.'''
    while True:
        try:
            turn = input('{} '.format(description))
            if turn.upper() == 'B' or turn.upper() == "W":
                return turn.upper()
            else:
                print('The turn entered above is invalid. Please choose either B (Black) or W( White).')
        except:
            print('The input entered above is not in the right format. Please try again.')
                     
def row_col_check(size: int, row_col: str)-> int:
    ''' Return an interger that is greater than zero and less than or equal the length of the gameboard'''
    while True:
        try:
            user_input = int(input('Please enter a {} number between 1 and {}: '.format(row_col,size)))
            if 0 < user_input and user_input <= size:
                return user_input
            else:
                print('The {} number is out of range. Please try again.'.format(row_col))
        except:
            print('The input entered above is not in the right format. Please try again.')

def move_check(gameboard: list, row: int, col: int)-> bool:
    ''' Return a True if the coordinate on the gameboard is empty; else return False'''
    if gameboard[row-1][col-1] != "B" and gameboard[row-1][col-1]!="W":
        return True
    

if __name__ == "__main__":

    ''' Run the program using the functions defined above and in reversi_logics module'''


    Row_Size = number_check('row')
    Col_Size = number_check('column')
    Win_method = winning_method()
    TOP_left = turn_check('Please specify the color (B or W) for the top left of the gameboard: ')
    first_turn = turn_check('Please enter the player turn (B or W) who wants to go first: ')

    print()
    gameboard_info = reversi_logics.Othello_Game_State(Row_Size,
                                                  Col_Size,
                                                  TOP_left,
                                                  first_turn)
    
    gameboard_check = reversi_logics.Othello_Game_State(Row_Size,
                                                  Col_Size,
                                                  TOP_left,
                                                  first_turn)

    gameboard = gameboard_info.gameboard()
    gameboard_checking = gameboard_check.gameboard()
    

    while True:
        checking_1= copy.deepcopy(gameboard_checking)
        checking_2= copy.deepcopy(gameboard_checking)
        checking_3= copy.deepcopy(gameboard_checking)
        checking_4= copy.deepcopy(gameboard_checking)
        checking_5= copy.deepcopy(gameboard_checking)
        print() 
        reversi_logics.print_gameboard(gameboard)
        print()
        print('\nThe player turn is '+ first_turn+'.')
        print('Current Game State:', reversi_logics.win_choice(gameboard, Win_method))

        
        First_player_check = reversi_logics.game_over(checking_1, first_turn)
        
        
        Second_player_check = reversi_logics.game_over(checking_2, reversi_logics.opposite_turn(first_turn))
        
        if First_player_check == True:
            first_turn = reversi_logics.opposite_turn(first_turn)
            print('\nThe other player cannnot make a move. The player turn is '+ first_turn+'.')
            
        if First_player_check == True and Second_player_check == True:
            print('The winner is {}.'.format(reversi_logics.win_choice(gameboard, Win_method)))
            break

        
            
        row_num = row_col_check(Row_Size, 'row')
        col_num = row_col_check(Col_Size, 'column')

        move_checking = move_check(gameboard, row_num, col_num)

        if move_checking == True:

            valid_move = reversi_logics.check_move(gameboard_checking, row_num, col_num, first_turn)
            if reversi_logics.flip_disc(valid_move, checking_3, row_num, col_num, first_turn)== []:
                
                print('\nThe move is invalid. Please try again.')
                
            elif gameboard == reversi_logics.flip_disc(valid_move, checking_4, row_num, col_num, first_turn):
                      
                print('\nThe move is invalid. Please try again.')
                
            else:
                
                gameboard = reversi_logics.flip_disc(valid_move, checking_5, row_num, col_num, first_turn)
                
                gameboard_checking = gameboard

                first_turn = reversi_logics.opposite_turn(first_turn)

        else:
            print('The move is invalid. Please try again.')
     
                  
        
















    

