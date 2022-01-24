#sqrt(sin(x))
import numpy as np
a,b,N=0,1,1000
n=np.random.normal(0,1/np.sqrt(2),N)
##2*g(x)*f(x)....mean=0,1/sqrt(2)
new_n=[];
for i in n:
    if(i<0):
        new_n.append(-i);
    else:
        new_n.append(i);
n=np.array(new_n);
n=np.sqrt(np.pi)*np.sqrt(np.sin(n))/2;
new_n=[];
for i in n:
    if(i>=0 and i<=np.pi):
        new_n.append(i);
g=np.array(new_n);
print(np.mean(g));
