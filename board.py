# Ngoc Nguyen ID# 72114439 Project 5 Lab 3


import tkinter
import reversi_logics
import copy
import reversi_interface



class Reversi_Board:
        
    def __init__(self, state: reversi_logics.Othello_Game_State, winning_choice: str):
        ''' Initializng the gameboard and display the score and player turn'''
        self._winning_choice = winning_choice


        self._state = state
        self._gameboard = self._state.gameboard()
        self._checking_gameboard = self._state.gameboard()
        self._count = reversi_logics.count(self._gameboard)

        self._row = self._state._ROW
        self._col = self._state._COL
        self._turn = self._state._turn
        self._root_window = tkinter.Tk()

        self._board_canvas = tkinter.Canvas(
            master = self._root_window,
            width = 400, height = 400,
            background = 'pale green')

        self._title = tkinter.Label(master = self._root_window, text= "Let's Play!", font = ('Helvetica',20))

        self._score = tkinter.Label(master = self._root_window, text= 'Black Score: ' + str(self._count[0]) + 
                                   '\nWhite Score: ' + str(self._count[1]), font = ('Helvetica',15))

        self._turn_label = tkinter.Label(master = self._root_window, text= 'Player Turn: ' + self._turn, font = ('Helvetica',15))
        

        self._board_canvas.grid(row=1, column = 0,columnspan = 2, padx = 20, pady=0,
                                sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._title.grid(row=0, column = 0,columnspan = 2, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._turn_label.grid(row=2, column =0, sticky = tkinter.S + tkinter.W + tkinter.N)

        self._score.grid(row=2, column = 1, sticky = tkinter.S + tkinter.W+ tkinter.N)


        self._board_canvas.bind('<Configure>', self._canvas_resized)
        self._board_canvas.bind('<Button-1>', self._clicked)
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._root_window.rowconfigure(0, weight=1)
        self._root_window.rowconfigure(2, weight=1)
        self._root_window.rowconfigure(1, weight = 5)

    
        
        
    def _clicked(self, event: tkinter.Event)-> None:
        ''' When the user makes a click, convert the pixel location of the click into the index of the gameboard
            and check whether that click is valid. If it is valid, update the gameboard, else, do nothing. When one player
            cannot make a valid turn, switch to the opposite player. When the game is over, display the winner and the score.'''
        
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()
        
        column_sep = canvas_width/self._col
        row_sep = canvas_height/self._row

        x = 0
        y=0
        row = 0
        col = 0
    

        for i in range(1,self._row+1):
            x = i* row_sep
            if event.y < x:
                row = i
                break

        for e in range(1,self._col+1):
            y = e* column_sep
            if event.x < y:
                col = e
                break
        
        checking_1= copy.deepcopy(self._checking_gameboard)
        checking_2= copy.deepcopy(self._checking_gameboard)
        checking_3= copy.deepcopy(self._checking_gameboard)
        checking_4= copy.deepcopy(self._checking_gameboard)
        checking_5= copy.deepcopy(self._checking_gameboard)
        


        move_checking = reversi_interface.move_check(self._gameboard, row, col)
        

        if move_checking == True:

            valid_move = reversi_logics.check_move(self._checking_gameboard, row, col, self._turn)
            if reversi_logics.flip_disc(valid_move, checking_3, row, col, self._turn)== []:
                
                pass
                
            elif self._gameboard == reversi_logics.flip_disc(valid_move, checking_4, row, col, self._turn):
                      
                pass
                
            else:
                
                self._gameboard = reversi_logics.flip_disc(valid_move, checking_5, row, col, self._turn)
                
                self._checking_gameboard = self._gameboard

                self._turn = reversi_logics.opposite_turn(self._turn)
                self._turn_label.config(text = "Player Turn: " + self._turn)
                self._count = reversi_logics.count(self._gameboard)
                
                self._score.config(text = 'Black Score: ' + str(self._count[0]) + 
                                           '\nWhite Score: ' + str(self._count[1]))

        else:
            pass

        self._draw_disc()

        First_player_check = reversi_logics.game_over(checking_1, self._turn)
        
        
        Second_player_check = reversi_logics.game_over(checking_2, reversi_logics.opposite_turn(self._turn))
        
        if First_player_check == True:
            self._turn = reversi_logics.opposite_turn(self._turn)
            self._turn_label.config(text= "Player Turn: " + self._turn)
        
            
        if First_player_check == True and Second_player_check == True:
            self._title.config(text= "Game Over!", font = ('Helvetica',30))
            self._title.grid(row=0, column = 0,columnspan = 2,padx = 30, pady = 30, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            
            self._turn_label.config(text = 'The Winner: ' + reversi_logics.win_choice(self._gameboard, self._winning_choice), font = ('Helvetica',15))
            self._turn_label.grid(row=2, column =0, padx = 20, pady = 20, sticky = tkinter.S + tkinter.W + tkinter.N )

            self._score.grid(row=2, column = 1, padx = 30, pady = 30, sticky = tkinter.S + tkinter.W+ tkinter.N)
            
            self._board_canvas.destroy()

        

        
    def _draw_disc(self)-> None:
        '''Check the gameboard and draw the ovals according to the position and color inside the list'''

        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()
        column_sep = canvas_width/self._col
        row_sep = canvas_height/self._row
        for row in range(len(self._gameboard)):
            for col in range(len(self._gameboard[row])):
                if self._gameboard[row][col] == "W":
                    self._board_canvas.create_oval(column_sep*col,row*row_sep,column_sep*(col+1),row_sep*(row+1), fill = "white")
                if self._gameboard[row][col] == 'B':
                    self._board_canvas.create_oval(column_sep*col,row*row_sep,column_sep*(col+1),row_sep*(row+1), fill = "black")


        
        
    def _canvas_resized(self, event: tkinter.Event)-> None:
        ''' When the canvas is resized, delete everything and draw a new canvas based on the new area'''
        self._draw_grid_col()
        self._draw_grid_row()
        self._draw_disc()


    
    

    def _draw_grid_col(self)-> None:
        ''' Draw the column according to the area of the gameboard'''
        self._board_canvas.delete(tkinter.ALL)
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()
        for item in range(self._col):
            self._board_canvas.create_line(((canvas_width/self._col)*item,0),((canvas_width/self._col)*item, canvas_height),
                                            fill = 'black')

    def _draw_grid_row(self)-> None:
        ''' Draw the row according to the area of the gameboard'''
        canvas_height = self._board_canvas.winfo_height()
        canvas_width = self._board_canvas.winfo_width()
        for item in range(self._row):
            self._board_canvas.create_line((0,(canvas_height/self._row)*item),(canvas_width,(canvas_height/self._row)*item),
                                       fill = 'black')

    

    def start(self)->None:
        ''' Start the canvas'''
        self._root_window.mainloop()


