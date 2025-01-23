import matplotlib.pyplot as plt
import numpy as np
import random as rd
import time

segments = []
for i in range(1000):
    x1 = rd.randint(-10, 10)
    y1 = rd.randint(-10, 10)
    x2 = rd.randint(-10, 10)
    y2 = rd.randint(-10, 10)
    segments.append([x1, y1, x2, y2])
regtangle = [-6, -6, 6, 6]


def filter_segment(regtangle, segment):
    x1, y1, x2, y2 = segment
    if (min(regtangle[0], regtangle[2]) <= x1 <= max(regtangle[0], regtangle[2]) 
        and min(regtangle[0], regtangle[2]) <= x2 <= max(regtangle[0], regtangle[2])
        and min(regtangle[1], regtangle[3]) <= y1 <= max(regtangle[1], regtangle[3])
        and min(regtangle[1], regtangle[3]) <= y2 <= max(regtangle[1], regtangle[3])):
            return True
    return False


def numpy_filter_segment(regtangle, segments):
    x_min, y_min, x_max, y_max = regtangle
    segments = np.array(segments)
    x1, y1, x2, y2 = segments[:, 0], segments[:, 1], segments[:, 2], segments[:, 3]
    mask = (x1 <= x_max) & (x1 >= x_min) & (x2 <= x_max) & (x2 >= x_min) & (y1 <= y_max) & (y1 >= y_min) & (y2 <= y_max) & (y2 >= y_min)
    return segments[mask]


def graph_plot(segments):
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 5))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    bx.set_xlim(-10, 10)
    bx.set_ylim(-10, 10)

    for segment in segments:
        x1, y1, x2, y2 = segment
        ax.plot([x1, x2], [y1, y2], color=np.random.rand(3))

    for segment in segments:
        x1, y1, x2, y2 = segment
        if filter_segment(regtangle, segment) == True:
            bx.plot([x1, x2], [y1, y2], color=np.random.rand(3))

    plt.show()


filter = []
start = time.time()
for segment in segments:
        x1, y1, x2, y2 = segment
        if filter_segment(regtangle, segment) == True:
            filter.append(segment)
stop = time.time()
print(f"Original Time: {stop - start}")

start = time.time()
numpy_filter_segment(regtangle, segments)
stop = time.time()
print(f"Numpy Time: {stop - start}")
graph_plot(segments)
