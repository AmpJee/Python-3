import matplotlib.pyplot as plt
import numpy as np
import csv

integers = np.genfromtxt('part2/values_for_bars.csv', delimiter=',')
unique_values, frequencies = np.unique(integers, return_counts=True)

plt.bar(unique_values, frequencies)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
