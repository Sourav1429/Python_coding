#Finding_area
import numpy as np
x=np.linspace(0,np.pi,100000);
f=np.sqrt(np.sin(x))*np.exp(-1*np.power(x,2));
#f=np.sin(x);
l=len(f);
a=x[0];
h,integral=0,0
for i in range(1,l):
    b=x[i];
    h=min(h,f[i]);
    integral+=h*(b-a);
    a=b
    h=f[i];
print(integral);
    
