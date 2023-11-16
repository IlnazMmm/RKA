from tkinter import *

# create the main window
root = Tk()
root.title("Chess")

# initialize the main game window
def initialize():
    global main_frame
    main_frame = Frame(root)
    main_frame.pack()
class ChessPiece:
    def __init__(self, color, type, row, column):
        self.color = color
        self.type = type
        self.row = row
        self.column = column

    def create_chessboard():
        for i in range(8):
            for j in range(8):
                square = Label(main_frame, bg='white', width=4, height=2)
                square.grid(row=i, column=j)

                if (i + j) % 2 == 0:
                    square.config(bg='white')
                else:
                    square.config(bg='gray')
# start the game
initialize()
root.mainloop()