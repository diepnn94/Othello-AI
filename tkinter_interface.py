# Ngoc Nguyen ID# 72114439 Project 5 Lab 3

import reversi_logics
import start_up_class
import board

if __name__ == '__main__':

    ''' Run the program using the function defined in the module imported above'''

    try:
    
        information = start_up_class.Start_up()
        information.start()
        row_num = information._row()
        col_num = information._col()
        top_left = information._top_left()
        winning_choice = information._winning_choice()
        first_player_turn = information._first_player_turn()
        
        
        gameboard = board.Reversi_Board(reversi_logics.Othello_Game_State(int(row_num),int(col_num),str(top_left),str(first_player_turn)), str(winning_choice))
        gameboard.start()

    except:
        pass

