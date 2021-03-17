"""
[Project 1]
"""


EX_GRAPH0 = {0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1 = {0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2 = {0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),
            6:set([]),7:set([3]),8:set([1,2]),9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes. A complete graph
    contains all possible edges subject to the restriction that self-loops are not allowed. 
    The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive. 
    Otherwise, the function returns a dictionary corresponding to the empty graph.

    Args:
        num_nodes (int): And integer (probably) of the number of nodes

    Returns:
        Dictionary : a dictionary representing a gragh
    """
    my_graph = {}

    if num_nodes < 0:
        return my_graph
    else:
        for node in range(num_nodes):
            temp_list = []
            for index in range(num_nodes):
                temp_list.append(index)
            temp_list.remove(node)
            my_graph[node] = set(temp_list)
                
    return my_graph

def compute_in_degrees(digraph):
    """Takes a directed graph (represented as a dictionary) and computes the in-degrees for the
    nodes in the graph. The function should return a dictionary with the same set of keys (nodes) as digraph
    whose corresponding values are the number of edges whose head matches a particular node.

    Args:
        digraph (dictionary): a directed graph

    Returns:
        dictionary: dictionary of keys with corresponding number of edges
    """
    my_graph = {}
    for key in digraph:
        my_graph[key] = 0
        for index in digraph:
            if key in digraph.get(index):
                my_graph[key] +=1
    return my_graph


def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized
    distribution of the in-degrees of the graph. The function should return
    a dictionary whose keys correspond to in-degrees of nodes in the graph. The value associated
    with each  particular in-degree is the number of nodes with that in-degree. In-degrees with
    no corresponding nodes in the graph are not included in the dictionary.

    Args:
        digraph (dictionary): a directed graph

    Returns:
        dictionary: a dictionarys
    """
    denominator = len(digraph)
    my_distrobution = {}
    my_in_degrees = compute_in_degrees(digraph)
    for key in my_in_degrees.values():
        my_distrobution[key] = 0
        for index in digraph:
            if key == my_in_degrees[index]:
                my_distrobution[key] +=1

    return my_distrobution

print(in_degree_distribution(EX_GRAPH0))

