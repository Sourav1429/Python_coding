import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return np.sqrt(np.sin(x));
a,b,N,l=0,np.pi,1000,20
area=0;
u=np.random.uniform(a,b,N)
integral=0;
for j in range(l):
    integral=0;
    for i in u:
        h=f1(i);
        integral+=h;
    answer=(b-a)/float(N)*integral
    print(answer);
    area+=answer
print(area/l);
