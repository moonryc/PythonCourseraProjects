"""
Question 8
"""

import main
import alg_appliccation4_provided as algo

word_list = algo.read_words(algo.WORD_LIST_URL)
first_spelling_check = main.check_spelling('humble', 1, word_list)
second_spelling_check = main.check_spelling('firefly', 2, word_list)
print('Question 8')
print('first_spelling_check: ', first_spelling_check)
print('second_spelling_check: ', second_spelling_check)
