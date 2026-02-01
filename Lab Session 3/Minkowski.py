import numpy as np
import matplotlib.pyplot as p
def md(a,b,pv):
    return sum(abs(a[i]-b[i])**pv for i in range(len(a)))**(1/pv)
a=X[0]
b=X[1]
d=[]
k=range(1,11)
for i in k:
    d.append(md(a,b,i))
p.plot(k,d)
p.show()
