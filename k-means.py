import pandas as pd
from sklearn.externals import joblib

df = pd.read_csv("./dataset/cities.csv")
x = df["X"]
y = df["Y"]

print("start to create the positions............................")
positions = []
for i in range(len(x)):
    positions.append([x[i], y[i]])
print("finish the process!")

print("start to K-means.........................................")
from sklearn.cluster import KMeans

n_cluster = 2000
kmeans = KMeans(n_clusters=n_cluster, n_jobs=5).fit(positions)

joblib.dump(kmeans,  './kmeans_model/doc_cluster.pkl')

labels = kmeans.labels_
cluster_position = kmeans.cluster_centers_
print("finish the process!")

print("write the details to files...............................")
with open("cluster.txt", "w") as f:
    for i in range(n_cluster):
        f.write(str(cluster_position[i]) + "\n")

with open("city_labels.txt", "w") as f:
    for i in range(n_cluster):
        f.write(str(labels[i]) + "\n")

print("finish the process!")
