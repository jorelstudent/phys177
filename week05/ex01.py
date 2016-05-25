import numpy as np
from scipy import signal
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import pdb

##Define function for direct Fourier Transform
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

##For the square wave with amplitude 1 for one cycle
t = np.linspace(0, 2. * np.pi, 1000)

pulse = signal.square((t - 0.045)/1.975)
plt.subplot(2,1,1)
plt.plot(t,(pulse+1.) / 2.)
plt.title('Square Wave')

N = len(pulse)
pulse -= (np.sum(pulse) / float(N))
coeff = dft(pulse)
num_coeff = len(coeff)

plt.subplot(2,1,2)
plt.plot(np.arange(num_coeff), coeff)
plt.title('Fourier Coefficients for a Square Wave')
plt.show()


##For the sawtooth wave 
pulse = signal.sawtooth(t)
plt.subplot(2,1,1)
plt.plot(t,pulse)
plt.title('Sawtooth Wave')

N = len(pulse)
pulse -= (np.sum(pulse) / float(N))
coeff = dft(pulse)
num_coeff = len(coeff)

plt.subplot(2,1,2)
plt.plot(np.arange(num_coeff), coeff)
plt.title('Fourier Coefficients for a Sawtooth Wave')
plt.show()

## For the modulate sine wave sin(pi*n/N) * sin (20*pi*n/N)
N = len(t)
pulse = np.sin(np.pi * t/ N) * np.sin(20. * np.pi *t/ N)
plt.subplot(2,1,1)
plt.plot(t,pulse)
plt.title('Modulated Sine Wave')

pulse -= (np.sum(pulse) / float(N))
coeff = dft(pulse)
num_coeff = len(coeff)

plt.subplot(2,1,2)
plt.plot(np.arange(num_coeff), coeff)
plt.title('Fourier Coefficients for a Modulated Sine Wave')
plt.show()


pdb.set_trace()
