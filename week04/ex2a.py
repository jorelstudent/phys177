import matplotlib.pyplot as plt
import numpy
import pdb

## create 100 spaced numbers between 0 and 1
x = numpy.linspace(0,1,100)
def f(x):
	return (924. * x**6) - (2772. * x**5) + (3150. * x**4) - (1680. * x**3) + (420 * x**2) - (42 * x) + 1

y = f(x)

##plotting the funciton
plt.plot(x,y)
plt.savefig('ex2.png', format = 'png')

pdb.set_trace()
