import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
from scipy.sparse import spdiags

def diag(a,b,c, n):
    A = a*np.ones(n)
    B = b*np.ones(n)
    C = c*np.ones(n)

    data    = np.vstack((A, B, C))
    diags   = np.array([-1, 0, 1])
    K = spdiags(data, diags, n, n)
    return K

K1 = diag(1, -2, 1, n=100)
K2 = diag(1, 0, -1, n=100)

print(K1.toarray(),"\n", K2.toarray())





