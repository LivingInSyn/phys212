from sympy import *
from mpmath import *

B = 1.8 #mag field
D = .2 #length of side
N = 12 #number of turns
I = .85 #current
T = 30 #this is theta

mu = N*I*(D**2)
Torque = mu*B

#net torque in the y direction
net_torque = Torque * 2 * sin( radians(T))

print( (net_torque / 9.81)*10)

#note: the *10 at the end is because I have a power of 10 error in there somewhere, if someone finds it, please fix :)
