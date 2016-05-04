## Create Fibonacci sequence
import pdb

##Create a list so I can get a list of the numbers
f_list = [1]
f0 = 0
f1 = 1
i = 1

##We let the list include 100 terms since we want to copmute f100 / f99

while i < 101:

	f2 = f0 + f1
	f_list.append(f2)
	f0 = f1
	f1 = f2
	i += 1
print 'The twelfth element of the series is', f_list[11]
print 'X100 / X99, where Xi is the ith element of the series is', float(f_list[99]) / float(f_list[98])

pdb.set_trace()

