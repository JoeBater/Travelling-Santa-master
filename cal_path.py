from utils import *
from sklearn.cluster import KMeans

cluster_cc = cluster_position("./info/cluster.txt")

path, path_position, diss = generate_path(cluster_cc)
print(diss)
plot_path(path_position)

'''
# solve the problem of long path
n_cluster = 20
kmeans = KMeans(n_clusters=n_cluster, n_jobs=5).fit(path_position)

from sklearn.externals import joblib
joblib.dump(kmeans,  './kmeans_model/doc_cluster_further.pkl')

labels = kmeans.labels_
cluster_position = kmeans.cluster_centers_
print("finish the process!")

print("write the details to files...............................")
with open("./info/cluster_further.txt", "w") as f:
    for i in range(n_cluster):
        f.write(str(cluster_position[i]) + "\n")

with open("./info/city_labels_further.txt", "w") as f:
    for i in range(n_cluster):
        f.write(str(labels[i]) + "\n")

print("finish the process!")

'''

cluster_fu = cluster_position("./info/cluster_further.txt")

path_f, path_position_f, d = generate_path(cluster_fu)
#plot_path(path_position_f)


diss = 0

cluster_f = [ [] for i in range(20)]

import re

pattern = re.compile(r'\[(\d*)\]')

with open("./info/class_further.txt", "r") as f:
    for i in range(2000):
        cluster = int(pattern.findall(f.readline())[0])
        cluster_f[cluster].append(cluster_cc[i])

print(path_f)
for i in range(20):
    path, path_position, dis = generate_path(cluster_f[i])
    diss = diss + dis
    plot_path(path_position,0)

#plt.show()
print(diss)



#----------------------------------------------------------------------------------
import pandas as pd
df = pd.read_csv("./dataset/cities.csv")
x = df["X"]
y = df["Y"]
po = []
for i in range(0,len(x)):
    po.append([x[i],y[i]])

cluster_o = [ [] for i in range(2000)]
with open("./info/class.txt", "r") as f:
    for i in range(len(x)):
        cluster = int(pattern.findall(f.readline())[0])
        cluster_o[cluster].append(po[i])

for i in range(2000):
    path, path_position, dis = generate_path(cluster_o[i])
    diss = diss + dis
    plot_path(path_position,0)
plt.show()
print(diss)