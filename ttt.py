from utils import *

positions = cluster_position("./info/cluster_further.txt")
path, positions, dis = generate_path(positions, 'GA', 5000, 2 * len(positions))
positions2 = cluster_position("./info/cluster.txt")
positions1 = cluster_position_csv("./dataset/cities.csv")
print(positions1[0])
print(positions)
plot_path(positions1, False, size=0.1, flag=0)
plot_path(positions2, False, size=3, flag=0)
plot_path(positions, True, size=50, flag=1)


cl = [[] for i in range(2000)]
with open("./info/city_labels_further.txt", 'r') as f:
    line = "123"
    i = 0
    line = f.readline()
    while len(line) != 0:
        l = int(line)
        cl[l].append(positions2[i])
        i = i + 1
        line = f.readline()

p1, p2, p3 = generate_path(cl[0], 'GA', 30000, 2 * len(cl[0]))
plot_path(p2, True, size=1, flag=1)
