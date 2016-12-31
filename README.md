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

## 
