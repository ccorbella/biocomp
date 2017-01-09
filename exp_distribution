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

import matplotlib.pyplot as plt
%matplotlib inline

vector_exp = np.empty(10000)
A = 0.05
import matplotlib.pyplot as plt
%matplotlib inline
for i in xrange(10000):
    vector_exp[i] = rand_exp(A)

print np.mean(vector_exp), np.var(vector_exp)
fig = plt.figure()
plt.xlim(0,100)
plt.hist(vector_exp, bins = 200)
x = np.linspace(0,100,10000)
plt.plot(x,10000*A*np.exp(-A*x), linewidth = 2)
plt.title(r'Exponential distribution for $\tau = 0.05 $', fontsize=16)
plt.ylabel('Frequency', fontsize=14)
fig.savefig('Exponential_distribution_t_0p05.png', bbox_inches='tight')


vector_exp = np.empty(10000)
A = 0.2
import matplotlib.pyplot as plt
%matplotlib inline
for i in xrange(10000):
    vector_exp[i] = rand_exp(A)

print np.mean(vector_exp), np.var(vector_exp)
fig = plt.figure()
plt.xlim(0,100)
plt.hist(vector_exp, bins = 200)
x = np.linspace(0,100,10000)
plt.plot(x,10000*A*np.exp(-A*x), linewidth = 2)
plt.title(r'Exponential distribution for $\tau = 0.2 $', fontsize=16)
plt.ylabel('Frequency', fontsize=14)
fig.savefig('Exponential_distribution_t_0p2.png', bbox_inches='tight')
