import numpy as np
def m(x):
    return sum(x)/len(x)
def v(x):
    u=m(x)
    return sum((i-u)**2 for i in x)/len(x)
def s(x):
    return v(x)**0.5
def ms(x):
    return np.mean(x,axis=0),np.std(x,axis=0)
c1=X[y==0]
c2=X[y==1]
m1,s1=ms(c1)
m2,s2=ms(c2)
print(m1)
print(s1)
print(m2)
print(s2)
print(np.linalg.norm(m1-m2))
