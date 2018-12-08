import math
import numpy as np

class TSP:
    cluster = None  # format_example with three clusters [[1,2],[2,3],[3,4]]
    path = [0]  # start at cluster_zero
    distance = 0

    def Greedy_Algorithm(self):
        # cal the number of cluster
        cluster_number = len(self.cluster)
        # label the city
        s = [0 for i in range(cluster_number)]
        # init the dis_array
        dis = [[0 for i in range(cluster_number)] for i in range(cluster_number)]
        # cal the dis_array
        for i in range(0, cluster_number):
            for j in range(0, cluster_number):
                if i == j:
                    dis[i][j] = 0
                elif j < i:
                    dis[i][j] = dis[j][i]
                else:
                    dis[i][j] = self.cal_dis(self.cluster[i], self.cluster[j])

        # greedy algorithm
        cluster_now = self.path[0]
        num_city = 1
        s[cluster_now] = 1
        while num_city != cluster_number:
            distance = 0
            shortestCluster = 0
            for i in range(cluster_number):
                if i == cluster_now or s[i] == 1:
                    continue
                if dis[cluster_now][i] < distance or distance == 0:
                    distance = dis[cluster_now][i]
                    shortestCluster = i

            self.distance = self.distance + distance
            s[shortestCluster] = 1
            self.path.append(shortestCluster)
            cluster_now = shortestCluster
            num_city = num_city + 1

    def cal_cluster_path(self, algorithm='greedy'):
        if algorithm == 'greedy':
            self.distance = 0
            n = self.search_min()
            self.path = [n]
            self.Greedy_Algorithm()
            return self.path, self.distance

    def cal_dis(self, p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def search_min(self):
        s = 0
        n = 0
        for i in range(0, len(self.cluster)):
            d = self.cal_dis(self.cluster[i], [0, 0])
            if d < s or s == 0:
                s = d
                n = i
        return n
