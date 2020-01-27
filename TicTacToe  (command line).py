import time, sys 


class TicTacToe:
    

    board = [i for i in range (10)]

    def welcome(self):
        print ("This is a tic-tac-toe game.  The first player to go is X and the next is 0")
        time.sleep(0.5)
        print ("Good luck!")
        print()
    
    def printBoard(self):
        time.sleep(0.5)
        print (self.board[1], ' | ', self.board[2], ' | ', self.board[3])
        print('-' * 15)
        print (self.board[4], ' | ', self.board[5], ' | ', self.board[6])
        print('-' * 15)
        print (self.board[7], ' | ', self.board[8], ' | ', self.board[9])

    def player_pick(self):
         self.player_x = str(input('> Player X name: '))
         self.player_0 = str(input('> Player 0 name: '))

    def win_check(self, player):
        if  ((self.board[1]==self.board[2]==self.board[3]) or
             (self.board[4]==self.board[5]==self.board[6]) or
             (self.board[7]==self.board[8]==self.board[9]) or
             
             (self.board[1]==self.board[5]==self.board[9]) or
             (self.board[3]==self.board[5]==self.board[7]) or
             (self.board[2]==self.board[5]==self.board[8]) or

             (self.board[1]==self.board[4]==self.board[7]) or
             (self.board[3]==self.board[6]==self.board[9])):
                 print('{} won'.format(player))
                 print ('Game over!')
                 return True
                 

    def x_move(self):

        while True:
        
             try:
                    print()
                    print ("{}'s turn".format(self.player_x))
                    player_x_choice = int(input('> '))
                    if self.board[player_x_choice] == 'x' or self.board[player_x_choice] == '0':
                        print ('Invalid move!')
                        continue
                    elif self.board[player_x_choice] == 0:
                        print ('Choice out of range!')
                        continue
                    else:
                        self.board[player_x_choice] = "x"
                        self.printBoard()
                        break
             except IndexError:
                    print ("Choice out of range!")


           

    def zero_move(self):

        while True:

             try:
                    print()
                    print ("{}'s turn".format(self.player_0))
                    player_0_choice = int(input('> '))
                    if self.board[player_0_choice] == 'x' or self.board[player_0_choice] == '0':
                        print ('Invalid move!')
                        continue
                    elif self.board[player_0_choice] == 0:
                        print ('Choice out of range!')
                        continue
                    else:
                        self.board[player_0_choice] = "0"
                        self.printBoard()
                        break
             except IndexError:
                    print ("Choice out of range!")

    def play_again(self):
        print ("Play again? Press 'y' for yes and any other key for no.")
        player_answer = str(input("> "))
        if player_answer == 'y'.lower():
            self.main()
        else:
            sys.exit()
            
        


    def main(self):
        self.welcome()
        self.player_pick()
        self.printBoard()
        while True:
            self.x_move()
            if self.win_check(self.player_x):
                self.play_again()
            self.zero_move()
            if self.win_check(self.player_0):
                self.play_again()
            
                                      
t = TicTacToe()
t.main()
            
        
