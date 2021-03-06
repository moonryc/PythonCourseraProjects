"""
[All of the functions that might be needed in project 1]
"""
import math

EX_GRAPH0 = {0:set([1,2]),1:set([]),2:set([])}
#EX_GRAPH1 = {0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
#EX_GRAPH2 = {0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),
#            6:set([]),7:set([3]),8:set([1,2]),9:set([0,3,4,5,6,7])}

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
    nodes in the graph. The function should return a dictionary with the same set of keys (nodes) as
    digraph whose corresponding values are the number of edges whose head matches a particular node.

    Args:
        digraph (dictionary): a directed graph

    Returns:
        dictionary: dictionary of keys with corresponding number of edges
    """
    my_graph = dict([(key, 0) for key in digraph])
    for targets in digraph.values():
        for target in targets:
            my_graph[target] += 1
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
    my_in_degrees = compute_in_degrees(digraph)
    my_distrobution = dict([(key, 0) for key in my_in_degrees.values()])
    for key in my_in_degrees.values():
        my_distrobution[key] += 1

    return my_distrobution

def compute_out_degree_average(digraph):
    denominator = float(len(digraph))
    out = digraph.values()
    numerator = 0
    for dummy_i in out:
        numerator += len(dummy_i)
    return float(numerator)/denominator

def normalized_in_degree_distrobution(unnormalized_distrobution,numnodes):
    """normalizes the in_degree_distrobution graph generated

    Args:
        unnormalized_distrobution (dictionary): graph generated by in_degree_distrobution
        numnodes (int): the len of the dictionary

    Returns:
        [dictionary]: a normalized dictionary of distrobution
    """
    my_dict = {}
    for key in unnormalized_distrobution:
        my_dict[key] = float(unnormalized_distrobution.get(key))/float(numnodes)
    return my_dict

def compute_out_degree_sum(digraph):
    """calculates the total sum of the out degrees of the graph

    Args:
        diagraph (graph): the current state of the graph

    Returns:
        int: the sum of the out_degrees of the entire graph
    """
    out = digraph.values()
    numerator = 0
    for dummy_i in out:
        numerator += len(dummy_i)
    return numerator

def compute_in_degrees_sum(digraph):
    """calculates the total sum of the in degrees of the graph

    Args:
        diagraph (graph): the current state of the graph

    Returns:
        int: the sum of the in_degrees of the entire graph
    """
    in_degrees = compute_in_degrees(digraph)
    in_degrees_values = in_degrees.values()
    return sum(in_degrees_values)

def log_normalized(normalized_dict):
    """takes the log of all of the keys and the values of a dictionary

    Args:
        normalized_dict (dictionary): a dictionary where both the keys and values are int

    Returns:
        dictionary: a dictionary with log(key):log(value)
    """
    log_dict = {}
    for key in normalized_dict.keys():
        if key != 0:
            new_key = float(math.log(key,10))
            old_value = normalized_dict[key]
            if old_value != 0:
                new_value = float(math.log(old_value,10))
                log_dict[new_key] = new_value
    return log_dict

def create_dic(nodes,edges):
    """Creates a band new dictionary based of of a list of nodes and a list containing set([]) of edges

    Args:
        nodes (list): a list of nodes
        edges (list): a list containing set([]) 

    Returns:
        [type]: [description]
    """
    my_dict={}
    for index in nodes:
        my_dict[index] = edges[index]
    return my_dict