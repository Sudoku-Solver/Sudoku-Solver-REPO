
from tkinter import *
import tkinter.messagebox
import time


root = Tk()                 # Initiate tkinter
root.geometry('275x283')    # Size of the screen


# Sudoku Solver class
class SolveSudoku():
    
    print ("Welcome to our AI Sudoku Solver made by Neysha M. Matos Torres, Diego Colon Davila and Kevin J. Bonet Guadalupe. Enjoy!")

    def __init__(self): # __init__
        self.allZero()
        self.startSolution()


    def allZero(self):          # All empty cells = 0 (validation)
        for i in range(9):
            for j in range(9):
                if Number[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    Number[i][j].set(0)


    def startSolution(self, i=0, j=0):      # Run the Backtracking algorithm (pseudoscope is in the final report)
        i,j = self.findNextCellToFill(i, j)

        if i == -1:
            return True
        for e in range(1,10):
            if self.itsValid(i,j,e):
                Number[i][j].set(e)
                if self.startSolution(i, j):
                    return True
                Number[i][j].set(0)
        return False


    def findNextCellToFill(self, i, j):     # Fill the nearest cell

        for x in range(i,9):
            for y in range(j,9):
                if Number[x][y].get() == '0':
                    return x,y

        for x in range(0,9):
            for y in range(0,9):
                if Number[x][y].get() == '0':
                    return x,y

        return -1,-1


    def itsValid(self, i, j, e):         # Check the Validity of Number[i][j]

        for x in range(9):
            if Number[i][x].get() == str(e):
                return False

        for x in range(9):
            if Number[x][j].get() == str(e):
                return False
  
        secTopX, secTopY = 3 *int((i/3)), 3 *int((j/3))
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if Number[x][y].get() == str(e):
                    return False
        
        return True
        



class Launch():     # Draw the grid
    
    def __init__(self, master):
        
        self.master = master
        master.title("AI Sudoku Puzzle Solver")

        font = ('Arial', 18)
        color = 'white'
        px, py = 0, 0

        self.__table = []
        for i in range(1,10):
            self.__table += [[0,0,0,0,0,0,0,0,0]]

        for i in range(0,9):
            for j in range(0,9):
                
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = '#71a3e3'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = '#71a3e3'
                else:
                    color = 'white'

                self.__table[i][j] = Entry(master, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'black',
                                          textvar = Number[i][j])
                self.__table[i][j].bind('<Motion>', self.correctGrid)
                self.__table[i][j].bind('<FocusIn>', self.correctGrid)
                self.__table[i][j].bind('<Button-1>', self.correctGrid)
                self.__table[i][j].grid(row=i, column=j)

        # Adding menu with options
        menu = Menu(master)
        master.config(menu = menu)

        file = Menu(menu)
        menu.add_cascade(label = 'Options', menu = file)
        file.add_command(label = 'Solve', command = self.solveInput)
        file.add_command(label = 'Clear', command = self.clearAll)

        # Welcome message box
        tkinter.messagebox.showinfo("AI Sudoku Puzzle Solver",  "Welcome to AI Sudoku Puzzle Solver made by Neysha M. Matos Torres, Diego Colon Davila and Kevin J. Bonet Guadalupe. \n\nHow to use: \n\n1. Add the sudoku you want to solve. \n2. Press \"Options\" then \"Solve\" to get your answer. \n3. Press \"Clear\" to do another puzzle.")


    def correctGrid(self, event):       # Check if inputs are incorrect
        for i in range(9):
            for j in range(9):
                if Number[i][j].get() == '':
                    continue
                if len(Number[i][j].get()) > 1 or Number[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    Number[i][j].set('')


    def clearAll(self):     # Clear the Grid
        for i in range(9):
            for j in range(9):
                Number[i][j].set('')


    
    def solveInput(self):       # Calls the class SolveSudoku
        t0 = time.time()        # Check the time it takes to solve the puzzle
        solution = SolveSudoku()
        t1 = time.time()        # Check the time it takes to solve the puzzle
        total = t1-t0           # Total time it takes to solve the puzzle

        print("Solve time: ",total)

        
        

# Global Matrix used to stored the numbers (don't delete)
Number = []
for i in range(1,10):
    Number += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        Number[i][j] = StringVar(root)

# Initiate program
app = Launch(root)
root.mainloop()
