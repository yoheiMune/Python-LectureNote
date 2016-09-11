import numpy as np
import matplotlib.pyplot as plt

# X = np.loadtxt("automobile.txt", delimiter=",")
# x = X[:, 0]
# y = X[:, 1]
# plt.plot(x, y, "ro")
# plt.draw()
# plt.show()

t = np.arange(0, 10, 0.1)
def f(x):
    return x ** 2
plt.plot(t, f(t))
plt.show()