"""
Question 5
"""

import math
import main
import question_4 as q4
import alg_appliccation4_provided as algo


human = algo.read_protein(algo.HUMAN_EYELESS_URL)
fruitfly = algo.read_protein(algo.FRUITFLY_EYELESS_URL)
scoring_matrix = algo.read_scoring_matrix(algo.PAM50_URL)
alignment_matrix = main.compute_alignment_matrix(human, fruitfly, scoring_matrix, False)
alignment = main.compute_local_alignment(human, fruitfly, scoring_matrix, alignment_matrix)
max_score = alignment[0]
max_score = float(max_score)


null_distro = q4.open_null_distro_pickle()

score = list(null_distro.keys())
freq = list(null_distro.values())
score_sum = 0

for i_value in range(len(score)):
    score_sum += score[i_value] * freq[i_value]

average = score_sum/sum(freq)

temp_internal_stand_dev = 0
for i_value in range(len(score)):
    temp_internal_stand_dev += ((score[i_value] - average)**2) * freq[i_value]
standard_dev = math.sqrt((temp_internal_stand_dev/sum(freq)))

print('Question 5')
print('The average is:', average)
print('The standard deviation is: ', standard_dev)
print('The z-value is: ', (max_score-average)/standard_dev)
