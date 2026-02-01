import numpy as np
import matplotlib.pyplot as p
x=X[:,0]
h,b=np.histogram(x,bins=10)
print(np.mean(x))
print(np.var(x))
p.hist(x,bins=10)
p.show()
