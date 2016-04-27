import numpy as np
from math import exp
import pdb
## Using Bisection method

## define function
def f(x):
	return (924. * x**6) - (2772. * x**5) + (3150. * x**4) - (1680. * x**3) + (420 * x**2) - (42 * x) + 1

## using the plot, I defined different x1 and x2 values with the zero
## in between them
x1 = [0.0241935, 0.1572, 0.352823, 0.592742, 0.798387, 0.961694]
x2 = [0.0423387, 0.1875, 0.417339, 0.667339, 0.854839, 0.97379]
i = 0

## make a while loop for each x1 and x2 pair, so more than one root is found, for bisection method
while i < len(x1):
	f1 = f(x1[i])
	f2 = f(x2[i])
	if f1 < 0. and f2 < 0.:
		print 'wrong initial values'
		pdb.set_trace() 
	if f1 > 0. and f2 > 0.:
		print 'wrong initial values'
		pdb.set_trace() 
	
	eps = 1.e-10

	j = 0
	while abs(x2[i]-x1[i])>eps:
		j += 1
		x3 = (x2[i] + x1[i]) / 2.
		f3 = f(x3)
	
	#if (f3 < 0. and f1<0.) or (f3 > 0. and f1>0.):
		if np.sign(f3) == np.sign(f1):
			x1[i] = x3
		if (f3 < 0. and f2<0.) or (f3 > 0. and f2>0.):
			x2[i] = x3

	solution = (x2[i]+x1[i]) / 2.
	print 'solution for',i + 1, 'root =', solution
	print 'number of steps =',j
	i += 1

pdb.set_trace() 
