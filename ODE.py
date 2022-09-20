#Jacob Silveira
#CST-305
#9/18/2022

#the odeint function requires three arguments, model function, initial condition, and time to solve
#Dt is my function for time and dt = Nb(number of bits)/Tr(transmission rate)
#Dpr is propogation delay and is D(distance)/S(speed of the packet)
#no queing or propogation delays so +Dp and +Dq omitted 
#Number of bits: 5, 5000 mbs
#Transmission rate: 1000000
#Propagation delay:10ms

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(y,t):
    #t is time 
    #y is Dpr
    #k is Dt, transmission delay
    k = 5000/1000000
    dydt = k + y
    return dydt
#inital condition, propagation delay in ms, can change 10 to 100 ms to see a higher propagation delay
y0=10

t = np.linspace(0,50,100)

y = odeint(model,y0,t)

plt.plot(t,y)
plt.xlabel("time in ms")
plt.ylabel("propagation delay in mb")
plt.title("Network Latency")
plt.show()