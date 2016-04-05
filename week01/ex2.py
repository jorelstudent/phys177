import numpy as np
import matplotlib.pyplot as plt

## list all the grades in a list
## initialize to be floats because adding and dividing
hw = [10., 10., 8., 9.5, 3., 9., 0., 6.]
midterm = [10., 10., 10., 10., 8., 5., 10., 7.]
final = [9., 10., 10., 6., 10., 6., 8., 9.]  
avg_list = []
fail = 0.
outs = 0.

## we sum all the grades together for each individual student
## and average them by dividing by 3 in this case

i = 0
print 'Final Grades: '
while i < 8:
## we sum the grades and divide by 3, assume equal weight
	sum0 = hw[i] + midterm[i] + final[i]
	avg = sum0 / 3
## use if statements to denote how many failed or outstanding students
## as well as append list for histogram data
	avg_list.append(avg)
	print avg
	if avg_list[i] < 6:
		fail += 1
	if avg_list[i] > 9.5:
		outs += 1
	i += 1
print 'Number of failed students', fail
print 'Fraction of outstanding students', (outs/8)

## plot histogram
plt.hist(avg_list)
plt.title('Histogram of Grades')
plt.xlabel('Final Grade')
plt.ylabel('Frequency')

## save plot to file
plt.savefig('ex2.png', format = 'png')
