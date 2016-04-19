import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
x = []
y = []
i = 0
j = 0
pi = np.pi
e0 = 8.854187817

z = np.zeros((101,101))
##Make a while loop, to and add your two potentials together
##You get a different one for each value
while i <= 100:
	while j <= 100:
		
		r1 = np.sqrt((i - 50) ** 2 + (j - 40) ** 2)
		r2 = np.sqrt((i - 50) ** 2 + (j - 60) ** 2)
		## if statements because we can't divide by 0
		if i == 50 and j == 40:
			phi = - 1 / (4 * pi * e0 * r2)
			j += 1
			continue
		if i == 50 and j == 60:
			phi = 1 / (4 * pi * e0 * r1)
			j += 1
			continue
		
		phi1 = 1 / (4 * pi * e0 * r1)
		phi2 = -1 / (4 * pi * e0 * r2)
		phi = phi1 + phi2
		z[i, j] = phi
		j += 1
	x.append(i)
	y.append(i)
	i += 1
	j = 0

## plot it by first making x,y into a grid, then reshaping z
## I use imshow, since it looks nicer than colormesh
X, Y = np.meshgrid(x,y)
Z = z.reshape(X.shape)

plt.imshow(Z, extent = (np.amin(x), np.amax(x),np.amin(y),np.amax(y)),cmap = cm.hot)
## you can make it look simpler using plt.pcolormesh(X,Y,Z)
plt.gray()
plt.show()

## Take the partial derivatives w.r.t. x
h = 1.
N = len(X)

derivx = np.zeros((101,101))
i = 0
while i <= 100:
	while j <= 100:
		if i == 0 and j == 0:
			derivx[i,j] = (z[1,1] - z[0,0]) / h
			i += 1
			continue
		if i == N and j == N:
			derivx[i,j] = (z[i,j] - z[i - 1, j - 1]) / h
			i += 1
			continue
		if i == 0:
			derivx[i,j] = (z[1,j] - z[0,j]) / h
			j += 1
			continue
		if i == N - 1:
			derivx[i,j] = (z[i, j] - z[i - 1,j]) / h
			j += 1
			continue
		if j == 0:
			derivx[i,j] = (z[i,1] - z[i,0]) / h
			j += 1
			continue
		if j == N - 1:
			derivx[i,j] = (z[i,j] - z[i, j - 1]) / h
			j += 1
			continue
		derivx[i,j] = (z[i, j + 1] - z[i, j - 1]) / (2. * h)
		j += 1
	i += 1
	j = 0

## Take the partial derivatives w.r.t. y
h = 1.
N = len(Y)

derivy = np.zeros((101,101))
i = 0
while i <= 100:
	while j <= 100:
		if i == 0 and j == 0:
			derivy[i,j] = (z[1,1] - z[0,0]) / h
			i += 1
			continue
		if i == N and j == N:
			derivy[i,j] = (z[i,j] - z[i - 1, j - 1]) / h
			i += 1
			continue
		if j == 0:
			derivy[i,j] = (z[i,1] - z[i,0]) / h
			j += 1
			continue
		if j == N - 1:
			derivy[i,j] = (z[i,j] - z[i, j - 1]) / h
			j += 1
			continue
		if i == 0:
			derivy[i,j] = (z[1,j] - z[0,j]) / h
			j += 1
			continue
		if i == N - 1:
			derivy[i,j] = (z[i, j] - z[i - 1,j]) / h
			j += 1
			continue
		
		derivy[i,j] = (z[i + 1, j] - z[i - 1, j]) / (2. * h)
		j += 1
	i += 1
	j = 0

## Make 2 plots, one for dx and one for dy. This is for dx
plt.subplot(2,1,1)
plt.imshow(derivx, extent = (np.amin(x), np.amax(x),np.amin(y),np.amax(y)),cmap = cm.hot)
plt.ylabel('dx')
plt.gray()
##Plot the plot of dy
plt.subplot(2,1,2)
plt.imshow(derivy, extent = (np.amin(x), np.amax(x),np.amin(y),np.amax(y)),cmap = cm.hot)
plt.ylabel('dy')
plt.gray()
plt.show()
