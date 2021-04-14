"""
Question 7
"""

import main

alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z'])

seq_x = 'abcde'
seq_y = 'xycdefg'
scoring_matrix = main.build_scoring_matrix(alphabet,2,1,0)
alignment_matrix = main.compute_alignment_matrix(seq_x, seq_y,scoring_matrix,True)
alignment = main.compute_global_alignment(seq_x, seq_y,scoring_matrix,alignment_matrix)
print(alignment)
x_l = len(seq_x)-1
y_l = len(seq_y)-1
print('the edit distance is: ' ,x_l +y_l - alignment[0])
print('The answer is: (diagonal_score:2, off_diag_score:1, dash_score:0)')
