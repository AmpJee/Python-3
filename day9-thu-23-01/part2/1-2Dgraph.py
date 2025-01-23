import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):
    return x*y


def f2(x, y):
    return x**2 + y**2


def f3(x, y):
    return np.sin(3*x) * y


x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

Z1 = f1(X, Y)
Z2 = f2(X, Y)
Z3 = f3(X, Y)

fig = plt.figure(figsize=(15, 6))

ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z') 
ax1.set_title('x*y')


ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma')

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z') 
ax2.set_title('x**2 + y**2')


ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='twilight')

ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z') 
ax3.set_title('sin(3x)*y')

plt.tight_layout()
plt.show()