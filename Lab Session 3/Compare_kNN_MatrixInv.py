import numpy as np

x=np.c_[np.ones(len(x1)),x1]
w=np.linalg.pinv(x)@y1

xt=np.c_[np.ones(len(x2)),x2]
yp=(xt@w)>0.5

print(sum(yp==y2)/len(y2))
print(n.score(x2,y2))
