"""ER undirect graph generator
"""

import random

def undirected_er_graph(numnodes, prob):
    """generates a undirected er graph from num nodes and probability

    Args:
        numnodes (int): and integer of the number of nodes
        prob (float): a number between 0 and 1

    Returns:
        dictionary: a dictionary reprentation of the graph
    """
    my_graph = {}
    for node in range(numnodes):
        my_graph[node] = set([])
    for V_i in my_graph.keys():
        for V_j in my_graph.keys():
            if V_i != V_j:
                a_variable = random.random()
                if a_variable < prob:
                    value_i = my_graph[V_i]
                    value_j = my_graph[V_j]
                    value_i.add(V_j)
                    value_j.add(V_i)
                    my_graph[V_i] = value_i
                    my_graph[V_j] = value_j
    return my_graph
