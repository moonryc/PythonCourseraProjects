import random
import numpy


"""
X ALWAYS GOES FIRST
randomly play N random number of games
"""
#import numeric

def mc_trial(board,player):
    pass

def mc_update_scores(scores,board,player):
    pass

def get_best_move(board,scores):
    pass

def mc_move(board,player,trials):
    pass

class TrainAi:
    def __init__(self):
        self.board = [[1,1,1],
                        ["","",""],
                        ["","",""]]
        self.score_board=[[],[],[]]
        self.player = True
        self.in_play = True
        self.row_dict= {7:0,8:0,9:0,4:1,5:1,6:1,1:2,2:2,3:2}
        self.col_dict= {7:0,8:1,9:2,4:0,5:1,6:2,1:0,2:1,3:2}
        
    def __str__(self):
        """
        Prints Board
        """
        return str(self.board[0]) + "\n"+ str(self.board[1]) + "\n" + str(self.board[2])
    def reset_board(self):
        """
        Resets board for follow up game
        """
        self.board = [["","",""], ["","",""], ["","",""]]
        self.player = True
        self.in_play = True

    def get_board(self):
        return self.board

    def get_score(self):
        return self.score_board

    def win_check(self):
        """
        Checks if the game is won
        """
        #Test for Crosses
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] != "":
            if self.player == True:
                print("PLAYER WON")
                self.in_play= False
            else:
                print('AI WON')
                self.in_play= False
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] != "":
            if self.player == True:
                print("PLAYER WON")
                self.in_play= False
            else:
                print('AI WON')
                self.in_play= False
        
        #Test Regular Board
        for row in range(3):
            test_row = self.board[row]
            if test_row[0] == test_row[1] and test_row[1] == test_row[2] and test_row[2] != "":
                print (test_row)
                if self.player == True:
                    print("PLAYER WON")
                    self.in_play= False
                else:
                    print('AI WON')
                    self.in_play= False
        # Test Column
        transposed= self.transpose()
        for row in range(3):
            test_row = transposed[row]
            if test_row[0] == test_row[1] and test_row[1] == test_row[2] and test_row[2] != "":
                if self.player == True:
                    print("PLAYER WON")
                    self.in_play= False
                else:
                    print('AI WON')
                    self.in_play= False
        
        #Test for stalemate
        stalemate=[]
        for row in self.board:
            for value in row:
                stalemate.append(value)
        self.in_play =  "" in stalemate

    def transpose(self):
        """
        Transposed the rows into columns
        """
        transposed=[]
        transposed = list(zip(*self.board))
        return transposed

    def players_turn(self,location):
        """
        Sets up how to handel the player actions
        """

        placement = "X"

        if self.board[self.row_dict.get(location)][self.col_dict.get(location)] !="":
            self.board[self.row_dict.get(location)][self.col_dict.get(location)] = placement 
            self.player = False
        self.__str__()
        pass
    def computer_turn(self):
        """
        Sets up how to handel computer actions
        """

        test_location = "O"

        self.player= True
        pass

    def first_game(self):
        """
        Sets up how to handel the first game to train the AI
        """
        while self.in_play == True:
            if self.player==True:
                print("waiting")
                pass
            else:
                self.computer_turn()
                pass
            pass
    def follow_up_games(self):
        """
        How to handel follow up games
        """
        self.reset_board()
        while self.in_play == True:
            if self.player==True:
                pass
            else:
                get_best_move(self.board,self.score_board)
                pass
            pass



test = TrainAi()
test.win_check()
# test.column_check()
print(test)


"""
Pygame is below and is used as such
"""


#Pygame tools for VS testing below
import pygame

# initialising pygame
pygame.init()

window_width = 600
window_height = 700


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("2048 test")

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            running = False
        elif keys[pygame.K_r]:
            print('Reset')
        elif keys[pygame.K_KP7]:
            print('TOP LEFT')
            test.players_turn(7)
        elif keys[pygame.K_KP8]:
            print('TOP MID')
            test.players_turn(8)
        elif keys[pygame.K_KP9]:
            print('TOP RIGHT')
            test.players_turn(9)
        elif keys[pygame.K_KP4]:
            print('MID LEFT')
            test.players_turn(4)
        elif keys[pygame.K_KP5]:
            print('MID MID')
            test.players_turn(5)
        elif keys[pygame.K_KP6]:
            print('RIGHT MID')
            test.players_turn(6)
        elif keys[pygame.K_KP1]:
            print('BOT LEFT')
            test.players_turn(1)
        elif keys[pygame.K_KP2]:
            print('BOT MID')
            test.players_turn(2)
        elif keys[pygame.K_KP3]:
            print('BOT RIGHT')
            test.players_turn(3)
        # else:
        #     print(event)
            
pygame.quit()