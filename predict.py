from sklearn.externals import joblib
import pandas as pd

def predict_class(model_path, vectorX, vectorY, output):
    kmeans = joblib.load(model_path)
    with open(output, "w") as f:
        for i in range(0, len(vectorX)):
            f.write(str(kmeans.predict([[vectorX[i], vectorY[i]]])) + "\n")

df = pd.read_csv("./dataset/cities.csv")

x = df["X"]
y = df["Y"]

predict_class("./kmeans_model/doc_cluster.pkl", x, y, "./info/class.txt")

import re

pattern = re.compile(r'(\d*\.\d*)')
cluster_X = []
cluster_Y = []
line = "123"
with open("./info/cluster.txt", "r") as f:
    while 1:
        line = pattern.findall(f.readline())
        if len(line) == 0:
            break
        cluster_X.append(float(line[0]))
        cluster_Y.append(float(line[1]))

predict_class("./kmeans_model/doc_cluster_further.pkl", cluster_X, cluster_Y, "./info/class_further.txt")

