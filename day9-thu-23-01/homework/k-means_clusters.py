import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math
import time

def generate_points(centroids):
    points = []
    for cx, cy in centroids:
        for _ in range(500):
            x = rd.gauss(cx, 0.5)
            y = rd.gauss(cy, 0.5)
            points.append([x, y])
    return points


def plot_initial(points, centroids, ):
    plt.figure()
    plt.scatter([x for x, y in points], [y for x, y in points], s=4, label='Points')
    plt.scatter([x for x, y in centroids], [y for x, y in centroids], s=10, color='black', label='Centroids')
    plt.legend()
    plt.title('Initial Points and Centroids')
    plt.savefig('k-means initial.png')
    plt.show()


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
 
def k_means(points, k, max_iterations=500):
    centroids = rd.sample(points, k)
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for point in points:
            distances = [distance(point[0], point[1], centroid[0], centroid[1]) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroids.append(tuple(map(sum, zip(*cluster))))
                new_centroids[-1] = tuple(x / len(cluster) for x in new_centroids[-1])
            else:
                new_centroids.append(rd.choice(points))
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return centroids, clusters
    

def k_means_numpy(points, k, max_iterations=500):
    centroids = rd.sample(points, k)
    points = np.array(points)
    for _ in range(max_iterations):
        distances = np.array([np.linalg.norm(points - centroid, axis=1) for centroid in centroids])
        clusters = np.argmin(distances, axis=0)
        new_centroids = np.array([np.mean(points[clusters == i], axis=0) for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    clusters = [points[clusters == i] for i in range(k)]
    return centroids, clusters

def plot_clusters(points, centroids, clusters, filename, title):
    plt.figure()
    for i, cluster in enumerate(clusters):
        cluster_points = [point for point in points if point in cluster]
        plt.scatter([x for x, y in cluster_points], [y for x, y in cluster_points], s=4, label=f'Cluster {i+1}')
    plt.scatter([x for x, y in centroids], [y for x, y in centroids], s=10, color='black', label='Centroids')
    plt.legend()
    plt.title(title)
    plt.savefig(filename)
    plt.show()


def main():
    centroids = [(-5, 3), (4, -7), (1, 9), (10, -1)]
    points = generate_points(centroids)
    plot_initial(points, centroids)
    start_time = time.time()
    centroids, clusters = k_means(points, k=4)
    end_time = time.time()
    print(f'K-Means Clusters Time taken: {end_time - start_time:.6f} seconds')
    plot_clusters(points, centroids, clusters, 'k-means clusters.png', 'K-Means Clusters')
    start_time = time.time()
    centroids, clusters = k_means_numpy(points, k=4)
    end_time = time.time()
    print(f'K-Means Clusters (NumPy) Time taken: {end_time - start_time:.6f} seconds')
    plot_clusters(points, centroids, clusters, 'k-means numpy clusters.png', 'K-Means Clusters (NumPy)')


if __name__ == '__main__':
    main()