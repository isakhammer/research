import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
from scipy.sparse import spdiags, linalg

def diag(a,b,c, n):
    A = a*np.ones(n)
    B = b*np.ones(n)
    C = c*np.ones(n)

    data    = np.vstack((A, B, C))
    diags   = np.array([-1, 0, 1])
    K = spdiags(data, diags, n, n, format = 'csc')
    return K

def f(x):
    return x**2

g0 = 0
g1 = 1

n = 100
h = ( g1 - g0 )/n
K1 = diag(1, -2, 1, n-1)
K2 = diag(1, 0, -1, n-1)
K = K1 + K2

x = np.linspace(0,1, n-1)
F = f(x)
F[0]  += g0*( 1/h**2 + 1/( 2*h ))
F[-1] += g1*( 1/h**2 - 1/( 2*h ))
U = linalg.spsolve(K,F)

print(U)
plt.plot( U)
plt.show()

# K1 U + K2 U = f(x)



