import re
from TSP import *
import matplotlib.pyplot as plt

plt.figure(figsize=(50, 50))


def cluster_position(clusterfile):
    pattern = re.compile(r'(\d*\.\d*)')
    cluster = []
    line = "123"

    with open(clusterfile, "r") as f:
        while 1:
            line = pattern.findall(f.readline())
            if len(line) == 0:
                break
            cluster.append([float(line[0]), float(line[1])])
    return cluster


def generate_path(cluster, algorithm='greedy', it=100):
    t = TSP()
    t.cluster = cluster
    t.it = it
    path, diss = t.cal_cluster_path(algorithm=algorithm)
    path_position = []
    for i in range(len(cluster)):
        path_position.append(cluster[path[i]])
    return path, path_position, diss


def plot_path(path_position, flag=1):
    for i in range(len(path_position)):
        if i == 0:
            plt.scatter(path_position[i][0], path_position[i][1], s=100)
        else:
            plt.scatter(path_position[i][0], path_position[i][1], s=100)

    # paint line
    for i in range(len(path_position)):
        p1 = path_position[i % len(path_position)]
        p2 = path_position[(i + 1) % len(path_position)]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], c='b')
    if flag == 1:
        plt.show()
