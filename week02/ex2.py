##Trapezoidal rule and Simpson's Rule from data set
import numpy as np
import matplotlib.pyplot as plt

## number of bins is 102 because from t = 0 to t = 100
N = 102
## opens a velocities.txt
x_y = np.loadtxt('velocities.txt')
t = x_y[:, 0]
v = x_y[:, 1]

ex2dat = np.asarray((t,v))

## get min and max x values for a and b,respectively, and bin length
a = ex2dat[0,0]
list_length = len(t)
dist_trap = []

b = ex2dat[0, list_length - 1]
h = (b-a) / N

## Apply trapezoidal rule
s = 0.5 * ex2dat[1,0] + 0.5 * ex2dat[1, list_length - 1]
for k in range(1,N):
	y = ex2dat[1, int(a + (k * h))]
	s += y
	dist_trap.append(s)
print 'Integral from Trapezoidal Rule', (h*s)
i_trap = open('i_trap.txt','w')
i_trap.write(str(h*s))
i_trap.close()


## Apply Simpson's Rule
s = ex2dat[1,0] + ex2dat[1, list_length - 1]
for k in range(1,N,2):
	y = ex2dat[1, int(a + (k * h))]
	s += 4 * y
for k in range(2,N,2):
	y = ex2dat[1, int(a + (k * h))]
	s += 2 * y
print 'Integral from Simpson\'s Rule', (h* s / 3)
i_simp = open('i_simp.txt','w')
i_simp.write(str((h*s/3)))
i_simp.close()

## Plotting the stuffs
## Plotting velocity vs time
plt.subplot(2,1,1)
plt.plot(t,v)
plt.ylabel('Velocity')
##STILL NEED TO PLOT distanve vs time
plt.subplot(2,1,2)
plt.plot(t, dist_trap)
plt.ylabel('Distance from Trap')
plt.xlabel('Time')
plt.show()
