from utils import *
from sklearn.cluster import KMeans

cluster_cc = cluster_position("./info/cluster.txt")

path, path_position, diss = generate_path(cluster_cc)

# solve the problem of long path
n_cluster = 20
kmeans = KMeans(n_clusters=n_cluster).fit(path_position)

from sklearn.externals import joblib
joblib.dump(kmeans,  './kmeans_model/doc_cluster_further.pkl')

labels = kmeans.labels_
print(len(labels))

cluster_position = kmeans.cluster_centers_
print(cluster_position)
print("finish the process!")
'''
print("write the details to files...............................")
with open("./info/cluster_further.txt", "w") as f:
    for i in range(n_cluster):
        f.write(str(cluster_position[i]) + "\n")

with open("./info/city_labels_further.txt", "w") as f:
    for i in range(n_cluster):
        f.write(str(labels[i]) + "\n")

print("finish the process!")
'''

