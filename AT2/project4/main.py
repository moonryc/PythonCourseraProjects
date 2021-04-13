"""
Project 4 main functions
"""


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """builds a dictionary representation of a scoring matrix

    Args:
        alphabet (set): a set of letters not including a dash
        diag_score (int): an int to represent the score of matching letters
        off_diag_score (int): an int to represent the score for when letters are matched
        dash_score (int): an int to represent the score for when a letter is mattched with a dash

    Returns:
        dictionary: a nested dictionary representation of of the scoring matrix
    """
    alphabet = list(alphabet)
    alphabet.append('-')
    temp_score_dict = {}
    for i_value in alphabet:
        if i_value != '-':
            second_temp_dict = {}
            for j_value in alphabet:
                if j_value == i_value:
                    second_temp_dict[j_value] = diag_score
                elif j_value != '-':
                    second_temp_dict[j_value] = off_diag_score
                else:
                    second_temp_dict[j_value] = dash_score
            temp_score_dict[i_value] = second_temp_dict
        else:
            second_temp_dict = {}
            for j_value in alphabet:
                second_temp_dict[j_value] = dash_score
            temp_score_dict[i_value] = second_temp_dict
    return temp_score_dict


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """Computes the alignment matrix/ dynamic programming table. If the global flag is set to True it compute a global alignment matrix if set to False it computes a local alignment matrix if set to

    Args:
        seq_x (string): a string of letters
        seq_y (string): a string of letters
        scoring_matrix (dictionary): a dictionary representation of the sccore for letter combinations
        global_flag (booleans): True for global and False for local

    Returns:
        2d list: a 2d list to represent....
    """
    seq_x_length = len(seq_x)
    seq_y_length = len(seq_y)
    temp_alignment_matrix = [[0 for dummy_one in range(
        seq_y_length+1)] for dummy_two in range(seq_x_length+1)]
    for i_value in range(1, seq_x_length+1):
        temp_alignment_matrix[i_value][0] = scoring_matrix[seq_x[i_value-1]]['-'] + \
            temp_alignment_matrix[i_value-1][0]
        if temp_alignment_matrix[i_value][0] < 0 and global_flag is False:
            temp_alignment_matrix[i_value][0] = 0
    for j_value in range(1, seq_y_length+1):
        temp_alignment_matrix[0][j_value] = scoring_matrix['-'][seq_y[j_value-1]] + \
            temp_alignment_matrix[0][j_value-1]
        if temp_alignment_matrix[0][j_value] < 0 and global_flag is False:
            temp_alignment_matrix[0][j_value] = 0
    for i_value in range(1, seq_x_length+1):
        for j_value in range(1, seq_y_length+1):
            m_x_y = scoring_matrix[seq_x[i_value-1]][seq_y[j_value-1]]
            m_x_dash = scoring_matrix[seq_x[i_value-1]]['-']
            m_dash_y = scoring_matrix['-'][seq_y[j_value-1]]
            temp_alignment_matrix[i_value][j_value] = max(
                temp_alignment_matrix[i_value - 1][j_value - 1] + m_x_y,
                temp_alignment_matrix[i_value - 1][j_value] + m_x_dash,
                temp_alignment_matrix[i_value][j_value - 1] + m_dash_y)
            if temp_alignment_matrix[i_value][j_value] < 0 and global_flag is False:
                temp_alignment_matrix[i_value][j_value] = 0
    return temp_alignment_matrix


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """computes the optimal pairwise strings based on two sequences, scoring matrix and alignment_matrix

    Args:
        seq_x (string): string of letters
        seq_y (string): string of letters
        scoring_matrix (dictionary): a dictionary used to score the combinations
        alignment_matrix (2d list): an alignment matrix

    Returns:
        int, string, string: the score and 2 pairwise strings that have the highest score
    """
    score = 0
    i_value = len(seq_x)
    j_value = len(seq_y)
    x_prime = ''
    y_prime = ''
    while i_value != 0 and j_value != 0:
        if alignment_matrix[i_value][j_value] == alignment_matrix[i_value-1][j_value-1] + scoring_matrix[seq_x[i_value-1]][seq_y[j_value-1]]:
            x_prime = seq_x[i_value-1] + x_prime
            y_prime = seq_y[j_value-1] + y_prime
            i_value -= 1
            j_value -= 1
        else:
            if alignment_matrix[i_value][j_value] == alignment_matrix[i_value - 1][j_value] + scoring_matrix[seq_x[i_value - 1]]['-']:
                x_prime = seq_x[i_value-1] + x_prime
                y_prime = '-' + y_prime
                i_value -= 1
            else:
                x_prime = '-' + x_prime
                y_prime = seq_y[j_value-1] + y_prime
                j_value -= 1
    while i_value != 0:
        x_prime = seq_x[i_value-1] + x_prime
        y_prime = '-'+y_prime
        i_value -= 1
    while j_value != 0:
        y_prime = seq_y[j_value-1] + y_prime
        x_prime = '-' + x_prime
        j_value -= 1
    index = 0
    for index in range(len(x_prime)):
        score += scoring_matrix[x_prime[index]][y_prime[index]]
    return score, x_prime, y_prime


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """computes the local alignment

    Args:
        seq_x (string): a string of letters
        seq_y (string): a string of letters
        scoring_matrix (dictionary): a dictionary used to score the combinations
        alignment_matrix (2d list): an alignment matrix

    Returns:
        int,string, string: an int representation of the score of the 2 string followed by the 2 strings
    """
    score = 0
    i_value = len(seq_x)
    j_value = len(seq_y)
    x_prime = ''
    y_prime = ''
    temp_row = 0
    temp_col = 0
    temp_max = 0
    for indx in range(len(alignment_matrix)):
        for indx_2 in range(len(alignment_matrix[0])):
            if alignment_matrix[indx][indx_2] >= temp_max:
                temp_row = indx
                temp_col = indx_2
                temp_max = alignment_matrix[indx][indx_2]
    i_value = temp_row
    j_value = temp_col
    while alignment_matrix[i_value][j_value] != 0:
        if alignment_matrix[i_value][j_value] == alignment_matrix[i_value-1][j_value-1] + scoring_matrix[seq_x[i_value-1]][seq_y[j_value-1]]:
            x_prime = seq_x[i_value-1] + x_prime
            y_prime = seq_y[j_value-1] + y_prime
            i_value -= 1
            j_value -= 1
        else:
            if alignment_matrix[i_value][j_value] == alignment_matrix[i_value - 1][j_value] + scoring_matrix[seq_x[i_value - 1]]['-']:
                x_prime = seq_x[i_value-1] + x_prime
                y_prime = '-' + y_prime
                i_value -= 1
            else:
                x_prime = '-' + x_prime
                y_prime = seq_y[j_value-1] + y_prime
                j_value -= 1
    for index in range(len(x_prime)):
        score += scoring_matrix[x_prime[index]][y_prime[index]]
    return score, x_prime, y_prime
