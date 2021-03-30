"""

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """

    distance, i_value, j_value = float('inf'), -1, -1
    coordinates = [i_value,j_value]
    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                d_temp, i_temp, j_temp = pair_distance(cluster_list,idx1, idx2)
                if d_temp < distance:
                    coordinates = [i_temp,j_temp] 
                    coordinates.sort()
                    distance = d_temp
    return (distance,coordinates[0],coordinates[1])


#print(slow_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0)]))
#print(slow_closest_pair([alg_cluster.Cluster(set([]), 1.1, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0.8, 1, 0)]))
#print(slow_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 1, 1, 0), alg_cluster.Cluster(set([]), 3, 2, 1, 0)]))
#print(slow_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 0, 1, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 1, 1, 0)]))
#(1.0,0,1)
#(float,0,1)

def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """

    return ()


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """

    return ()



######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    return []


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    return []


TEST_CASE= [alg_cluster.Cluster(set(['00']), 0.0, 0.0, 1, 0.1), 

             alg_cluster.Cluster(set(['10']), 1.0, 0.0, 2, 0.1), 

             alg_cluster.Cluster(set(['11']), 1.0, 1.0, 3, 0.1), 

             alg_cluster.Cluster(set(['01']), 0.0, 1.0, 4, 0.1), 

             alg_cluster.Cluster(set(['1010']), 10.0, 10.0, 5, 0.1), 

             alg_cluster.Cluster(set(['1011']), 10.0, 11.0, 6, 0.1), 

             alg_cluster.Cluster(set(['1111']), 11.0, 11.0, 7, 0.1), 

             alg_cluster.Cluster(set(['1110']), 11.0, 10.0, 8, 0.1)]

