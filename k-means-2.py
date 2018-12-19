from utils import cluster_position
from sklearn.externals import joblib

positions = cluster_position("./info/cluster.txt")

print("start to K-means.........................................")
from sklearn.cluster import KMeans

n_cluster = 20
kmeans = KMeans(n_clusters=n_cluster, n_jobs=5).fit(positions)

joblib.dump(kmeans, './kmeans_model/doc_cluster_further.pkl')

labels = kmeans.labels_
print(len(labels))
cluster_position = kmeans.cluster_centers_
print(len(cluster_position))
print("finish the process!")

print("write the details to files...............................")
with open("./info/cluster_further.txt", "w") as f:
    for i in range(len(cluster_position)):
        f.write(str(cluster_position[i]) + "\n")

with open("./info/city_labels_further.txt", "w") as f:
    for i in range(len(labels)):
        f.write(str(labels[i]) + "\n")

print("finish the process!")
