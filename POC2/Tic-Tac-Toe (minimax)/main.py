"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import random

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

    #base case/ if the game is running
    if board.check_win() == None:
        score_move=[]
        for empty_cells in board.get_empty_squares():
            clone_board = board.clone()
            clone_board.move(empty_cells[0],empty_cells[1], player)
            score = mm_move(clone_board,provided.switch_player(player))[0]

            if score == 1 and player == provided.PLAYERX:
                return (1, empty_cells)
            elif score == -1 and player == provided.PLAYERO:
                return (-1, empty_cells)

            score_move.append((score, empty_cells))
        player_x_move = max(score_move)
        player_o_move = min(score_move)

        if player == provided.PLAYERO:
            return player_o_move
        else:
            return player_x_move
    else:
        return SCORES[board.check_win()], (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
