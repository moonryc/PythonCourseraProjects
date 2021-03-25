"""
Breath first search algo for looking through a graph represented by a dictionary
"""
from collections import deque
import random
import alg_application2_provided as comnet

def get_num_edges(ugraph):
    """returns the todal number of edges in the graph

    Args:
        ugraph (dictionary): a graph represented by a dictionarys

    Returns:
        int: the number of edges
    """
    total = 0
    for node in ugraph:
        total += len(ugraph[node])
    return total/2

def bfs_visited(ugraph, start_node):
    """returns a set of nodes that were visited in the the breadth first search

    Args:
        ugraph (dict): an undirected graph
        start_node (int): an int representing the starting node in the ugraph

    Returns:
        set: a set of all nodes that are visitable
    """
    my_queue = deque() #my_queue = Q
    visited = set([start_node])
    my_queue.append(start_node)
    while len(my_queue) > 0:
        node = my_queue[0]
        my_queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                my_queue.append(neighbor)
    return visited

def cc_visited(ugraph):
    """
    takes a dictionary and returns a list of sets where each set consists
    of all the nodes (nothing else) in a connected componet and there is exactly
    one set in the list for each componet

    Args:
        ugraph (dictionary): an undirected graph

    Returns:
        list: a list of sets consisting of connected nodes
    """
    remainingnodes = set(ugraph.keys())
    my_cc = []
    while len(remainingnodes) > 0:
        node = random.choice(list(remainingnodes))
        w_visited = bfs_visited(ugraph, node)
        my_cc.append(w_visited)
        remainingnodes = remainingnodes - w_visited
    return my_cc

def largest_cc_size(ugraph):
    """takes the undirected graph and returns an int of the largest connect componet

    Args:
        ugraph (dictionary): an undirected graph

    Returns:
        int: the size of the largest connected componet
    """
    my_set = cc_visited(ugraph)
    largest = 0
    for index in my_set:
        if len(index) > largest:
            largest = len(index)
    return largest

def compute_resilience(ugraph, attack_order):
    """[summary]

    Args:
        ugraph (undirected graph): an undirected graph
        attack_order (list): a list of nodes

    Returns:
        list: 
    """
    my_graph = ugraph
    largest_componets =[]
    largest_componets.append(largest_cc_size(ugraph))
    for attack in attack_order:
        node_remove = attack
        connected_nodes = my_graph.get(node_remove)
        for index in connected_nodes:
            value = my_graph[index]
            value.remove(node_remove)
            my_graph[index] = value
        my_graph.pop(attack)
        largest_componets.append(largest_cc_size(my_graph))
    return largest_componets

def computer_network_graph():
    """returns the computer network graph

    Returns:
        dictionary: a graph the represents the computer network graph
    """
    return comnet.load_graph(comnet.NETWORK_URL)

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

