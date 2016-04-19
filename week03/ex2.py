from numpy import array,empty
## Solve for values in a matrix using LU method
import numpy.linalg as lin

## Here are the 4 equations
print 'Here are the 4 equations:'
print '4V1 - V2 - V3 - V4 = V+'
print '- V1 + 4V2 - V3 - V4 = 0'
print '- V1 - V2 + 4V3 - V4 = V+'
print '- V1 - V2 - V3 + 4V4 = 0'

## We define two arrays, one for the matrix and another for the vector
A = array([[4, -1, -1, -1],
	[-1, 4, -1, -1], 
	[-1, -1, 4, -1],
	[-1, -1, -1,4]], float)
v = array ([1,0,1,0], float)
N = len(v)

## Gaussian elimination
for i in range(N):

	## We divide by diagonal element
	diagonal = A[i,i]
	A[i,:] /= diagonal
	v[i] /= diagonal

	##Subtract from the lower rows
	for j in range(i + 1, N):
		mult = A[j,i]
		A[j,:] -= mult * A[i,:]
		v[j] -= mult * v[i]

## Backsubstitution to get the four voltages
V = empty(N, float)
for i in range(N - 1, -1, -1):
	V[i] = v[i]
	for j in range(i + 1, N):
		V[i] -= A[i,j] * V[j]

print 'values from Gaussian Elimination: ', V

## Redefine the two arrays because they have been altered
## in the first part
A = array([[4, -1, -1, -1],
	[-1, 4, -1, -1], 
	[-1, -1, 4, -1],
	[-1, -1, -1,4]], float)
v = array ([1,0,1,0], float)
V = lin.solve(A,v)
print 'values from LU method from built in func: ', V
