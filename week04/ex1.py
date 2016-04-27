import numpy as np
from math import exp,log,sqrt
import pdb

## Using relax method, with 2 variables
def f(x,y):
	return y * (a + x**2)
def g(x,y):
	return b / (a + x**2)	

## defining the variables
a = 1.
b = 2.
x = 1.5
y = 0.5

## Relaxation method loop
for i in range(10):
	x = f(x,y)
	y = g(x,y)
	print 'x = ', x
	print 'y = ', y
""" 
There is no need to do the second part because the relaxation method already works after the first increment.
"""
pdb.set_trace()
