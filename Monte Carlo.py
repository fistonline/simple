# matplotlib inline
from scipy import random
import numpy as np
import matplotlib.pyplot as plt

N = 30000

x = np.random.uniform(low=0, high=1, size=[N, 1])
y = np.random.uniform(low=0, high=1, size=[N, 1])

inside_bool = x ** 2 + y ** 2 < 1

approx_pi = 4 * np.sum(inside_bool) / N
print('Liczba pi: {}, około: {}'.format(np.pi, approx_pi))

x_in = x[inside_bool]
y_in = y[inside_bool]

plt.figure(figsize=[5, 5])
plt.scatter(x, y, s=1)
plt.scatter(x_in, y_in, color='r', s=1)
plt.show()
