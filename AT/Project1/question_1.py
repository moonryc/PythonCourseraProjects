import main
import alg_load_graph as alg
import matplotlib.pyplot as plt
#import user48_LAdJVaadjQ_7 as main
#import codeskulptor
#import simpleplot
#codeskulptor.set_timeout(30)

#step1
GRAPH_papers = alg.load_graph(alg.CITATION_URL)
#step2
GRAPH_inde_unnormal = main.in_degree_distribution(GRAPH_papers)
#step3
GRAPH_normal_inde = main.normalized_in_degree_distrobution(GRAPH_inde_unnormal,len(GRAPH_papers))
#step4
GRAPH_log = main.log_normalized(GRAPH_normal_inde)

#simpleplot.plot_scatter('In-degree distrobution, Citation Graph', 600,600, 'log in-degree', 'log probability', [GRAPH_log])

# Plot

plt.title('Scatter plot pythonspot.com')
for data_dict in GRAPH_log:
    x = data_dict
    y = GRAPH_log.get(x)
    plt.scatter(x,y)

#plt.legend(plot.keys())
plt.show()