"""
Question 6
"""

import main
import alg_project3_viz3 as alg_viz
import alg_cluster
import alg_clusters_matplotlib3

data_table = alg_viz.load_data_table(alg_viz.DATA_111_URL)

singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(
        set([line[0]]), line[1], line[2], line[3], line[4]))

cluster_list = main.kmeans_clustering(singleton_list, 9, 5)
alg_clusters_matplotlib3.plot_clusters(data_table, cluster_list, True)
