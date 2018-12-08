import pandas as pd

df = pd.read_csv("./dataset/cities.csv")
x = df["X"]
y = df["Y"]
clusterX = [[] for i in range(2000)]
clusterY = [[] for i in range(2000)]

import re

pattern = re.compile(r'\[(\d*)\]')

with open("./info/class.txt", "r") as f:
    for i in range(0, len(x)):
        cluster = int(pattern.findall(f.readline())[0])
        clusterX[cluster].append(x[i])
        clusterY[cluster].append(y[i])

import matplotlib.pyplot as plt

plt.figure(figsize=(50, 50))
for i in range(0, len(clusterX)):
    plt.scatter(clusterX[i], clusterY[i])

plt.show()
