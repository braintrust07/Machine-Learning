import numpy as np
def d(a,b):
    return sum(a[i]*b[i] for i in range(len(a)))
def l(a):
    return (sum(i*i for i in a))**0.5
a=np.array([1,2,3])
b=np.array([4,5,6])
print(d(a,b))
print(np.dot(a,b))
print(l(a))
print(np.linalg.norm(a))
