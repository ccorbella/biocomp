#Final
import numpy as 
def create_x_t_array(x_v,t_v,p=0.001):
    """ In order to compute the FFT, the data provided had to be given
    every certain fixed time step. Otherwise, the results obtained would
    have been pointless. We could have taken samples using the smallest of
    the time scales and we would not have lost any resolution but the resulting
    vectors would be too large to be processed fast enough.
    
    Therefore, given two arrays, one for the time steps between every computation
    of x_v (that will be called t_v) and x_v itself, this function computes the
    average value every p time steps of x_v.
    
    Input
    -------
    x_v: numpy vector; a vector
    t_v: numpy vector; a vector with the instants at which the values of x_v 
    have been computed
    p:   float; period of sampling
    
    Output
    -------
    A numpy vector with the results."""
    split_at = t_v.searchsorted(np.arange(0,t_v[-1],p))        #Finding the split positions from the vector t_v
    means    = np.array(map(np.mean,np.split(x_v, split_at)))  #Computation of the mean of the splitted x_v subvectors
    #NaN subvectors would appear in case p < Delta t. Then, there would be no samples to average.
    return means[~np.isnan(means)]                             #Providing the results (except for the NaN subvectors)

#Mean amplitude
import math
from scipy import signal

def A_rms_freq(x_p, p=0.001):
    """ Given an array, it computes the RMS amplitude of the signal and
    its frequency.
     The frequency has been proved to be practically uniform, so it is
    used in order to split the signal into its different repetitions. After
    doing so, the amplitude is computed using the RMS formula.
    
    Input
    --------
    x_p: numpy vector; a vector
    p:   float; period of sampling
    
    Output
    --------
    amp: float; the mean RMS amplitude
    f:   float; the frequency"""
    ff,  periodograma_x   = signal.periodogram(x_p,1.0/p , nfft = 2**20)
    f = ff[np.argmax(periodograma_x)] # Finding the frequency of the signal from the periodogram
    T = 1/f;                          # Period of the signal
    T_indx = int(T/p)                 # Period index inside the array
    N = int(x_p.shape[0]/T_indx)      # Number of periods of the array
    f = 1.0/T_indx
    Arms = np.empty(N)
    
    for i in xrange(N):
        Arms[i] = math.sqrt(f*np.sum(x_p[i*T_indx: (i+1)*T_indx]**2)) #RMS formula computation
    
    return np.mean(Arms), f

A = np.empty(10); f = np.empty(10)
p = 0.001;

for i in xrange(10):
    AA = np.empty(10); ff = np.empty(10)
    for j in xrange(10):
        x1_v = np.load('x1_'+str(j+1)+'_v'+str(i)+'.npy');
        x2_v = np.load('x2_'+str(j+1)+'_v'+str(i)+'.npy');
        t_v = np.load('t_'+str(j+1)+'_v'+str(i)+'.npy');
        # Combining both funcitons above, this small program computes the average
        #amplitude and the frequency of the signal.
        x1_vp = create_x_t_array(x1_v, t_v, p); x2_vp = create_x_t_array(x2_v, t_v, p)
        AA[j], ff[j] = A_rms_freq(x1_vp)
        
    A[i] = np.mean(AA); f[i] = np.mean(ff)
    np.save('A'+str(i),A [i]); np.save('f'+str(i), f[i]);
