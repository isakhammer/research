import numpy as np
import matplotlib.pyplot as plt

P = np.array([[1, 0, 0], [0.05, 0.8, 0.15], [0, 0, 1]])
N = 100

for n in range(0, N):
    P = P.dot(P)

plt.bar(range(1,4), P[1,...])