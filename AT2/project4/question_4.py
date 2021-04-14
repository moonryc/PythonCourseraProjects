"""
Question 4
"""
import pickle
import main
import matplotlib.pyplot as plt
import alg_appliccation4_provided as algo


human = algo.read_protein(algo.HUMAN_EYELESS_URL)
fruitfly = algo.read_protein(algo.FRUITFLY_EYELESS_URL)
scoring_matrix = algo.read_scoring_matrix(algo.PAM50_URL)


def pickle_null_distro():
    """
    Pickles the null_distro
    """
    _null_distro = main.generate_null_distribution(human, fruitfly, scoring_matrix, 1000)
    pickle_out = open('dict_slow.pickle', 'wb')
    pickle.dump(_null_distro, pickle_out)
    pickle_out.close()


def open_null_distro_pickle():
    """
    Opens the null_distro dictionary from the pickled file
    """
    pickle_in = open('dict_slow.pickle', 'rb')
    return pickle.load(pickle_in)


# pickle_null_distro()
null_distro = open_null_distro_pickle()

scores = list(null_distro.keys())
scores.sort()
my_values = []
for keys in scores:
    my_values.append(float(null_distro[keys]/1000.0))


def display_graph():
    """option to display graph
    """
    plt.bar(scores, my_values)
    plt.xlabel('Scores')
    plt.ylabel('Fraction of trials')
    plt.title('Scoring distrobution of local alignment Trials')
    plt.grid(True)
    plt.show()
