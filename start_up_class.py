# Ngoc Nguyen ID# 72114439 Lab 3 Project 5

import tkinter

class message_box:
    def __init__(self):
        '''Initialize a toplevel window that deliver a message to the user when a condition is raised'''
        self._dialog_window = tkinter.Toplevel()
        message_label = tkinter.Label(
            master = self._dialog_window,
            text = 'One of the entries is not filled. Please try again.',
            font = ('Helvetica',15))
        message_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        got_it_button = tkinter.Button(master = self._dialog_window,
                                       text = 'Got It!',
                                       font = ('Helvetica',15),
                                       command = self._got_it_command)
        got_it_button.grid(row = 1, column =0, padx=10, pady=10)

    def _got_it_command(self)-> None:
        '''Destroy the toplevel window'''
        self._dialog_window.destroy()

    def show(self) -> None:
        '''Show the toplevel window and wait until the got_it_command is clicked'''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


class Start_up:
    def __init__(self):

        '''Initialize a option menu window that asks for the row and column number, top left, first player turn and winning option'''
        
        self._root_window = tkinter.Tk()
 

        self._greeting = tkinter.Label(self._root_window, text = 'Welcome to Othello Game!', font = ('Helvetica',20))
        self._greeting.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tkinter.N + tkinter.W + tkinter.E)
        self._root_window.rowconfigure(0, weight= 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._rows_string = tkinter.StringVar()
        self._cols_string = tkinter.StringVar()
        self._top_left_option = tkinter.StringVar()
        self._first_turn = tkinter.StringVar()
        self._winning_style = tkinter.StringVar()


        self._button1= tkinter.OptionMenu(self._root_window, self._rows_string, *('4', '6', '8', '10','12', '14','16'))
        self._button1_label = tkinter.Label(master = self._root_window, text = 'ROWS: ', font = ('Helvetica',15))
        self._button1_label.grid(row =1, column= 0,padx = 40, sticky = tkinter.E + tkinter.N)
        self._button1.grid(row =1, column = 1,padx = 20, sticky = tkinter.W + tkinter.N)
        self._root_window.rowconfigure(1, weight =1)
        self._root_window.columnconfigure(0,weight = 1)
        self._root_window.columnconfigure(1, weight = 1)

        self._button2= tkinter.OptionMenu(self._root_window, self._cols_string, *('4', '6', '8', '10','12', '14','16'))
        self._button2_label = tkinter.Label(master = self._root_window, text = 'COLUMNS: ', font = ('Helvetica',15))
        self._button2_label.grid(row =2, column= 0,padx = 40, sticky = tkinter.E + tkinter.N)
        self._button2.grid(row =2, column = 1,padx = 20, sticky = tkinter.W + tkinter.N)
        self._root_window.rowconfigure(2, weight =1)
        

        self._button3= tkinter.OptionMenu(self._root_window, self._top_left_option, *('B','W'))
        self._button3_label = tkinter.Label(master = self._root_window, text = 'TOP LEFT: ', font = ('Helvetica',15))
        self._button3_label.grid(row =3, column= 0,padx = 40, sticky = tkinter.E + tkinter.N)
        self._button3.grid(row =3, column = 1,padx = 20, sticky = tkinter.W + tkinter.N)
        self._root_window.rowconfigure(3, weight =1)
        

        self._button4= tkinter.OptionMenu(self._root_window, self._first_turn, *('B','W'))
        self._button4_label = tkinter.Label(master = self._root_window, text = 'FIRST PLAYER: ', font = ('Helvetica',15))
        self._button4_label.grid(row =4, column= 0,padx = 40, sticky = tkinter.E + tkinter.N)
        self._button4.grid(row =4, column = 1,padx = 20, sticky = tkinter.W + tkinter.N)
        self._root_window.rowconfigure(4, weight =1)
        

        self._button5= tkinter.OptionMenu(self._root_window, self._winning_style, *('MOST','LEAST'))
        self._button5_label = tkinter.Label(master = self._root_window, text = 'WINNING STYLE: ', font = ('Helvetica',15))
        self._button5_label.grid(row =5, column= 0,padx = 40, sticky = tkinter.E + tkinter.N)
        self._button5.grid(row =5, column = 1,padx = 20, sticky = tkinter.W + tkinter.N)
        self._root_window.rowconfigure(5, weight =1)
        

        button_frame = tkinter.Frame(master = self._root_window)

        button_frame.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10)

        start_button= tkinter.Button(master = button_frame, text = 'START', font = ('Helvetica',15), command = self._start_button)
        start_button.grid(row = 0, column = 0, padx=10, pady = 10, sticky = tkinter.E + tkinter.S + tkinter.N)
        

        self._start_click= False
        
    def _started_clicked(self)-> bool:
        '''Return a boolean if the START button is clicked'''
        return self._start_click

    def _start_button(self)-> None:
        ''' When the START button is clicked, check if all entries are filled, if one of the entries is not filled, raise the message_box window,
            when all entries are filled, store the filled entries and destroy the window'''
        self._started_clicked = True
        self._row_number = self._rows_string.get()
        self._col_number = self._cols_string.get()
        self._top_left_corner = self._top_left_option.get()
        self._first_player_option = self._first_turn.get()
        self._winning_option = self._winning_style.get()


        if '' in [self._row_number,
                     self._col_number,
                     self._top_left_corner,
                     self._first_player_option,
                     self._winning_option]:
    
                message = message_box()
                message.show()
        else:    
            self._root_window.destroy()
                

        
    def _row(self)-> str:
        '''Return the row number entered in the option menu window'''
        return self._row_number
    
    def _col(self)-> str:
        '''Return the column number entered in the option menu window'''
        return self._col_number
    
    def _top_left(self)->str:
        '''Return the top left player entered in the option menu window'''
        return self._top_left_corner
    
    def _first_player_turn(self)->str:
        '''Return the first player entered in the option menu window'''
        return self._first_player_option
    
    def _winning_choice(self)-> str:
        '''Return the winning choice entered in the option menu window'''
        return self._winning_option

    
        
        
    def start(self):
        self._root_window.mainloop()

    
