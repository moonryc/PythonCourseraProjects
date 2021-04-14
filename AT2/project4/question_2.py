"""
Question 2
"""

import main
import question_1 as q1
import alg_appliccation4_provided as algo

local_human = q1.pam50_local_alignment[1].replace('-', '')
local_fruitfly = q1.pam50_local_alignment[2].replace('-', '')
consensus_pax_string= algo.read_protein(algo.CONSENSUS_PAX_URL)
#scoring matrix
scoring_matrix_pam50 = q1.scoring_matrix_pam50


global_align_human_pax_matrix = main.compute_alignment_matrix(local_human, consensus_pax_string,scoring_matrix_pam50,True)
global_align_fruitfly_pax_matrix = main.compute_alignment_matrix(local_fruitfly, consensus_pax_string,scoring_matrix_pam50,True)

global_align_human_pax = main.compute_global_alignment(local_human, consensus_pax_string,scoring_matrix_pam50,global_align_human_pax_matrix)
global_align_fruitfly_pax = main.compute_global_alignment(local_fruitfly, consensus_pax_string,scoring_matrix_pam50,global_align_fruitfly_pax_matrix)

print()
print('Question 2')
count = 0
for human in range(len(global_align_human_pax[1])):
    if global_align_human_pax[1][human] == global_align_human_pax[2][human]:
        count += 1
print('Human', float(count/len(global_align_human_pax[1])*100),'%')
print('Human global alignment: ', global_align_human_pax)
count_2 = 0
for human in range(len(global_align_fruitfly_pax[1])):
    if global_align_fruitfly_pax[1][human] == global_align_fruitfly_pax[2][human]:
        count_2 += 1
print('Fruitfly global alignment: ', global_align_fruitfly_pax)
print('Fruitfly', float(count_2/len(global_align_fruitfly_pax[1])*100),'%')

