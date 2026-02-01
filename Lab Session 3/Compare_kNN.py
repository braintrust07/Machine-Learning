import numpy as np
def kn(x,t,y,k):
    d=[(np.linalg.norm(x-i),c) for i,c in zip(t,y)]
    d.sort()
    r=[c for _,c in d[:k]]
    return max(set(r),key=r.count)
p=[kn(i,x1,y1,3) for i in x2]
print(p)
print(n.predict(x2))
