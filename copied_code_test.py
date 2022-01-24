import numpy as np
import matplotlib.pyplot as plt

##ladders = [(2,4)]
##snakes = [(4,2)]
##trans = ladders + snakes

# Set up the transition matrix
T=[[2/3.,1/6.,1/6.,0,0,0,0,0,0],
   [0,2/3.,1/6.,1/6.,0,0,0,0,0],
   [0,0,0,0,1,0,0,0,0],
   [0,0,0,2/3.,1/6.,1/6.,0,0,0],
   [0,0,1,0,0,0,0,0,0],
   [0,0,0,0,0,2/3.,1/6.,1/6.,0],
   [0,0,0,0,0,0,2/3.,1/6.,1/6.],
   [0,0,0,0,0,0,0,5/6.,1/6.],
   [0,0,0,0,0,0,0,0,0]]
T=np.array(T);

# The player starts at position 0.
v = np.zeros(9)
v[0] = 1

n, P = 0, []
cumulative_prob = 0
# Update the state vector v until the cumulative probability of winning
# is "effectively" 1
while True:
    n += 1
    a = v.dot(T)
    flag=0;
    for i in range(9):
        if(a[i]!=v[i]):
            flag=1;
            break;
    if(flag==0):
        break;
    v=a;
    P.append(v[8])
    cumulative_prob += P[-1]
mode = np.argmax(P)+1
print('modal number of moves:', mode)

# Plot the probability of winning as a function of the number of moves
fig, ax = plt.subplots()
ax.plot(np.linspace(1,n,n), P, 'g-', lw=2, alpha=0.6, label='Markov')
ax.set_xlabel('Number of moves')
ax.set_ylabel('Probability of winning')

plt.show()
