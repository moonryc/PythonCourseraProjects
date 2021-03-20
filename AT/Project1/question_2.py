import random
import main
import matplotlib.pyplot as plt
#import user48_LAdJVaadjQ_7 as main
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

er_dictionary = main.create_dic(V,E)
num_nodes = len(er_dictionary)
er_dic_in = main.compute_in_degrees(er_dictionary)
unnormal_er_in = main.in_degree_distribution(er_dictionary)
normalized_er_in = main.normalized_in_degree_distrobution(unnormal_er_in,num_nodes)
GRAPH_log = main.log_normalized(normalized_er_in)

#simpleplot.plot_scatter('Normalized Distrobution', 600,600, 'log in-degree', 'log probability', [GRAPH_log])

# Plot

plt.title('Scatter plot pythonspot.com')
for data_dict in GRAPH_log:
    x = data_dict
    y = GRAPH_log.get(x)
    plt.scatter(x,y)

#plt.legend(plot.keys())
plt.show()
