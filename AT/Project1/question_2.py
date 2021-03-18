import random
import math
import question_1 as q1
#import user48_LAdJVaadjQ_7 as q1
#import codeskulptor
#import simpleplot
#codeskulptor.set_timeout(30)

V = [dummy_i for dummy_i in range(1000)]
E = []
p = .5

for V_i in V:
    sub_list = set([])
    for V_j in V:
        if V_i != V_j:
            a = random.random()
            if a < p:
                sub_list.add(V_j)
    E.append(sub_list)

def create_dic(nodes,edges):
    my_dict={}
    for index in nodes:
        my_dict[index] = edges[index]
    return my_dict

er_dictionary = create_dic(V,E)
num_nodes = len(er_dictionary)
er_dic_in = q1.compute_in_degrees(er_dictionary)
unnormal_er_in = q1.in_degree_distribution(er_dictionary)
normalized_er_in = q1.normalized_in_degree_distrobution(unnormal_er_in,num_nodes)

def log_normalized(normalized_dict):
    log_dict = {}
    for key in normalized_dict.keys():
        if key != 0:
            log_dict[float(math.log(key))] = float(math.log(normalized_dict[key]))
    return log_dict

plot = log_normalized(normalized_er_in)
print(plot)



#simpleplot.plot_scatter('Normalized Distrobution', 600,600, 'in degree', 'ratio of occurence', [plot])
