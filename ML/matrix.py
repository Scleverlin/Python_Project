import numpy as np
import matplotlib.pyplot as plt
# A function to create a dataset.
from sklearn.datasets import make_regression
# A library for data manipulation and analysis.
import pandas as pd

print (np.random.seed(3)) 

m = 30
X, Y = make_regression(n_samples=m, n_features=1, noise=20, random_state=1)
X = X.reshape((1, m))
Y = Y.reshape((1, m))
print('Training dataset X:')
print(X)
print('Training dataset Y')
print(Y)

print (X.shape) # rows, columns


