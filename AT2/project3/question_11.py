"""
Question 11
"""
import question_3 as q3
import main
import matplotlib.pyplot as plt


data_table_111 = q3.data_table
singleton_list_111 = q3.singleton_list


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
index_1 = []
for idx in range(6, 21, 1):
    index_1.append(idx)


def showgraph_3108():
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


showgraph_3108()

"""Answer: for the first data set with 111 points it clear that heirchal has less distortion but the remaining two data sets
    do not mimic this behavior. So the answer is no. If you choose a larger data set though such as 3108 you can see that kmeans ends up with less distortion.
    so in conclusion with fewer points heirchal is better but at a certain point once you have a large enough number of points kmeans becomes
    the less distorted methoid in the long run.
    """
