##Using Newton's method to solve for zeros
import numpy as np
import matplotlib.pyplot as plt
import pdb

## Creates a space from 0 to 1 with 20 bins
t = np.linspace(0,1,20)

def f(t):
	return (-3 * t**5) - (24 * t**4) + (3 * t) + 10

##Plot the function to find t near the zeros
y = np.asarray(f(t))
plt.plot(t,y)
plt.xlabel('Time [Gyr]')
plt.ylabel('Height')
plt.title('Height of a comet above the sun\'s equatorial plane vs time [Gyr]')
plt.show()

##Define the f'(t) function
def f_prime(t):
	return (-15 * t**4) - (96 * t**3) + 3

##From the graph the t = 0.77621 is close to 0
##Newton's Method
eps = 1
t0 = 0.77621
t_old = 1
i = 0
while abs(t_old - t0) > 10e-10:
	t_old = t0
	t0 = t_old - (f(t_old)/f_prime(t_old))
	i += 1
print 'The time in Gyr when the comet will cross the solar equator is t =',t0
print 'The number of steps for Newton\'s method is:', i

pdb.set_trace()

