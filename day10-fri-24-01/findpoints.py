import numpy as np
import matplotlib.pyplot as plt
import random as rd
import csv


def k_means(points, k, max_iterations=500):

    centroids = rd.sample(list(points), k)
    points = np.array(points)
    for _ in range(max_iterations):
        distances = np.array([np.linalg.norm(points - centroid, axis=1) for centroid in centroids])
        clusters = np.argmin(distances, axis=0)
        new_centroids = np.array([np.mean(points[clusters == i], axis=0) for i in range(k)])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    clusters = [points[clusters == i] for i in range(k)]
    return np.array(centroids), clusters


def  plot_clusters(clusters, centroids):
    plt.figure(figsize=(10, 10))
    for i, cluster in enumerate(clusters):
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='black', s=100, label='Centroids')
    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('K-Means Clustering')
    plt.savefig('k-means_clusters.png')
    plt.show()



def main():
    points =np.genfromtxt('points.csv', delimiter=',')

    x_min, x_max = points[:, 0].min(), points[:, 0].max()
    y_min, y_max = points[:, 1].min(), points[:, 1].max()

    k = 4
    centroids, clusters = k_means(points, k)
    plot_clusters(clusters, centroids)

    print("Bounds of the area:")
    print(f"x_min: {x_min}, x_max: {x_max}")
    print(f"y_min: {y_min}, y_max: {y_max}")
    print("Centroids:")
    for i, centroid in enumerate(centroids):
        print(f"Centroid {i+1}: {centroid}")


if __name__ == '__main__':
    main()