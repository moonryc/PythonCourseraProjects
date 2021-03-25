"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm

    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that each node number
        appears in correct ratio

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

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

def undirected_pa_graph(numnodes, m):
    """generates an upa graph using numnodes and m

    Args:
        numnodes (int): an int representing the largest number of nodes in the graph
        m (int): represent the number of starting nodes

    Returns:
        dictionary: a dictionary representation of a graph
    """
    my_graph = make_complete_graph(m)
    obj = UPATrial(m)
    for i_value in range(m, numnodes):
        value = obj.run_trial(m)
        my_graph[i_value] = value
        for node in value:
            my_graph[node].add(i_value)
    return my_graph
