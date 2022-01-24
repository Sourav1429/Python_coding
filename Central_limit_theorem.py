import numpy as np
import matplotlib.pyplot as plt

gauss_samples=1000
n_points=1000
a,b=0,1

uniform_matrix=np.random.uniform(a,b,(gauss_samples,n_points));
gaussians=np.mean(uniform_matrix,axis=0)
plt.hist(gaussians)
plt.show()
