"""
Question 7
"""

import question_5 as q5
import question_6 as q6


def compute_distortion(cluster_list):
    """computes the overall distortion

    Args:
        cluster_list (list): list of clusters

    Returns:
        int: the sum of the distortion of the clusters
    """
    distortion = 0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(q5.data_table)
    return distortion


# For hierarchical_clustering
print("{:2e}".format(compute_distortion(q5.cluster_list)))
# answer for part a) 1.7516x10^11

# For kmeans_clustering
print("{:2e}".format(compute_distortion(q6.cluster_list)))
# answer for part a) 2.7125x10^11
