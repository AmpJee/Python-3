import matplotlib.pyplot as plt
import random as rd
import math


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
    #plt.savefig('k-means initial.png')
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
    
def main():
    centroids = [(-5, 3), (4, -7), (1, 9), (10, -1)]
    points = generate_points(centroids)
    plot_initial(points, centroids)


if __name__ == '__main__':
    main()
