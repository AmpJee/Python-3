import matplotlib.pyplot as plt
import numpy as np
import random as rd

segments = np.array([[rd.randint(0, 10), rd.randint(0, 10), rd.randint(0, 10), rd.randint(0, 10)] for i in range(10)])
regtangle = [-10, -10, 10, 10]


def isregtangle(regtangle, segment):
    x1, y1, x2, y2 = segment
    if (min(regtangle[0], regtangle[2]) <= x1 <= max(regtangle[0], regtangle[2]) 
        and min(regtangle[0], regtangle[2]) <= x2 <= max(regtangle[0], regtangle[2])
        and min(regtangle[1], regtangle[3]) <= y1 <= max(regtangle[1], regtangle[3])
        and min(regtangle[1], regtangle[3]) <= y2 <= max(regtangle[1], regtangle[3])):
            return True
    return False

for segment in segments:
    x1, y1, x2, y2 = segment
    if isregtangle(regtangle, segment) == True:
        plt.plot([x1, x2], [y1, y2])


plt.show()