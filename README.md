# Cell Project
Projecte Biologia Computacional

## Guillespie module
This is the first module that must be imported and used. Using a self-created random number generator, it computes the Guillespie evolution of the next sys$$X_1 + X2 → 2X2$$
$$X_2 → 0$$

The results are saved in vectors that, after its proper import, can be plotted using instructions such as:
```python
import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(0)
plt.plot(t_v,x1_v) #To find the x1 evolution
plt.plot(t_v,x2_v) #To find the x2 evolution
plt.plot(x1_v,x2_v)
```


## Amplitude module
In order to work with the 'Amplitude' module, the vectors must have been first created and imported using the first module.
Finally, to show the results something such as:
```python
import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(A)
```

or 

```python
import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(f)
```

is recommended to plot the amplitudes (for the first case) and the frequencies (for the second).
