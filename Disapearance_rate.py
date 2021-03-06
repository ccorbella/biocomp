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
    
    #Initialization
    x1_v = np.array([x1]); x2_v = np.array([x2]); t = 0; t_v = np.array([t]) 
    
    #ITERATION   
    while t < Tmax and ((x1 != 0) and (x2 != 0)):
        x1,x2, t
        A = c1*x1+c2*x1*x2+c3*x2
        PA1 = c1*x1/A; PA2 = c2*x1*x2/A; PA3 = c3*x2/A;    

        p = rand_uni() #canviar

        if p < PA1:       #A1
            x1 += 1

        elif p < PA2+PA1: #A2
            x1 -= 1; x2 += 1;

        else:             #A3
            x2 -= 1

        x1_v = np.append(x1_v,x1); x2_v = np.append(x2_v,x2);
        
        t += rand_exp(A)
        t_v = np.append(t_v,t)

    if x1 == 0 or x2 == 0:
        return 1
    return 0
 
c20 = 0.000005; c21 = 0.001; N = 100; N2 = 100;
c3  = 1.0; c1 = 1.0

c2_data = np.empty(N); i = 0;
for c2 in np.linspace(c20,c21,N):
    xo = np.array([c3/c2, c1/c2])*1.2; #initial conditions
    for j in xrange(N2):
        c2_data[i] += stochastic_oscillation(xo[0],xo[1])
    i += 1;
    c2_data /= N2;
