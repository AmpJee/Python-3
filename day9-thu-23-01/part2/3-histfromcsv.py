import matplotlib.pyplot as plt
import numpy as np
import csv

realnumbers = np.genfromtxt('part2/values_for_hist.csv', delimiter=',')

plt.hist(realnumbers, bins=10, color='green', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
