import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
from scipy.sparse import spdiags, linalg
from scipy import interpolate

def diag(a,b,c, n):
    A = a*np.ones(n)
    B = b*np.ones(n)
    C = c*np.ones(n)
    data    = np.vstack((A, B, C))
    diags   = np.array([-1, 0, 1])
    K = spdiags(data, diags, n, n, format = 'csc')
    return K


def ex1():

    def f(x):
        return 0.0*x

    # Inital values
    sigma = 0
    alpha = 0.0
    x0 = 0
    xend = 1 # or x_{M+1}
    M = 99
    h = (xend - x0)/(M + 1)

    # Discretize A matrix
    A = diag(1, -2, 1, M+1)
    A[-1, -3:] = np.array([-h/2, 2*h, -3*h/2])

    # Discretize input space
    # M + 2 because of start and end points.
    x = np.linspace(x0, xend, M+2)

    # Discretize F from x1 to xend
    F = f(x[1:])
    F[0] = F[0] - alpha/h**2
    F[-1] = sigma

    # Solve for U_i of i in { 1,..., M+1 }
    U = linalg.spsolve(A,F)

    # Append U_0, which is defined as sigma
    U = np.append([alpha], U )

    # Spline for plotting purposes
    U_spline = interpolate.CubicSpline(x, U)

    plt.plot( x, U, label="discretized")
    plt.plot( x, U_spline(x, 0), label="spline")
    plt.plot( x, U_spline(x, 1), label="spline first derivative")
    plt.legend()
    plt.show()


ex1()
