import math
from GA import GA


class TSP:
    cluster = None  # format_example with three clusters [[1,2],[2,3],[3,4]]
    path = [0]  # start at cluster_zero
    distance = 0
    it = 100
    lifeCount = 20
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

    def GA_Algorithm(self, n=0):
        print(self.lifeCount)
        citys = []
        for i in range(0, len(self.cluster)):
            citys.append(tuple(self.cluster[i]))

        ga = GA(aCrossRate=0.7,
                aMutationRage=0.02,
                aLifeCount=self.lifeCount,
                aGeneLenght=len(citys),
                aMatchFun=self.matchFun())

        ga.initOrder = self.path
        ga.initPopulation()

        distance_list = []
        generate = [index for index in range(1, n + 1)]
        while n > 0:
            ga.next()
            distance = self.distanceTotal(ga.best.gene)
            distance_list.append(distance)
            print(("第%d代 : 当前最小距离%f") % (ga.generation, distance))
            n -= 1
        self.distance = distance
        print('当前最优路线:')
        string = ''
        ppp = []
        for index in ga.best.gene:
            string += str(index) + '->'
            ppp.append(index)
        print(string[0:len(string) - 2])
        self.path = ppp
        # print("GA")

    def cal_cluster_path(self, algorithm='greedy'):
        if algorithm == 'greedy':
            self.distance = 0
            n = self.search_min()
            self.path = [n]
            self.Greedy_Algorithm()
            return self.path, self.distance

        elif algorithm == 'GA':
            self.distance = 0
            n = self.search_min()
            self.path = [n]
            self.Greedy_Algorithm()

            self.GA_Algorithm(self.it)
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

    def distanceTotal(self, order):
        distance = 0.0
        for i in range(-1, len(self.cluster) - 1):  # 取到-1，因为要形成一个回路形成一个哈密顿图 #
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.cluster[index1], self.cluster[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)  # 欧式距离 #
        return distance

    def matchFun(self):
        return lambda life: 1.0 / self.distanceTotal(life.gene)