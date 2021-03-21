"""
Generates a Graph for question 3 and containes the correct n and m
"""
import random
import main
import matplotlib.pyplot as plt
#import user48_LAdJVaadjQ_7 as main
#import codeskulptor
#import simpleplot
#codeskulptor.set_timeout(30)

#m must be <= n
# m is also the number of existing nodes to which a 
# new node is connected during iternation, m is a fixed number
#choose values for n and m that yield a DPA graph whose number of nodes and edges is roughly the same to those of the citation graph.

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def dpa_function(n,m):
    """generates a graph useing the DPA algorithim

    Args:
        n (int): number of nodes
        m (int): number of existing nodes to which a 
                 new node is connected during iternation, m is a fixed number
                 choose values for n and m that yield a DPA graph whose number
                 of nodes and edges is roughly the same to those of the citation graph.

    Returns:
        [dictionary]: a graph in the form of a dictionary
    """
    obj = DPATrial(m)
    graph = main.make_complete_graph(m)
    for i_value in range(m, n-1):
        graph[i_value] = obj.run_trial(m)
    return graph

GRAPH = dpa_function(27770,13)
#GRAPH = dpa_function(10,5)

in_degrees = main.compute_in_degrees(GRAPH)
unnormalized_in_degrees = main.in_degree_distribution(GRAPH)
normalized_in_degree_distro = main.normalized_in_degree_distrobution(unnormalized_in_degrees, len(GRAPH))
GRAPH_log = main.log_normalized(normalized_in_degree_distro)

edges_sum = main.compute_in_degrees_sum(GRAPH) + main.compute_out_degree_sum(GRAPH)
print('sum of edges:', edges_sum)

#simpleplot.plot_scatter('Normalized Distrobution', 'log in-degree', 'log probability', [GRAPH_log])

# Plot

plt.title('Scatter plot pythonspot.com')
for data_dict in GRAPH_log:
    x = data_dict
    y = GRAPH_log.get(x)
    plt.scatter(x, y)

#plt.legend(plot.keys())
plt.show()