"""
Question 3
"""
import time
import matplotlib.pyplot as plt
import main
import alg_application2_provided as comnet




################################################################
#The tighetest upper bound for targeted_order looks to be

#n
#    n
#    m

#O(n*(n+m)) => but the website says the answer is n^2

#The tighetest upper bound for fast_target_order looks to be

#n
#n
#n
#    m
#        m?

#O(n+m)

################################################################

#q1.compnet
#main.fast_target_order(compnet)
#comnet.targeted_order()
m = 5
numnodes = [idx for idx in range(10, 1000, 10)]
graph_list = []
for num_nodes in range(10, 1000, 10):
    graph_list.append(main.get_upa_graph(num_nodes, 5))

fast = []
slow = []



for graph in graph_list:
    start_time_slow = time.clock()
    comnet.targeted_order(graph)
    ellapsed_slow = time.clock()-start_time_slow
    slow.append(ellapsed_slow)
    start_time_fast = time.clock()
    main.fast_target_order(graph)
    ellapsed_fast = time.clock() -start_time_fast
    fast.append(ellapsed_fast)



print len(fast)

################################################################

#Graph

#Graph
def showgraph():
    plt.title('Question 3')
    plt.xlabel('Size of UPA')
    plt.ylabel('running time in seconds')
    plt.text(0, 0, 'm = {}'.format(m))
    plt.plot(numnodes, fast, label='Fast_targeted_order')
    plt.plot(numnodes, slow, label='targeted_order')
    plt.legend()
    plt.show()
showgraph()
