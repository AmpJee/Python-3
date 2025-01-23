import matplotlib.pyplot as plt
import numpy as np
import random as rd
import time

segments = np.array([[rd.randint(-10, 10), rd.randint(-10, 10), rd.randint(-10, 10), rd.randint(-10, 10)] for _ in range(500)])
regtangle = [-6, -6, 6, 6]


def filter_segment(regtangle, segment):
    x1, y1, x2, y2 = segment
    if (min(regtangle[0], regtangle[2]) <= x1 <= max(regtangle[0], regtangle[2]) 
        and min(regtangle[0], regtangle[2]) <= x2 <= max(regtangle[0], regtangle[2])
        and min(regtangle[1], regtangle[3]) <= y1 <= max(regtangle[1], regtangle[3])
        and min(regtangle[1], regtangle[3]) <= y2 <= max(regtangle[1], regtangle[3])):
            return True
    return False

def graph_plot(segments):
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 5))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    bx.set_xlim(-10, 10)
    bx.set_ylim(-10, 10)

    start = time.time()

    for segment in segments:
        x1, y1, x2, y2 = segment
        ax.plot([x1, x2], [y1, y2], color=np.random.rand(3))

    for segment in segments:
        x1, y1, x2, y2 = segment
        if filter_segment(regtangle, segment) == True:
            bx.plot([x1, x2], [y1, y2], color=np.random.rand(3))

    stop = time.time()

    plt.show()

    return stop - start

print(f"Time: {graph_plot(segments)}")