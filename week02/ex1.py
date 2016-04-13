##Trapezoidal rule and Simpson's Rule from data points
import numpy as np

## have the user input how many bins it wants
N = input('Input the number of bins you want: ')
## Input a list of x and y values 
x_y = input('Input x and y values as a list, with each element in this form, [x,y]: ')
ex1dat = np.asarray(x_y,dtype = float)

## get min and max x values for a and b,respectively, and bin length
a = ex1dat[0,0]
list_length = len(x_y)
b = ex1dat[list_length - 1, 0]
h = (b-a) / N

## Apply trapezoidal rule
s = 0.5 * ex1dat[0,1] + 0.5 * ex1dat[list_length - 1, 1]
for k in range(1,N):
	y = ex1dat[int(a + (k * h)), 1]
	s += y
print 'Integral from Trapezoidal Rule', (h*s)

## Apply Simpson's Rule
s = ex1dat[0,1] + ex1dat[list_length - 1, 1]
for k in range(1,N,2):
	y = ex1dat[int(a + (k * h)), 1]
	s += 4 * y
for k in range(2,N,2):
	y = ex1dat[int(a + (k * h)), 1]
	s += 2 * y
print 'Integral from Simpson\'s Rule', (h* s / 3)
