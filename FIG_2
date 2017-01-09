#GILLESPIE ALGORITHM
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
    
    p = rand_uni() #canviar
    
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


plt.figure(0)
plt.plot(t_v,x1_v)
