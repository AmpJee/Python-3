import matplotlib.pyplot as plt
import random as rd

centriods = [[5, 6], [-3, 5], [1, 9]]

points = []
for cx, cy in centriods:
    for _ in range(500):
        x = rd.gauss(cx, 0.5)
        y = rd.gauss(cy, 0.5)
        points.append([x, y])

plt.figure(figsize=(10, 10))
plt.scatter([x for x, y in points], [y for x, y in points], s=4, label='Points')
plt.scatter([x for x, y in centriods], [y for x, y in centriods], s=10, color='black', label='Centroids')

plt.legend()
plt.title('K-Means Clustering')
plt.savefig('k-means_clusters.png')
plt.show()
