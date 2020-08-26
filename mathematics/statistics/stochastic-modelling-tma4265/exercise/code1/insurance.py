import numpy as np
import numpy

n=5000000 #Number of years
lam=6;mu=-2;sigma=1; 
C= [0]*n


for i in range(0,n):
    N=numpy.random.poisson(lam=lam, size=1) #Sample the number of insurance claims from the poisson distriution.
    C[i]=sum(numpy.random.lognormal(mean=mu, sigma=sigma, size=N)) #Sample the insurance amount claims from the lognormal distribution.

print("Expected value: ", numpy.mean(C))
print("Variance: " ,numpy.var(C))
