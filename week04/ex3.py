import numpy as np
import pdb
## Using Secant method

## define function
def f(x):
	return x**2 - (4 * x * np.sin(x)) + (2 * np.sin(x))**2

## define the derivative of the function
def f_prime(x):
	return 2*x - (4 * np.sin(x)) - (4 * x * np.cos(x)) + (8 * np.sin(x) * np.cos(x))

## taken from a plot of the function; points where the zeros are near
x = [-2., 0.1, 2.]
i = 0

## make a while loop for each x, so more than one root is found
while i < len(x):
	
	eps = 1.e-10
	x_old = -1
	j = 0
	while abs(x[i] - x_old)>eps:
		j += 1
		x_old = x[i]
		x[i] = x_old - (f(x_old) / f_prime(x_old))

	solution = x[i]
	print 'solution for',i + 1, 'root =', solution
	print 'number of steps =',j
	i += 1

pdb.set_trace() 
