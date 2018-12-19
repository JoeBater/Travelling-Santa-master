from utils import *

length_cluster1 = 2000
length_cluster2 = 20
it_time = 30002

nodePosition = cluster_position_csv("./dataset/cities.csv")

# create map1 : node - > 1-cluster
map1 = [[], []]
with open("./info/city_labels.txt", 'r') as f:
    line = f.readline()
    index = 0
    while len(line) != 0:
        map1[0].append(index)
        map1[1].append(int(line))
        line = f.readline()

# split node
clusterBy2000 = [[] for i in range(length_cluster1)]
for i in range(len(map1[0])):
    clusterBy2000[map1[1][i]].append(i)

# create map2 : 1-cluster - > 2-cluster
map2 = [[], []]
with open("./info/city_labels_further.txt", 'r') as f:
    line = f.readline()
    index = 0
    while len(line) != 0:
        map2[0].append(index)
        map2[1].append(int(line))
        line = f.readline()

# split 1-cluster
clusterBy20 = [[] for i in range(length_cluster2)]
for i in range(len(map2[0])):
    clusterBy20[map2[1][i]].append(i)

# cal 2-cluster path
cluster2 = cluster_position("./info/cluster_further.txt")
p1, p2, p3 = generate_path(cluster2, 'GA', 20000, 2 * len(cluster2))
cluster2_path = p1

# sort by cluster2_path
clusterBy20S = []
for i in range(length_cluster2):
    clusterBy20S.append(clusterBy20[cluster2_path[i]])

# 1-cluster position
cluster1 = cluster_position("./info/cluster.txt")

#
clusterBy20S_Positon = [[] for i in range(length_cluster2)]
for i in range(len(clusterBy20S)):
    for j in range(len(clusterBy20S[i])):
        clusterBy20S_Positon[i].append(cluster1[clusterBy20S[i][j]])

clusterBy20S_PositonS = [[] for i in range(length_cluster2)]
for i in range(length_cluster2):
    p1, p2, p3 = generate_path(clusterBy20S_Positon[i], 'GA', it_time, 2 * len(clusterBy20S_Positon[i]))
    clusterBy20S_PositonS[i] = p2
    c = []
    for j in range(len(clusterBy20S[i])):
        c.append(clusterBy20S[i][p1[j]])
    clusterBy20S[i] = c

# plot_path(clusterBy20S_PositonS[0], True, size=1, flag=0)
# plot_path(clusterBy20S_PositonS[1], True, size=1, flag=1)

final_cluster_path = []
# save to file  2000 path
with open("./info/2000path.txt", 'w') as f:
    for i in range(len(clusterBy20S)):
        for j in range(len(clusterBy20S[i])):
            final_cluster_path.append(clusterBy20S[i][j])
            f.write(str(clusterBy20S[i][j]) + "\n")

#
clusterBy2000S = []
for i in range(length_cluster1):
    clusterBy2000S.append(clusterBy2000[final_cluster_path[i]])


clusterBy2000S_Position = [[] for i in range(length_cluster1)]
for i in range(length_cluster1):
    for j in range(len(clusterBy2000S[i])):
        clusterBy2000S_Position[i].append(nodePosition[clusterBy2000S[i][j]])

for i in range(length_cluster1):
    p1, p2, p3 = generate_path(clusterBy2000S_Position[i], 'GA', it_time, 2 * len(clusterBy2000S_Position[i]))
    c = []
    for j in range(len(clusterBy2000S[i])):
        c.append(clusterBy2000S[i][p1[j]])
    clusterBy2000S[i] = c

with open("./info/200000path.txt", 'w') as f:
    for i in range(len(clusterBy2000S)):
        for j in range(len(clusterBy2000S[i])):
            f.write(str(clusterBy2000S[i][j]) + "\n")
