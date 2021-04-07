"""
slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""
import random
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
    coordinates = [i_value, j_value]
    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                d_temp, i_temp, j_temp = pair_distance(
                    cluster_list, idx1, idx2)
                if d_temp < distance:
                    coordinates = [i_temp, j_temp]
                    coordinates.sort()
                    distance = d_temp

    return (distance, coordinates[0], coordinates[1])


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """

    num_clusters = len(cluster_list)
    if num_clusters <= 3:
        distance, i_value, j_value = slow_closest_pair(cluster_list)
    else:
        m_value = int(math.floor(num_clusters/2))
        left_cluster = cluster_list[0:m_value]
        right_cluster = cluster_list[m_value:]
        left_distance, left_i_value, left_j_value = fast_closest_pair(
            left_cluster)
        right_distance, right_i_value, right_j_value = fast_closest_pair(
            right_cluster)
        if left_distance > right_distance:
            distance, i_value, j_value = right_distance, right_i_value + \
                m_value, right_j_value + m_value
        else:
            distance, i_value, j_value = left_distance, left_i_value, left_j_value
        mid = .5*(cluster_list[m_value].horiz_center() +
                  cluster_list[m_value].horiz_center())
        temp_distance, temp_i_value, temp_j_value = closest_pair_strip(
            cluster_list, mid, distance)
        if distance > temp_distance:
            distance, i_value, j_value = temp_distance, temp_i_value, temp_j_value

    return (distance, i_value, j_value)


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

    s_cluster_list = []
    for i_value in range(len(cluster_list)):
        if abs(cluster_list[i_value].horiz_center() - horiz_center) < half_width:
            s_cluster_list.append([cluster_list[i_value], i_value])
    s_cluster_list.sort(key=lambda cluster: cluster[0].vert_center())
    length_k = len(s_cluster_list)
    distance, i_value, j_value = float('inf'), -1, -1
    coordinates = [i_value, j_value]
    for idx1 in range(length_k-1):
        number = min([idx1+4, length_k])
        for idx2 in range(idx1+1, number):
            temp_distance, temp_i_value, temp_j_value = pair_distance(
                cluster_list, s_cluster_list[idx1][1], s_cluster_list[idx2][1])
            if temp_distance < distance:
                coordinates = [temp_i_value, temp_j_value]
                coordinates.sort()
                distance = temp_distance

    return (distance, coordinates[0], coordinates[1])

######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Note that your implementation of lines 5-6 in the pseudo-code
    need not match the pseudo-code verbatim. In particular, merging
    one cluster into the other using merge_clusters and then removing
    the other cluster is fine. Note that, for this function, mutating
    cluster_list is allowed to improve performance.

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    cluster_list.sort(key=lambda cluster: cluster.horiz_center())
    while len(cluster_list) > num_clusters:
        (dummy, cluster_i, cluster_j) = fast_closest_pair(cluster_list)
        cluster_list[cluster_i].merge_clusters(cluster_list[cluster_j])
        cluster_list.remove(cluster_list[cluster_j])
        cluster_list.sort(key=lambda cluster: cluster.horiz_center())
    return cluster_list


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    population_and_index = [(cluster_list[idx].total_population(), idx)
                            for idx in range(len(cluster_list))]
    population_and_index.sort()
    population_and_index.reverse()
    mean_cluster = [(cluster_list[population_and_index[idx][1]].horiz_center(),
                     cluster_list[population_and_index[idx][1]].vert_center())
                    for idx in range(num_clusters)]

    new_cluster_list = []
    for dummy_i in range(num_iterations):
        # initialize k empty sets C1,.....,Ck
        mean_cluster_list = []
        new_cluster_list = []
        for i_index in range(num_clusters):
            mean_cluster_list.append(
                alg_cluster.Cluster(
                    set([]),
                    mean_cluster[i_index][0],
                    mean_cluster[i_index][1],
                    0, 0))
            new_cluster_list.append(
                alg_cluster.Cluster(
                    set([]),
                    mean_cluster[i_index][0],
                    mean_cluster[i_index][1],
                    0, 0))
        # This was for creating the new_cluster_list

        for idx1 in range(len(cluster_list)):
            temp_dist = []
            for idx2 in range(num_clusters):
                temp_dist.append((cluster_list[idx1].distance(
                    mean_cluster_list[idx2]), idx2))
            new_cluster_list[min(temp_dist)[1]].merge_clusters(cluster_list[idx1])

        # This is for redefining the new_clusters center

        mean_cluster = [(new_cluster_list[idx].horiz_center(), new_cluster_list[idx].vert_center())
                        for idx in range(num_clusters)]

    return new_cluster_list


def gen_random_cluster(num_clusters):
    """
    generates clusters
    Args:
        num_clusters (int): desired number of clusters
    Returns:
        list: a list of clusters
    """
    temp_list = []
    for dummy_i in range(num_clusters):
        temp_list.append(alg_cluster.Cluster(
            set([]),
            random.randint(-1, 1) * random.random(),
            random.randint(-1, 1) * random.random(),
            0, 0))
    return temp_list
