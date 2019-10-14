# Tic Tac Toe game
# Two players
# Same machine

from tkinter import *
from tkinter import messagebox


class TicTacToe:

    # Function assigns either x or 0 depending on whose turn it is
    # Add a win check after each button press
    def player_press(self,button):
        if self.turn_check:
            button.config(text="x",bg="red")
            button.config(state=DISABLED)
            self.turn_check = False
            self.win_check()
        else:
            button.config(text="0",bg="blue")
            button.config(state=DISABLED)
            self.turn_check = True
            self.win_check()

    # Function checks whether there's a winner
    def win_check(self):
        if  (self.button_1["text"]=="x" and self.button_2["text"]=="x" and self.button_3["text"]=="x" or
             self.button_4["text"]=="x" and self.button_5["text"]=="x" and self.button_6["text"]=="x" or
             self.button_7["text"]=="x" and self.button_8["text"]=="x" and self.button_9["text"]=="x" or
             self.button_1["text"]=="x" and self.button_5["text"]=="x" and self.button_9["text"]=="x" or
             self.button_1["text"]=="x" and self.button_4["text"]=="x" and self.button_7["text"]=="x" or
             self.button_3["text"]=="x" and self.button_6["text"]=="x" and self.button_9["text"]=="x" or
             self.button_2["text"]=="x" and self.button_5["text"]=="x" and self.button_8["text"]=="x" or
             self.button_7["text"]=="x" and self.button_5["text"]=="x" and self.button_3["text"]=="x"):
             self.disableButtons()
             messagebox.showinfo("Victory for X", "X wins!")

        elif (self.button_1["text"]=="0" and self.button_2["text"]=="0" and self.button_3["text"]=="0" or
              self.button_4["text"]=="0" and self.button_5["text"]=="0" and self.button_6["text"]=="0" or
              self.button_7["text"]=="0" and self.button_8["text"]=="0" and self.button_9["text"]=="0" or
              self.button_1["text"]=="0" and self.button_5["text"]=="0" and self.button_9["text"]=="0" or
              self.button_1["text"]=="0" and self.button_4["text"]=="0" and self.button_7["text"]=="0" or
              self.button_3["text"]=="0" and self.button_6["text"]=="0" and self.button_9["text"]=="0" or
              self.button_2["text"]=="0" and self.button_5["text"]=="0" and self.button_8["text"]=="0" or
              self.button_7["text"]=="0" and self.button_5["text"]=="0" and self.button_3["text"]=="0"):
              self.disableButtons()
              messagebox.showinfo("Victory for 0", "0 wins!")

    # Function to disable all buttons in case of a win
    def disableButtons(self):
        self.button_1.config(state=DISABLED)
        self.button_2.config(state=DISABLED)
        self.button_3.config(state=DISABLED)
        self.button_4.config(state=DISABLED)
        self.button_5.config(state=DISABLED)
        self.button_6.config(state=DISABLED)
        self.button_7.config(state=DISABLED)
        self.button_8.config(state=DISABLED)
        self.button_9.config(state=DISABLED)

    def __init__(self, master):

        # Variable to check player turn
        self.turn_check = True

        # Create window settings
        master.title("Tic Tac Toe")
        master.resizable(width=False, height=False)
        master.geometry("242x258")

        # Create buttons and tie them to the player_press function
        self.button_1=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda: self.player_press(self.button_1))
        self.button_2=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_2))
        self.button_3=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_3))
        self.button_4=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_4))
        self.button_5=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_5))
        self.button_6=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_6))
        self.button_7=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_7))
        self.button_8=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_8))
        self.button_9=Button(master, text="", bg="yellow", fg="black", width=10, height=5, command=lambda :self.player_press(self.button_9))

        # Position buttons on the grid
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)


# Initialize the game
root=Tk()
my_game=TicTacToe(root)
root.mainloop()

