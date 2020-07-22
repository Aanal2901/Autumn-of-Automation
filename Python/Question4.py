import numpy as np
X = np.random.normal(0, 1, size=(20,20))
#print(X)
y = np.random.normal(size = 20).astype('int32')
#print(y)

a = np.dot(X.transpose(), X)
b = np.dot(X.transpose(), y)
a_inv = np.linalg.inv(a)
theta = np.dot(a_inv, b)
#theta = np.dot(np.linalg.inv(np.dot(X.transpose(), X)), np.dot(X.transpose(), y))
print(theta)