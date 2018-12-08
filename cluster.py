import re
import matplotlib.pyplot as plt

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

import pandas as pd

df = pd.read_csv("./dataset/cities.csv")
x = df["X"]
y = df["Y"]
plt.figure(figsize=(50, 50))
plt.scatter(x, y)
sValue = 300
plt.scatter(cluster_X, cluster_Y, c='r', marker='o', s=sValue)
plt.show()

