"""
Question 1
"""

import main
import alg_appliccation4_provided as algo

human_protein_string = algo.read_protein(algo.HUMAN_EYELESS_URL)
fruitfly_protein_string = algo.read_protein(algo.FRUITFLY_EYELESS_URL)
scoring_matrix_pam50 = algo.read_scoring_matrix(algo.PAM50_URL)

alignment_matrix_pam50 = main.compute_alignment_matrix(human_protein_string, fruitfly_protein_string, scoring_matrix_pam50,False)
pam50_local_alignment = main.compute_local_alignment(human_protein_string,fruitfly_protein_string,scoring_matrix_pam50,alignment_matrix_pam50)
print()
print('Question 1')
print('Score: ', pam50_local_alignment[0])
print('Human local: ', pam50_local_alignment[1])
print('Fruitfly local: ', pam50_local_alignment[2])