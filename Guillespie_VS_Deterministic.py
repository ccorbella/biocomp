import numpy as np
import math
import random

def deterministic_evolution(alpha0,T=50):
    dt = 0.001; N = int(T/dt)

    K = 1; alpha1 = 100; n = 2; gamma = 1; beta = 5; delta = 5;
    mm1 = np.zeros(N); mm2 = np.zeros(N); mm3 = np.zeros(N);
    pp1 = np.zeros(N); pp2 = np.zeros(N); pp3 = np.zeros(N);

    #Initialization
    m1 = 0; m2 = 0; m3 = 1; p1 = 0; p2 = 0; p3 = 0;

    for i in xrange(N):
        dm1 = dt*(alpha1*K**n/(K**n+p3**n) - gamma*m1 + alpha0)
        dm2 = dt*(alpha1*K**n/(K**n+p1**n) - gamma*m2 + alpha0)
        dm3 = dt*(alpha1*K**n/(K**n+p2**n) - gamma*m3 + alpha0)
        dp1 = dt*(beta*m1 - delta*p1)
        dp2 = dt*(beta*m2 - delta*p2)
        dp3 = dt*(beta*m3 - delta*p3)

        #Update
        m1 += dm1; m2 += dm2; m3 += dm3; p1 += dp1; p2 += dp2; p3 += dp3;
        mm1[i] = m1; mm2[i] = m2; mm3[i] = m3;
        pp1[i] = p1; pp2[i] = p2; pp3[i] = p3;
    
    t = np.linspace(0,T,N)
    return mm1, mm2, mm3, pp1, pp2, pp3, t

def guillespie_evolution(V,alpha0,T=50):
    K = 1; alpha1 = 100; n = 2; gamma = 1; beta = 5; delta = 5;
    K *= V; alpha1 *= V; alpha0 *= V; #Considering the volume: passing concentrations into #Moleculles

    m1o=200; m2o=0; m3o=0; p1o=0; p2o=0; p3o=0; #inital conditions (#Mollecules)

    MM1   = np.empty(1); MM1[0]   = m1o; m1 = m1o;
    MM2   = np.empty(1); MM2[0]   = m2o; m2 = m2o;
    MM3   = np.empty(1); MM3[0]   = m3o; m3 = m3o;
    PP1   = np.empty(1); PP1[0]   = p1o; p1 = p1o;
    PP2   = np.empty(1); PP2[0]   = p2o; p2 = p2o;
    PP3   = np.empty(1); PP3[0]   = p3o; p3 = p3o;
    TIMES = np.empty(1); TIMES[0] = 0;   t = 0;

    Kn = K**n

    while t < T:
        b1  = beta*m1;  b2  = beta*m2;  b3  = beta*m3
        g1  = gamma*m1; g2  = gamma*m2; g3  = gamma*m3;
        d1  = delta*p1; d2  = delta*p2; d3  = delta*p3;
        a1  = alpha0 + alpha1*Kn/(Kn+p3**n)
        a2  = alpha0 + alpha1*Kn/(Kn+p1**n)
        a3  = alpha0 + alpha1*Kn/(Kn+p2**n)
        rs  = b1+b2+b3+g1+g2+g3+a1+a2+a3+d1+d2+d3;
        t  += random.expovariate(rs)

        r   = random.random()

        if   r < b1/rs:
            p1 += 1.0
        elif r < (b1+b2)/rs:
            p2 += 1.0
        elif r < (b1+b2+b3)/rs:
            p3 += 1.0
        elif r < (b1+b2+b3+g1)/rs:
            m1 -= 1.0
        elif r < (b1+b2+b3+g1+g2)/rs:
            m2 -= 1.0
        elif r < (b1+b2+b3+g1+g2+g3)/rs:
            m3 -= 1.0
        elif r < (b1+b2+b3+g1+g2+g3+a1)/rs:
            m1 += 1.0
        elif r < (b1+b2+b3+g1+g2+g3+a1+a2)/rs:
            m2 += 1.0
        elif r < (b1+b2+b3+g1+g2+g3+a1+a2+a3)/rs:
            m3 += 1.0
        elif r < (b1+b2+b3+g1+g2+g3+a1+a2+a3+d1)/rs:
            p1 -= 1.0
        elif r < (b1+b2+b3+g1+g2+g3+a1+a2+a3+d1+d2)/rs:
            p2 -= 1.0
        elif r < (b1+b2+b3+g1+g2+g3+a1+a2+a3+d1+d2+d3)/rs:
            p3 -= 1.0

        MM1   = np.append(MM1,m1);
        MM2   = np.append(MM2,m2);
        MM3   = np.append(MM3,m3);
        PP1   = np.append(PP1,p1);
        PP2   = np.append(PP2,p2);
        PP3   = np.append(PP3,p3);
        TIMES = np.append(TIMES,t)
        
    return MM1, MM2, MM3, PP1, PP2, PP3, TIMES
