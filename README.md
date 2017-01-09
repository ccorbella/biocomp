# Cell Project
## Guillespie module
This is the first module that must be imported and used. Using a self-created random number generator, it computes the Guillespie evolution of the next system:

![equation](http://latex.codecogs.com/gif.latex?X_1%20%5Crightarrow%202%B7X_2)
![equation](http://latex.codecogs.com/gif.latex?X_1%20&plus;%20X_2%20%5Crightarrow%202%B7X_2)
![equation](http://latex.codecogs.com/gif.latex?X_2%20%5Crightarrow%200)

The results are saved in vectors that, after its proper import, can be plotted using instructions such as:
```python
import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(t_v,x1_vi) #To find the x1 evolution of the vector i
plt.plot(t_v,x2_vi) #To find the x2 evolution of the vector i
plt.plot(x1_vi,x2_vi)
```

Note that the random numbers are computed using m = 2^b because this allows the modulus operation to be computed by merely truncating all but the rightmost **b** bits:
```latex
X_{n}    = a X_{n} + c
X_{n+1} = X_{n} - (X_{n} << b) >> b
```

Taking b = 32, it can be rewritten as:
```latex
X_{n+1} = (a X_{n} + c) \& \text{0xFFFFFFFF}
```

### Amplitude module
In order to work with the 'Amplitude' module, the vectors must have been first created and imported using the first module.
Finally, to show the results something such as:
```python
import numpy as np
x1_v0 = np.load('x1_v0.npy'); x2_v0 = np.load('x2_v0.npy'); t_v0 = np.load('t_v0.npy');
x1_v1 = np.load('x1_v1.npy'); x2_v1 = np.load('x2_v1.npy'); t_v1 = np.load('t_v1.npy');
x1_v2 = np.load('x1_v2.npy'); x2_v2 = np.load('x2_v2.npy'); t_v2 = np.load('t_v2.npy');
x1_v3 = np.load('x1_v3.npy'); x2_v3 = np.load('x2_v3.npy'); t_v3 = np.load('t_v3.npy');
x1_v4 = np.load('x1_v4.npy'); x2_v4 = np.load('x2_v4.npy'); t_v4 = np.load('t_v4.npy');
x1_v5 = np.load('x1_v5.npy'); x2_v5 = np.load('x2_v5.npy'); t_v5 = np.load('t_v5.npy');
x1_v6 = np.load('x1_v6.npy'); x2_v6 = np.load('x2_v6.npy'); t_v6 = np.load('t_v6.npy');
x1_v7 = np.load('x1_v7.npy'); x2_v7 = np.load('x2_v7.npy'); t_v7 = np.load('t_v7.npy');
x1_v8 = np.load('x1_v8.npy'); x2_v8 = np.load('x2_v8.npy'); t_v8 = np.load('t_v8.npy');
x1_v9 = np.load('x1_v9.npy'); x2_v9 = np.load('x2_v9.npy'); t_v9 = np.load('t_v9.npy');

import matplotlib.pyplot as plt
%matplotlib inline

fig = plt.figure(0)
plt.plot(np.linspace(1,10,10),A)
plt.xlabel('c',fontsize=16)
plt.ylabel('Amplitude',fontsize=16)

plt.savefig('amplitude.png')

fig = plt.figure(1)
plt.plot(np.linspace(1,10,10),f)
plt.xlabel('c',fontsize=16)
plt.ylabel('Frequency',fontsize=16)

plt.savefig('frequency.png')
```

is recommended to plot the amplitudes (for the first case) and the frequencies (for the second).

### Disappearance rate module
The disappearance rate module is just a program that computes the stochastic evolution for values of c_2 close to 0.005.

## Oscillating biochemical reaction 
Here, the evolution of an oscillating reaction is computed both in a deterministic and an stochastic way. To compute them and import the necessary modules, instructions such as those can be used:

```python
alpha0 = 1.8; T = 50;
mm1, mm2, mm3, pp1, pp2, pp3, t = deterministic_evolution(alpha0)
plt.plot(t,mm1,label='m1')
plt.plot(t,mm2,label='m2')
plt.plot(t,mm3,label='m3')
plt.legend()
plt.xlabel('t')
```
