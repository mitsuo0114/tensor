import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.arange(100)
np.random.seed(seed=1234)
y = np.random.normal(loc=x, scale=10)

y_true = x.copy()

plt.scatter(x, y, marker='o')
plt.plot(x, y_true, linestyle='--', linewidth=3, color='orange', label='True model')
plt.grid(which='major',color='black',linestyle=':')
plt.grid(which='minor',color='black',linestyle=':')
plt.ylabel('y')
plt.xlabel('x')
plt.legend(loc='best')
plt.savefig('build/figure.png')