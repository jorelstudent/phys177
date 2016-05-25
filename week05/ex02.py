import numpy as np
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import pdb
## Load the data file
filein = 'sunspots.txt'
data = np.loadtxt(filein)

##Plot the function
t = data[:,0]
y = data[:,1]
plt.plot(t,y)
plt.xlabel('Month')
plt.ylabel('Observed # of Sunspots')
plt.title('Observed # of Sunspots vs Months')
plt.show()

## The estimated period around 125 months
## Get the Fourier Transform from the Fourier coefficients
## Plot the full power spectrum
N = len(t)
y -= (np.sum(y)/float(N))
coeff = rfft(y)
num_coeff = len(coeff)
plt.plot(np.arange(num_coeff),np.abs(coeff)**2)
plt.xlabel('Frequency')
plt.ylabel('$|c_k|^2$')
plt.title('Full Power Specturm')
plt.show()

##From here we see that peak approximately corresponds to the value 24
##To get the cycle, we get the total number of months, which is 3142
print 'The approximate length of the cycle is', 3142/24
pdb.set_trace()
