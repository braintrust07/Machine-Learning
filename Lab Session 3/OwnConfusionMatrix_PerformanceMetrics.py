def cm(y,t):
    tp=sum((y==1)&(t==1))
    tn=sum((y==0)&(t==0))
    fp=sum((y==0)&(t==1))
    fn=sum((y==1)&(t==0))
    return tp,tn,fp,fn
def acc(tp,tn,fp,fn):
    return (tp+tn)/(tp+tn+fp+fn)
def pre(tp,fp):
    return tp/(tp+fp)
def rec(tp,fn):
    return tp/(tp+fn)
def f1(p,r):
    return 2*p*r/(p+r)
tp,tn,fp,fn=cm(y2,yp)
print(acc(tp,tn,fp,fn))
print(pre(tp,fp))
print(rec(tp,fn))
print(f1(pre(tp,fp),rec(tp,fn)))
