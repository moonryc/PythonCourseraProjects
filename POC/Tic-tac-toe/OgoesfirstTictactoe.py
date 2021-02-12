import random

"""
Tic-Tac-Toe pygame that is mine/ best version so far uses pygame but PGGAME is kinda broken ATM
"""

user_input=""

class tictactoeboard:
    """
    tic - tac - toe - board
    """
    def __init__(self):
        self.board = []
        self.score = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = False
        self.in_play= True

    def __str__(self):
        return str(self.board[0])+"\n"+str(self.board[1])+"\n"+str(self.board[2])
    def reset(self):
        """
        Resets board
        """
        self.board = [["","",""],["","",""],["","",""]]
    def start_game(self):
        """
        Sets up a new game
        """
        self.reset()
        self.player = False
        print("------------------------------"+"\n"+
                "Use numpad to play"+"\n"+"PRESS 'R' TO RESET THE BOARD"+
                "\n"+"PRESS A TO RESET THE AI'S BRAIN"+
                "\n""------------------------------")
        #print(self)
        self.game()
    def get_player(self):
        """
        Tells you what players turn it is if you get lost
        """
        if self.player == True:
            print("Human")
        elif self.player == False:
            print("AI")
    def get_score(self):
        print(self.score)
    def check_win(self, board):
        """
        Checks if the game is won
        """
        #Test for Crosses
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] != "":
            if self.player == True:
                self.score_update("PLAYER_WIN")
                print("player win")
                
            else:
                self.score_update("AI_WIN")
                print("ai win")
                
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] != "":
            if self.player == True:
                self.score_update("PLAYER_WIN")
                print("player win")
                
            else:
                self.score_update("AI_WIN")
                print("ai win")
                
        
        #Test Regular Board
        for row in range(3):
            test_row = self.board[row]
            if test_row[0] == test_row[1] and test_row[1] == test_row[2] and test_row[2] != "":
                print (test_row)
                if self.player == True:
                    self.score_update("PLAYER_WIN")
                    print("player win")
                    
                else:
                    self.score_update("AI_WIN")
                    print("ai win")
                    
        # Test Column
        transposed= self.transpose()
        for row in range(3):
            test_row = transposed[row]
            if test_row[0] == test_row[1] and test_row[1] == test_row[2] and test_row[2] != "":
                if self.player == True:
                    self.score_update("PLAYER_WIN")
                    
                else:
                    self.score_update("AI_WIN")
                    
        
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
    def score_update(self,player_to_update):
        
        if player_to_update == "AI_WIN":
            #add for Xs
            for row in range(3):
                for col in range(3):
                    if self.board[row][col]=="X":
                        self.score[row][col]+=1
                    elif self.board[row][col]=="O":
                        self.score[row][col]-=1
        
        if player_to_update == "PLAYER_WIN":
            #add for Os
            for row in range(3):
                for col in range(3):
                    if self.board[row][col]=="O":
                        self.score[row][col]+=1
                    elif self.board[row][col]=="X":
                        self.score[row][col]-=1

        pass
    def get_empty_space(self):
        empty_loc = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    empty_loc.append([row,col])
        return empty_loc
    def get_best_score(self,empty_loc):
        """
        Returns the highest scored location for the AI
        empty_loc is a list of locations that are empty/ playable
        """
        row = 0
        col = 0
        highest_score = -1000
        final_location =[]
        for location in empty_loc:
            row, col = location
            if highest_score < self.score[row][col]:
                highest_score = self.score[row][col]
                final_location=[row,col]         
        return final_location
    def ai_turn(self):
        """
        AI's brain/ how it chooses
        """
        row, col = self.get_best_score(self.get_empty_space())
        self.board[row][col] = "X"
        print(self)
        self.player=True

    def players_turn(self,location):
        if location == 7:
            self.board[0][0] = "O"
        elif location == 8:
            self.board[0][1] = "O"
        elif location == 9:
            self.board[0][2] = "O"
        elif location == 4:
            self.board[1][0] = "O"
        elif location == 5:
            self.board[1][1] = "O"
        elif location == 6:
            self.board[1][2] = "O"
        elif location == 1:
            self.board[2][0] = "O"
        elif location == 2:
            self.board[2][1] = "O"
        elif location == 3:
            self.board[2][2] = "O"
        self.player=False
    def game(self):
        global user_input
        while True:
            if self.player==False:
                self.ai_turn()
            else:
                user_input = int(input("Enter location: "))
                self.players_turn(user_input)

                

test=tictactoeboard()
test.start_game()
"""
    ########################################################################
    import pygame

    # initialising pygame
    pygame.init()
    window_width = 600
    window_height = 700
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("TTT test")

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
    #######################################################################
"""