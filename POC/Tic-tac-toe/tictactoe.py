"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board,player):
    pass

def mc_update_scores(scores,board,player):
    pass

def get_best_move(board,scores):
    pass

def mc_move(board,player,trials):
    pass


game_board=[[],[],[]]
score_board=[[0,0,0],[0,0,0],[0,0,0]]
#mc_move(game_board,,NTRIALS)
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
import numpy

test = [[7,8,9],[4,5,6],[1,2,3]]
for j in range(3):
    for i in test[j]:
        print(i)