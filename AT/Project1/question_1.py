#import codeskulptor
#codeskulptor.set_timeout(30)
import alg_load_graph as alg
#import simpleplot
import math

def make_complete_graph(numnodes):
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

    if numnodes < 0:
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

def normalized_in_degree_distrobution(unnormalized_distrobution,numnodes):
    my_dict = {}
    for key in unnormalized_distrobution:
        my_dict[key] = float(unnormalized_distrobution.get(key))/float(numnodes)
    return my_dict


scientific_dictionary = alg.load_graph(alg.CITATION_URL)
num_nodes = len(scientific_dictionary)
scientific_in_degrees = compute_in_degrees(scientific_dictionary)
unnormalized_in_degrees_distrobution = in_degree_distribution(scientific_dictionary)
normalized_in_degree_distro = normalized_in_degree_distrobution(unnormalized_in_degrees_distrobution, num_nodes)

def log_normalized(normalized_dict):
    log_dict = {}
    for key in normalized_dict.keys():
        if key != 0:
            log_dict[float(math.log(key))] = float(math.log(normalized_dict[key]))
    return log_dict
plot = log_normalized(normalized_in_degree_distro)


#simpleplot.plot_scatter('Normalized Distrobution', 1600,1600, 'in degree', 'ratio of occurence', [plot])

