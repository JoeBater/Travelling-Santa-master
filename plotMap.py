import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./dataset/cities.csv")
x = df["X"]
y = df["Y"]
plt.figure(figsize=(50, 50))
plt.scatter(x, y)
plt.show()
