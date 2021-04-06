"""
Question 1
"""
import time
import main
import matplotlib.pyplot as plt

time_slow_closest_pair = []
time_fast_closest_pair = []
for i in range(2, 200):
    cluster_list = main.gen_random_cluster(i)

    slow_initial_time = time.perf_counter()
    main.slow_closest_pair(cluster_list)
    slow_final_time = time.perf_counter() - slow_initial_time
    time_slow_closest_pair.append(slow_final_time)

    fast_initial_time = time.perf_counter()
    main.fast_closest_pair(cluster_list)
    fast_final_time = time.perf_counter() - fast_initial_time
    time_fast_closest_pair.append(fast_final_time)


def showgraph():
    """
    for turning the graph on and off
    """
    plt.title('Question 1')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Running time in seconds')
    plt.plot(time_fast_closest_pair, label='fast_closest_pair')
    plt.plot(time_slow_closest_pair, label='slow_closest_pair')
    plt.legend()
    plt.show()


showgraph()
