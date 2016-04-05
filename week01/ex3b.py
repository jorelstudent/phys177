import numpy as np
import matplotlib.pyplot as plt
## import package for square roots
import math

h = 800
vmin = input('Input the minimum initial velocity[m/s]: ')
vmax = input('Input the maximum initial velocity[m/s]: ')
##initialize v to vmin
v = vmin

## make a list of time and velocities
t_list = []
v_list = []
## Get the difference and divide it by 9, so it runs from 0 to 10
## Don't forget to make ascii file, aka .txt file
interval = (vmax - vmin) / 9.
while v < vmax:
	t = (-v / 9.81) + math.sqrt(v ** 2 + 2 * h * 9.81) / 9.81
	t_list.append(t)
	v_list.append(v)
	print 'Time: ', t
	print 'Velocity: ', v
	v += interval

ex3bdat = np.asarray((v_list, t_list))
np.savetxt('ex3b.dat',ex3bdat)
##plot and save
plt.plot(v_list, t_list)
plt.xlabel('Initial Velocity')
plt.ylabel('Time')
plt.savefig('ex3b.png', format = 'png')

