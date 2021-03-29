"""
Question 2
"""
import question_4 as q4

#largest connected componet @ 20% which is after removing 248 nodes
# remaing nodes are 992
# within 25% of 992 is 744
nodes_20percent_removal = int(len(q4.resil_comp)*.2) #248
lowest_25percent = int((len(q4.resil_comp) - nodes_20percent_removal)*.75) #744


cc_at_240_compnet = q4.resil_comp[nodes_20percent_removal]
cc_at_240_er = q4.resil_er[nodes_20percent_removal] 
cc_at_240_upa = q4.resil_upa[nodes_20percent_removal]

test_array = [cc_at_240_compnet,cc_at_240_er,cc_at_240_upa]

for value in test_array:
    if value > lowest_25percent:
        print value
        print('yes')
    else:
        print('no')

print 'the computer network is not resilient but the ER and the UPA graphs are resilient, the shape of the graph could best be described as linear with a negative slope of roughly -1'