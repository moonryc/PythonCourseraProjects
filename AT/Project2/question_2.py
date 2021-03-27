"""
Question 2
"""
import question_1 as q1

#largest connected componet @ 20% which is after removing 248 nodes
# remaing nodes are 992
# within 25% of 992 is 744
nodes_20percent_removal = int(len(q1.resil_comp)*.2) #248
lowest_25percent = int((len(q1.resil_comp) - nodes_20percent_removal)*.75) #744


cc_at_240_compnet = q1.resil_comp[nodes_20percent_removal]
cc_at_240_er = q1.resil_er[nodes_20percent_removal] 
cc_at_240_upa = q1.resil_upa[nodes_20percent_removal]

test_array = [cc_at_240_compnet,cc_at_240_er,cc_at_240_upa]

for value in test_array:
    if value > lowest_25percent:
        print('yes')
    else:
        print('no')

print 'all graphs are resilient, the shape of the graph could best be described as linear with a negative slope of roughly -1'