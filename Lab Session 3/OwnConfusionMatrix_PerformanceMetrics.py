import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="IRCTC_Stock_Price")
X=df[["Open","High","Low","Volume"]].to_numpy()
y=(df["Close"].shift(-1)>df["Close"]).astype(int).to_numpy()
X=X[:-1]
y=y[:-1]
x1,x2,y1,y2=train_test_split(X,y,test_size=0.3)
n=KNeighborsClassifier(n_neighbors=3)
n.fit(x1,y1)
yp=n.predict(x2)
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
