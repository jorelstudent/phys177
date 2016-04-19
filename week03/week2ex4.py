## Trap Rules and Error Analysis
import numpy as np
import scipy.integrate as integrate
## define function, upper and lower bounds, and bins
def f(x):
	return np.sin(np.sqrt(100 * x)) ** 2
error_trap = 1
N = 10
## taken from actual integration
int_error = (1./400.)*(201. - 20. * np.sin(20.) - np.cos(20.))
a = 0.
b = 1.

while abs(error_trap) > 10 ** -6:
	print 'Number of slices: ', N
	h = (b-a) / float(N)

	## Apply trapezoidal rule
	s = 0.5 * f(a) + 0.5 * f(b)
	for k in range(1,N):
		y = f(a + (k * h))
		s += y
	s_adj = 0
	for k in range(1,N,2):
		y = f(a + (k * h))
		s_adj += y
	print 'Integral from Trapezoidal Rule: ',(1./2.) * h*s + (h*s_adj)
	int_trap = (1./2.)* h * s + (h*s_adj)

	## Calculate errors
	int_true = 22. / 5.
	
	## Error for built in Trapz Rule
	error_trap = (1. / 3.) * (int_trap - int_error)
	print 'Error in trapezoidal rule: ', error_trap
	N = 2 * N



