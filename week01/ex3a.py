## import package for square roots
import math

h = 800
v_i = input('Input the initial velocity [m/s]: ') 
t = (-v_i / 9.81) + math.sqrt(v_i ** 2 + 2 * h * 9.81) / 9.81
print 'Time [s] it takes to reach the ground: ', t
