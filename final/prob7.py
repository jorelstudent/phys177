import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft, irfft
import scipy
import matplotlib.animation as animation
import pdb

## define the global variables
m = 9.109e-31 ## in kg
hbar = 1.0545718e-34 ## in (m ** 2)kg/s
L = 10. ** -8 ## in m
sigma = 1.e-10 ## in m
kappa = 5.e10 ## in m ** -1
x_0 = L/2. ## in m
N = 1000
## PART A of prob 9.7
## create 1000 spaced box from 0 to L
x = np.linspace(0, L, N)
## Create another 1000 spaced object from 0 to N
p = np.linspace(0, N, N)


##define the function for t = 0
## USE THE DISCRETE FUNCTION
def psi(x):
	psi = np.exp(- ((x-x_0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * kappa * x)
	return psi

psi_x = psi(x)
## Keep boundary conditions
psi_x[0] = 0.
psi_x[L] = 0.
##create the two arrays containing the real and imaginary parts of psi(x,0)
psi_real = psi_x.real
psi_imag = psi_x.imag

##Use discrete sine transforms, for a 1D, so we define that and its inverse
def dst(y):
	n = len(y)
	y2 = np.empty(2 * n, float)
	y2[0] = y2[n] = 0.0
	y2[1:n] = y[1:]
	y2[:n:-1] = -y[1:]
	a = np.imag(rfft(y2))[:n]
	a[0] = 0.0
	return a
	
def idst(a):
	n = len(a)
	c = np.empty(n + 1, complex)
	c[0] = c[n] = 0.0
	c[1:n] = -1j * a[1:]
	y = irfft(c)[:n]
	y[0] = 0.0
	return y

## We perform the discrete sine transform to each array, so we calculate alpha_k and eta_k for each point, since b_k = alpha_k + i * eta_k
alpha_k = dst(psi_real)
eta_k = dst(psi_imag)

## PART B of problem 9.7

## We define the real part of the wavefunction

def real_psi(p, t):
	s = 0.
	for k in range(1, N - 1):
		y = (alpha_k[k] * np.cos(((np.pi ** 2) * hbar * (k ** 2) * t) / (2 * m * (L**2))) \
		     - eta_k[k] * np.sin(((np.pi ** 2) * hbar * (k ** 2) * t) / (2 * m * (L**2)))) \
		     * np.sin(np.pi * k * p / N)
		s += y
	real_psi = (1. / N) * s
	return real_psi

t = 5.e-17
psi_x = real_psi(p,t)

psi_inv = idst(psi_x)
plt.plot(p,psi_inv)
plt.show()

b_k = np.vectorize(complex)(alpha_k, eta_k)


## PART C how to make an animation

t = np.linspace(0,1.e-16,100)
arr = np.zeros((N,100))
for i in range(100):
	psi_x = real_psi(p,t[i])
	psi_inv = idst(psi_x)
	arr[:,i] = psi_inv

fig3 = plt.figure(3)
fig3,ax = plt.subplots()

plt.xlim(0,1000)
plt.ylim(-0.02,0.02)

line, = ax.plot(p,psi_inv)

def animate(i):
	line.set_ydata(arr[:,i])
	return line,

ani = animation.FuncAnimation(fig3, animate, np.arange(1, 100),interval=300)


plt.show()


pdb.set_trace()
