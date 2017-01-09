#Frequency and amplitude
#Conrad i Maria: Fig 3

#Functions
import numpy as np
def create_x_t_array(x_v,t_v,p=0.001):
    split_at = t_v.searchsorted(np.arange(0,t_v[-1],p))
    means    = np.array(map(np.mean,np.split(x_v, split_at)))
    return means[~np.isnan(means)]

#Mean amplitude
import math
from scipy import signal

def A_rms_freq(x_p, p=0.001):
    ff,  periodograma_x   = signal.periodogram(x_p,1.0/p , nfft = 2**20)
    f = ff[np.argmax(periodograma_x)]
    T = 1/f;
    T_indx = int(T/p)
    N = int(x_p.shape[0]/T_indx)
    f = 1.0/T_indx
    Arms = np.empty(N)

    
    for i in xrange(N):
        Arms[i] = math.sqrt(f*np.sum(x_p[i*T_indx: (i+1)*T_indx]**2))
    
    
    return np.mean(Arms), f
########################################################################
#Here the results of the Gillespie algorithm are imported.

#They were extremely long to calculate, but still, the code used was the following:
"""
import numpy as np
N = 10;
lin = np.linspace(1,3,N)
xo = [c3/c2 * lin, c1/c2 * lin];
T = 1.0/0.14
A_rms_X1 = np.empty(N); A_rms_X2 = np.empty(N)

for i in xrange(N):
    x1o, x2o = xo[0][i], xo[1][i]
    x1_v, x2_v, t_v = stochastic_oscillation(x1o,x2o)
    np.save('x1_1_v'+str(i), x1_v); np.save('x2_1_v'+str(i), x2_v); np.save('t_1_v'+str(i), t_v); 
    
    print "N'he fet %d" %i
"""
#This is for one single repetition for c = 1:3 (using 10 values)
#It was executed 10 times changing: np.save('x1_j_v'+str(i), x1_v); np.save('x2_j_v'+str(i), x2_v); np.save('t_j_v'+str(i), t_v); 

A = np.empty(10); f = np.empty(10)
p = 0.001;

for i in xrange(10):
    AA = np.empty(10); ff = np.empty(10)
    for j in xrange(10):
        x1_v = np.load('x1_'+str(j+1)+'_v'+str(i)+'.npy');
        x2_v = np.load('x2_'+str(j+1)+'_v'+str(i)+'.npy');
        t_v = np.load('t_'+str(j+1)+'_v'+str(i)+'.npy');
        x1_vp = create_x_t_array(x1_v, t_v, p); x2_vp = create_x_t_array(x2_v, t_v, p)
        AA[j], ff[j] = A_rms_freq(x1_vp)
        
    A[i] = np.mean(AA); f[i] = np.mean(ff)

np.save('A', A); np.save('f', f);

fig = plt.figure(0)
plt.plot(np.linspace(1,3,10),A) #Ferne varies
fig.savefig('amplitude.png')
fig = plt.figure(1)
plt.plot(np.linspace(1,3,10),f) #Ferne varies
fig.savefig('frequency.png')
    
