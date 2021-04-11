"""
Homework 4
"""
from itertools import permutations


def question_2():

    x = 'A'
    y = 'B'


def remove_permutations(new_string_1_list, old_string_1):
    my_temp_array = []
    for string_item in new_string_1_list:
        for i_value in range(len(string_item)):
            if len(string_item[i_value]) >= len(old_string_1):
                if string_item[i_value].replace('-', '') == old_string_1:
                    my_temp_array.append(string_item[i_value])
    return my_temp_array


def valid_alignments(align_1, align_2):
    modified_align_1 = ''
    modified_align_2 = ''
    permutations_1 = []
    permutations_2 = []
    valid_strings = set([])
    counter = 0
    if len(align_1) != len(align_2):
        if len(align_1) > len(align_2):
            num_base_dash = len(align_1)-len(align_2)
            modified_align_1 = align_1 + num_base_dash * '-'
            modified_align_2 = align_2 + len(align_1) * '-'
            for temp_value in range(len(modified_align_1)):
                permutations_1.append([''.join(p) for p in permutations(modified_align_1)])
                modified_align_1 = modified_align_1[0:len(modified_align_1)-1]
                permutations_2.append([''.join(p) for p in permutations(modified_align_2)])
                modified_align_2 = modified_align_1[0:len(modified_align_2)-1]
        elif len(align_2) > len(align_1):
            num_base_dash = len(align_2)-len(align_1)
            modified_align_2 = align_2 + num_base_dash * '-'
            modified_align_1 = align_1 + len(align_2) * '-'
            for temp_value in range(len(modified_align_2)):
                permutations_1.append([''.join(p) for p in permutations(modified_align_1)])
                modified_align_1 = modified_align_1[0:len(modified_align_1)-1]
                permutations_2.append([''.join(p) for p in permutations(modified_align_2)])
                modified_align_2 = modified_align_1[0:len(modified_align_2)-1]
    else:
        modified_align_2 = align_2 + len(align_2) * '-'
        modified_align_1 = align_1 + len(align_2) * '-'
        for temp_value in range(len(modified_align_2)):
            permutations_1.append([''.join(p) for p in permutations(modified_align_1)])
            modified_align_1 = modified_align_1[0:len(modified_align_1)-1]
            permutations_2.append([''.join(p) for p in permutations(modified_align_2)])
            modified_align_2 = modified_align_1[0:len(modified_align_2)-1]
    permutations_1 = remove_permutations(permutations_1, align_1)
    permutations_2 = remove_permutations(permutations_2, align_2)
    print(len(permutations_1))
    for x_prime in permutations_1:
        for y_prime in permutations_2:
            if len(x_prime) == len(y_prime):
                for char in range(len(x_prime)):
                    if x_prime[char] == '-' and y_prime[char] =='-':
                        break
                    if char == len(x_prime)-1:
                        valid_strings.add((x_prime,y_prime))

    return valid_strings


print(len(valid_alignments('ab', 'ab')))

def remove_again(list_perm, original):
    my_set =set([])
    for i_value in list_perm:
        if i_value.replace('-','') == original:
            my_set.add(i_value)
    return my_set


permu_11 = [''.join(p) for p in permutations('abc--')]
#print(permutations_9)
print(remove_again(permu_9, 'abc'))
print(len(remove_again(permu_9, 'abc')))

# Initialize OPT(i,j) = 0 wherever i>= j-4
# for k <= 5 to n-1
#    for i <= 1 to n-k
#        j <= i+k
#        OPT(i,j) = max(OPT(i,j-1), max(1+OPT(i,t-1)+ OPT(t+1,j-1)))
# return OPT(1,n)
