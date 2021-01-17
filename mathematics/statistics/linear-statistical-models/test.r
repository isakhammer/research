# R program for matrix multiplication 

# 1a
# Creating matrices 
A <- matrix(, nrow=2, ncol=2) 
A[1,1] = 9
A[1,2] = -2
A[2,1] = -2
A[2,2] = 6

#1b
# Symmetric if this is true
t(A) == m

#1c
# Positive definitess if this is true
det(A) == 0

#1d 
# Find the eigen values and vectors
ev <- eigen(A)
values <- ev$values
U <- ev$vectors
D = diag(values)

#1e
# Find an orthogonal diagonalization of A
A_star = U %*% D %*% t(U) 
A_star == A

#1f
# Find inverse of matrix
A_inv = solve(A)
sum(A_inv %*% A - diag(2)) < 0.001

# Find eigen values of inverse matrix
ev = eigen(A_inv)
values <- ev$values
U_inv <- ev$vectors
D_inv = diag(values)


# 1h
# Why can A be a covariance matrix
# Because it is a square matrix and positive diagonal.


# 1i
S1 = diag(A)
S1 <- diag(S1)
S1_inv = solve(sqrt(S1))
B1 = S1_inv  %*%  A %*%  S1_inv
B = cov2cor(A)
sum(B1 - B) < 0.001 # equivalent

#1j

# Inital values
EX = matrix(1:2,2,1)
EX[1] = 3
EX[2] = 1
covX = A

# i) 
M = matrix(1:4,2,2)
M[1,1] = 1
M[1,2] = 1
M[2,1] = 1
M[2,2] = 2

Y = M %*% 





