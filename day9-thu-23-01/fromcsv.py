import matplotlib.pyplot as plt
import numpy as np
import csv

points = np.genfromtxt('points.csv', delimiter=',')
distances = np.genfromtxt('distances.csv', delimiter=',')

plt.scatter(points[:, 0], points[:, 1], c=distances)
plt.show()
