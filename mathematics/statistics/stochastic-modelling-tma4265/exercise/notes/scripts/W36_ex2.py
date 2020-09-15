

import numpy as np
import matplotlib.pyplot as plt
import random

n = 365
A = np.zeros(n)

P = np.array([[0.7, 0.3 ],
              [0.25, 0.75]])

for i in range(1,n):
    r= random.uniform(0,1)
    if A[i-1] == 0:
      # if it rains, will it rain the day after
      A[i] = ( r < P[0,0])
    else:
      # if it doesnt rain, will it rain the day after
      A[i] = ( r < P[1,0])

rain = np.ones(n) - A
no_rain = A
t = np.arange(n)

n_rain = np.linalg.norm(rain,1)
n_no_rain = np.linalg.norm(no_rain,1)

print(n_rain, n_no_rain)
print(n_rain/n, n_no_rain/n)

#plt.scatter(t,rain)
#plt.scatter(t,no_rain)
#plt.legend()
#plt.show()
