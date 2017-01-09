#imports
import numpy as np
import math
def seedLCG(initVal):
    global rand
    rand = initVal

def lcg():
    a = 1140671485
    c = 128201163
    m = 2**24
    global rand
    rand = (a*rand + c) % m
    return rand

def rand_exp(l,p=10000.0):
    """ Donat el valor mitja l, proporciona un nombre aleatori que segueix
    una distribucio exponencial. """
    a = 0.0
    while a == 0:
        a = (lcg()%(p))/p
    return (-1.0/l) * math.log(a)

def rand_uni(p=10000.0):
    """ Donat el valor mitja l, proporciona un nombre aleatori que segueix
    una distribucio uniforme entre 0 i 1. """
    
    return (lcg()%(p))/p

seedLCG(1)

def stochastic_oscillation(x1,x2, Tmax=100):
    """ Given the initial conditions and the stop instant, it returns whether
    or not any of the variables has become null. 
    
    Input
    -------
    x1, x2: int; initial conditions for x1 and x2
    Tmax:   int (optional); stop instant.
    
    Output
    -------
    A boolean that is True in case some of the variables have disappeared and
    False in case none of them has."""
    
    t = 0;
    
    #ITERATION   
    while t < Tmax and ((x1 != 0) and (x2 != 0)):
        A = c1*x1+c2*x1*x2+c3*x2
        PA1 = c1*x1/A; PA2 = c2*x1*x2/A; PA3 = c3*x2/A;    

        p = rand_uni() #canviar

        if p < PA1:       #A1
            x1 += 1

        elif p < PA2+PA1: #A2
            x1 -= 1; x2 += 1;

        else:             #A3
            x2 -= 1

        #x1_v = np.append(x1_v,x1); x2_v = np.append(x2_v,x2);
        
        t += rand_exp(A)
        #t_v = np.append(t_v,t)

    if x1 == 0 or x2 == 0:
        return (1,t/Tmax)
    return (0, 1)
 
c20 = 0.0005; c21 = 0.05; N = 100; N2 = 100;
c1 = 1.0; c3 = 1.0;

c2_data = np.zeros(N); c2_temp = np.zeros(N); i = 0;
for c2 in np.linspace(c20,c21,N):
    xo = np.array([c3/c2, c1/c2])*1.2; #initial conditions
    #print "Començo c2 = %f" %c2
    for j in xrange(N2):
        (mor,tf) = stochastic_oscillation(int(xo[0]),int(xo[1]))
        c2_data[i] += mor
        c2_temp[i] += tf
        #print "N'he fet %d" %j
    i += 1;
    
    #print c2_data
    #print c2_temp
c2_data /= N2;
c2_temp /= N2;

#This code is relatively quick and can be executed in a feasible amount of time

import matplotlib.pyplot as plt
%matplotlib inline
fig = plt.figure(0)
plt.plot(np.linspace(c20,c21,N),c2_data)
plt.xlabel('c2')
plt.ylabel('Frequency of disappearance')
fig.savefig('P4b_freq.png')

fig = plt.figure(1)
plt.plot(np.linspace(c20,c21,N),c2_temp*tf)
plt.xlabel('c2')
plt.ylabel('Average disappearance time')
fig.savefig('P4b_time.png')
