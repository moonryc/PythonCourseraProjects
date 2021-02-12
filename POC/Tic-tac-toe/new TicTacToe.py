import random
import poc_ttt_provided as provided
"""
Tic-Tac-Toe pygame that is mine/ best version so far
"""

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 300         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    

def mc_trial(board,player):
    curr_player = player
    while board.check_win() == None:
        choice = random.choice(board.get_empty_squares())
        board.move(choice[0],choice[1],curr_player)
        curr_player = provided.switch_player(curr_player)


def mc_update_scores(scores,board,player):
    board_win = board.check_win()
    if board_win == provided.DRAW:
        scores = draw_list(len(scores))
        return scores
    
    score_current = SCORE_CURRENT * 1 if board_win == player else SCORE_CURRENT * -1
    score_other = SCORE_OTHER * 1 if board_win is not player else SCORE_OTHER * -1

    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if board.square(row ,col) == player:
                scores[row][col] += score_current
            elif board.square(row ,col) != 1:
                # If it's not empty
                scores[row][col] += score_other

#custom method
def draw_list(dimension):
    """
    creates an empty list of zeros
    """
    return [([0]* dimension) for dummy_i in range(dimension)]

def get_best_move(board,scores):
    """
    Gets the best possible move for a given board by using a scores grid
    """
    empty_spot = board.get_empty_squares()
    first_spot = empty_spot[0]
    highest_score = scores[first_spot[0]][first_spot[1]]
   
    best_move = first_spot
    
    for square in empty_spot:
        square_score = scores[square[0]][square[1]]
        if(square_score > highest_score):
            highest_score = square_score
            best_move = square    

    return best_move

def mc_move(board,player,trials):
    """
    Run a Monte Carlo test  and makes the best possible move with the given player
    """
    empty_scores =  draw_list(board.get_dim()) # Empty scores list

    for dummy_i in range(trials):
        cloned_board = board.clone() # New board based on the given board
        mc_trial(cloned_board,player)
        mc_update_scores(empty_scores, cloned_board,player)
    
        
    return get_best_move(board, empty_scores)





provided.play_game(mc_move, NTRIALS, False)