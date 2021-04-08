"""
Question 10
"""

import main
import alg_project3_viz3 as alg_viz
import alg_cluster
import matplotlib.pyplot as plt

data_table_111 = alg_viz.load_data_table(alg_viz.DATA_111_URL)
data_table_290 = alg_viz.load_data_table(alg_viz.DATA_290_URL)
data_table_896 = alg_viz.load_data_table(alg_viz.DATA_896_URL)

singleton_list_111 = []
for line in data_table_111:
    singleton_list_111.append(alg_cluster.Cluster(
        set([line[0]]), line[1], line[2], line[3], line[4]))
singleton_list_290 = []
for line in data_table_290:
    singleton_list_290.append(alg_cluster.Cluster(
        set([line[0]]), line[1], line[2], line[3], line[4]))
singleton_list_896 = []
for line in data_table_896:
    singleton_list_896.append(alg_cluster.Cluster(
        set([line[0]]), line[1], line[2], line[3], line[4]))


def compute_distortion(cluster_list, data_table):
    """computes the overall distortion

    Args:
        cluster_list (list): list of clusters

    Returns:
        int: the sum of the distortion of the clusters
    """
    distortion = 0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(data_table)
    return distortion



hierarchical_distortion_111 = []
kmeans_distortion_111 = []
hierarchical_distortion_290 = []
kmeans_distortion_290 = []
hierarchical_distortion_896 = []
kmeans_distortion_896 = []
index_1 = []
for idx in range(6, 21, 1):
    index_1.append(idx)


def showgraph_111():
    """
    for turning the graph on and off
    """
    for idx_111_2 in range(6, 21, 1):
        cluster_list_k = main.kmeans_clustering(singleton_list_111, idx_111_2, 5)
        kmeans_distortion_111.append(compute_distortion(cluster_list_k, data_table_111))
    for idx_111 in range(20, 5, -1):
        cluster_list_h = main.hierarchical_clustering(singleton_list_111, idx_111)
        hierarchical_distortion_111.append(compute_distortion(cluster_list_h, data_table_111))

    hierarchical_distortion_111.reverse()

    plt.title('Question 10, 111 points')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Distortion')
    plt.plot(index_1, hierarchical_distortion_111, label='hierarchical_distortion_111')
    plt.plot(index_1, kmeans_distortion_111, label='kmeans_distortion_111')
    plt.legend()
    plt.show()


def showgraph_290():
    """
    for turning the graph on and off
    """
    for idx_290_2 in range(6, 21, 1):
        cluster_list_k = main.kmeans_clustering(singleton_list_290, idx_290_2, 5)
        kmeans_distortion_290.append(compute_distortion(cluster_list_k, data_table_290))
    for idx_290 in range(20, 5, -1):
        cluster_list_h = main.hierarchical_clustering(singleton_list_290, idx_290)
        hierarchical_distortion_290.append(compute_distortion(cluster_list_h, data_table_290))

    hierarchical_distortion_290.reverse()

    plt.title('Question 10, 290 points')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Distortion')
    plt.plot(index_1, hierarchical_distortion_290, label='hierarchical_distortion_290')
    plt.plot(index_1, kmeans_distortion_290, label='kmeans_distortion_290')
    plt.legend()
    plt.show()


def showgraph_896():
    """
    for turning the graph on and off
    """
    for idx_896_2 in range(6, 21, 1):
        cluster_list_k = main.kmeans_clustering(singleton_list_896, idx_896_2, 5)
        kmeans_distortion_896.append(compute_distortion(cluster_list_k, data_table_896))
    for idx_896 in range(20, 5, -1):
        cluster_list_h = main.hierarchical_clustering(singleton_list_896, idx_896)
        hierarchical_distortion_896.append(compute_distortion(cluster_list_h, data_table_896))

    hierarchical_distortion_896.reverse()

    plt.title('Question 10, 896 points')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Distortion')
    plt.plot(index_1, hierarchical_distortion_896, label='hierarchical_distortion_896')
    plt.plot(index_1, kmeans_distortion_896, label='kmeans_distortion_896')
    plt.legend()
    plt.show()


showgraph_111()
showgraph_290()
showgraph_896()
