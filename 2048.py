from tkinter import Frame,Label,CENTER

import logic
import constant as c

class Game2048(Frame):
    def __init__(self):
        #this will create frame close minimize buttons
        Frame.__init__(self)
        # this will make look entire frame as grid
        self.grid()
        # this will give frame title or its application name
        self.master.title('2048')
        # this will bind key to key_down functionn
        #if any key will be pressed it will go to key down function
        self.master.bind('<Key>',self.key_down)
        self.commands= {c.KEYS_DOWN: logic.move_down,c.KEYS_LEFT:logic.move_left,
                        c.KEYS_RIGHT: logic.move_right, c.KEYS_UP:logic.move_up}
        self.grid_cells=[]
        # initalize grid-> adding widget to grid
        self.init_grid()
        #it will add two new 2's in your matrix
        self.init_matrix()
        # this will change background of grid, colors of text,font of text
        # it will changes the Ui
        
        self.upgrade_grid_cells()

        #It will runs your program
        self.mainloop()


    def init_grid(self):
        background= Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                #this will create another frame inside background
                cell=Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,width=c.SIZE/c.GRID_LEN,height=
                           c.SIZE/c.GRID_LEN)
                # this will  make each chell ie 4 cell in a single row
                #into individual grid

                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)

                #inside each grid we for label it is basically text field

                t=Label(master=cell,text='',bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,
                        height=2)
                
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row )





    def init_matrix(self):
        # this willl create matrix which define logic.py
        self.matrix=logic.start_game()
        logic.add_new_2(self.matrix)
        logic.add_new_2(self.matrix )

    def upgrade_grid_cells(self):
        # this function changes colour of occupied and empty cell in each frame

        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):

                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text='',bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],
                                                    fg= c.CELL_COLOR_DICT[new_number])
        

        # it will wait until all color changed
        self.update_idletasks()


    def key_down(self,event):
        # a='abc'
        # repr(a)---> will print  'abc' not abc

        key=repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                logic.add_new_2(self.matrix)
                self.upgrade_grid_cells()
                changed=False
            if logic.get_current_state(self.matrix)=='WON':
                self.grid_cells[1][1].configure(text='You',bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text='Win!',bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            if logic.get_current_state(self.matrix)=='LOST':
                self.grid_cells[1][1].configure(text='You',bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text='Lose!',bg=c.BACKGROUND_COLOR_CELL_EMPTY)



gamegrid=Game2048()