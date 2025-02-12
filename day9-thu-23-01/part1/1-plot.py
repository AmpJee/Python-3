import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**2

def f2(x):
    return x * np.sin(2*x)


def f3(x):
    return np.arctan(x)


x = np.linspace(-2, 2, 100)
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

plt.plot(x, y1, label='Parabola', color='green', marker='o', markersize=2)
plt.plot(x, y2, label='Sine Curve', color='red', linestyle='dashed', marker='o', markersize=2)
plt.plot(x, y3, label='Inverse Tangent', color='pink', linestyle='dotted', marker='o', markersize=2)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Functions')
plt.legend()
plt.show()