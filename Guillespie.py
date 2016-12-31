#imports
import numpy as np
import math
import matplotlib.pyplot as plt
%matplotlib inline

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
    """ It provides random float numbers that follow an exponential distribution of 1/l mean.
    
    Input
    --------
    l: float, The mean of the exponential distribution.
    p: float, Precision.
    
    Output
    --------
    A random float following the exponential random distribution.
    
    Test
    --------
    >>>vector_exp = np.empty(10000)
    >>>A = 0.05
    >>>for i in xrange(10000):
    >>>    vector_exp[i] = rand_exp(A)
    >>>(np.mean(vector_exp) - 1/A) < 0.5, (np.var(vector_exp) - (1/A)**2) < 4
    (True, True)"""
    
    # In order to compute a random number that follows an exponential distribution, 
    #first a random number that follows a uniform distribution is calculated.
    #Then, we compute its logarithm. Just to prevent it broke in case the random number
    #got was 0, that case is taken into consideration and another random number is
    #computed.
    # Ideally, in a continue distribution, the probability to have a 0 should be null.
    #The fact is that we are having a finite precision and, therefore, its probability
    #to occur is far bigger.
    a = 0.0
    while a == 0:
        a = (lcg()%(p))/p
    return (-1.0/l) * math.log(a)


def rand_uni(p=10000.0):
    """ It provides random float numbers that follow an uniform distribution between 0 and 1.
    
    Input
    --------
    p: float, Precision.
    
    Output
    --------
    A random float following a uniform random distribution between 0 and 1.
    
    Test
    --------
    >>>vector_uni = np.empty(10000)
    >>>for i in xrange(10000):
    >>>    vector_uni[i] = rand_uni(A)
    >>>(np.mean(vector_uni) - 0.5) < 0.05
    True"""
    
    return (lcg()%(p))/p

seedLCG(1)

#GILLESPIE ALGORITHM
def Guillespie():
  #Constants
  c1 = 1.0; c2 = 0.0005; c3 = 1.0;
  x1 = 1000.0; x2 = 1000.0; t = 0;
  Tmax = 100

  x1_v = np.array([x1]); x2_v = np.array([x2])
  t_v = np.array([t]) 

  #ITERATION   
  while t < Tmax and ((x1 != 0) and (x2 != 0)):
      A = c1*x1+c2*x1*x2+c3*x2
      PA1 = c1*x1/A; PA2 = c2*x1*x2/A; PA3 = c3*x2/A;    

      p = rand_uni()

      if p < PA1:       #A1
          x1 += 1

      elif p < PA2+PA1:     #A2
          x1 -= 1; x2 += 1;

      else:             #A3
          x2 -= 1

      x1_v = np.append(x1_v,x1); x2_v = np.append(x2_v,x2);

      t += rand_exp(A)
      t_v = np.append(t_v,t)

  if x1 == 0:
          print "The particles X1 have totally disappeared"
  elif x2 == 0:
          print "The particles X2 have totally disappeared"

  np.save('x1_v',x1_v); np.save('x2_v',x2_v); np.save('t_v',t_v)
