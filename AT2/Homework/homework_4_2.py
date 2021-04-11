"""[summary]
"""
my_scoring_matrix = [[10, 5, -10], [5, 10, -10], [-10, -10, -100000]]
the_scoring_matrix = [[5, 2, 2, 2, -2],
                      [2, 5, 2, 2, -2],
                      [2, 2, 5, 2, -2],
                      [2, 2, 2, 5, -2],
                      [-4, -4, -4, -4, 0]]
score_dictionary = {'a': 0, 'c': 1, 't': 2, 'g': 3, '-': 4}


def compute_global_alignment_scores_2(string_1, string_2, scoring_matrix):
    m = len(string_1)
    n = len(string_2)
    s = [[0 for temp_one in range(n+1)] for temp_two in range(m+1)]
    for i in range(1, m+1):
        #s[i][0] = s[i-1][0]
        s[i][0] = scoring_matrix[score_dictionary.get(
            string_1[i-1])][len(scoring_matrix)-1] + s[i-1][0]
    for j in range(1, n+1):
        #s[0][j] = s[0][j-1]
        s[0][j] = scoring_matrix[len(
            scoring_matrix)-1][score_dictionary.get(string_2[j-1])] + s[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            M_x_y = scoring_matrix[score_dictionary.get(
                string_1[i-1])][score_dictionary.get(string_2[j-1])]
            M_x_dash = scoring_matrix[score_dictionary.get(string_1[i-1])][len(scoring_matrix)-1]
            M_dash_y = scoring_matrix[len(scoring_matrix)-1][score_dictionary.get(string_2[j-1])]
            #s[i][j] = max(s[i-1][j-1],s[i-1][j],s[i][j-1] )
            #s[i][j] = max(s[i-1][j-1] + M_x_y,s[i-1][j],s[i][j-1] )
            s[i][j] = max(s[i-1][j-1] + M_x_y, s[i-1][j] + M_x_dash, s[i][j-1] + M_dash_y)
    return s


#print(compute_global_alignment_scores_2('ac', 'tag', the_scoring_matrix))


def compute_alignment(string_1, string_2, scoring_matrix, dynamic_table):
    i = len(string_1)
    j = len(string_2)
    x_prime = ''
    y_prime = ''
    while i != 0 and j != 0:
        if dynamic_table[i][j] == dynamic_table[i-1][j-1] + scoring_matrix[score_dictionary.get(
                string_1[i-1])][score_dictionary.get(string_2[j-1])]:
            x_prime = x_prime + string_1[i-1]
            y_prime = y_prime + string_2[j-1]
            i -= 1
            j -= 1
        else:
            if dynamic_table[i][j] == dynamic_table[i-1][j] + scoring_matrix[score_dictionary.get(string_1[i-1])][
                    len(scoring_matrix)]:
                x_prime = x_prime + string_1[i-1]
                y_prime = '-'+y_prime #+ '-'
                i -= 1
            else:
                x_prime = '-'+x_prime #+ '-'
                y_prime = y_prime + string_2[j-1]
                j -= 1
    while i != 0:
        x_prime = string_1[i-1] + x_prime
        y_prime = y_prime+ '-' 
        i-=1
    while j != 0:
        y_prime = string_2[j-1] + y_prime
        x_prime = x_prime +'-'  
        j-=1
    return x_prime, y_prime

print(compute_alignment('ac','tag',the_scoring_matrix,compute_global_alignment_scores_2('ac', 'tag', the_scoring_matrix)))