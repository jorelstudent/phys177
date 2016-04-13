## Trap and Simp Rules for a function
import numpy as np
import scipy.integrate as integrate
## define function, upper and lower bounds, and bins
def f(x):
	return (x ** 4) - (2 * x) + 1
a = 0.
b = 2.
N = 20
h = (b-a) / N

## Apply trapezoidal rule
s = 0.5 * f(a) + 0.5 * f(b)
for k in range(1,N):
	y = f(a + (k * h))
	s += y
print 'Integral from Trapezoidal Rule', (h*s)

## Apply Simpson's Rule
s = f(a) + f(b)
for k in range(1,N,2):
	y = f(a + (k * h))
	s += 4 * y
for k in range(2,N,2):
	y = f(a + (k * h))
	s += 2 * y
print 'Integral from Simpson\'s Rule', (h* s / 3)

## Apply Trapezoidal Rule from Scipy
x = np.linspace(0, 2, num = 20)
int_trap = integrate.trapz(f(x), x)
print 'Integral from built in Trapezoidal Rule', int_trap

## Apply built in Simpson's Rule from Scipy
int_simp = integrate.simps(f(x), x)
print 'Integral from built in Simpson\'s Rule', int_simp

## Calculate errors
int_true = 22. / 5.
## Apply built in Trapz and Simps rule, for only 10 bins
x = np.linspace(0, 2, num = 10)
int_trap = integrate.trapz(f(x), x)
int_simp = integrate.simps(f(x), x)

## Error for built in Trapz Rule
error_trap = (1. / 3.) * (int_trap - int_true)
print 'Error in trapezoidal rule: ', error_trap

## Error for built in Simp Rule
error_simp = (1./ 15.) * (int_simp - int_true)
print 'Error in Simpson\'s Rule', error_simp
