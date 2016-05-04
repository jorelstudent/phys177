##Plotting the potential V = kQ/r
import numpy as np
import matplotlib.pyplot as plt
import pdb

##Defining constants and the function
k = 9 * 10**9
Q = -1
def f(r):

	return k * Q / r
##Declaring a 101 X 101 matrix for my z
z = np.zeros((101,101))
i = 0
j = 0
##Filling in my z matrix
while i < 101:
	while j < 101:
		if i == 50 and j == 50:
			z[i,j] = 0
			j += 1
			continue
		##Have to multiply each term by 10e-2 since we want to change 
		##from cm to m
		r = (np.sqrt((i - 50) ** 2 + (j - 50) ** 2)) * 10e-2
		z[i,j] = f(r)
		j += 1
	i += 1
	j = 0

plt.imshow(z,extent = [0, 100,0,100])
plt.xlabel('x in cm')
plt.ylabel('y in cm')
plt.title('Potential of a charge in 1m by 1m space')
plt.savefig('problem4.png')

pdb.set_trace()

