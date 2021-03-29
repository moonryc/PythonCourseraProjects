"""
Question 4
"""

import main
import matplotlib.pyplot as plt

################################
#Computer network
compnet = main.get_compnet_graph()
nodes = len(compnet)
edges = main.get_num_edges(compnet)
#compnet contains 1239 Nodes
#compnet contains 3047 Edges

attack_compnet = main.fast_target_order(compnet)
resil_comp = main.compute_resilience(compnet, attack_compnet)
#computer_network_graph = main.res_to_graph(resil_comp)
#print computer_network_graph



################################


################################
#ER algorithim
#need to comput p for for ER algorithim
probability = .004 
er_test = main.get_er_graph(1239, probability)

attack_er = main.fast_target_order(er_test)
resil_er = main.compute_resilience(er_test,attack_er)
#er_graph = main.res_to_graph(resil_er)

################################

################################
#UPA algorithm
#need to compute m for the UPA algorithim
m = 3
upa_test = main.get_upa_graph(1239, m)

attack_upa = main.fast_target_order(upa_test)
resil_upa = main.compute_resilience(upa_test, attack_upa)
#upa_graph = main.res_to_graph(resil_upa)


#################################
#Graph
def showgraph():
    plt.title('Question 4')
    plt.xlabel('Number of nodes removed')
    plt.ylabel('Largest Connected Componet due to Node Removal')
    plt.plot(resil_comp,label='Computer network resilience')
    plt.plot(resil_er,label='ER Algorithim resilience, p = {}'.format(probability))
    plt.plot(resil_upa,label='UPA Algorithim resilience, m = {}'.format(m))
    plt.legend()
    plt.show()
showgraph()
