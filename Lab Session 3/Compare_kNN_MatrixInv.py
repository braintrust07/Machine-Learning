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
x=np.c_[np.ones(len(x1)),x1]
w=np.linalg.pinv(x)@y1
xt=np.c_[np.ones(len(x2)),x2]
yp=(xt@w)>0.5
print(sum(yp==y2)/len(y2))
print(n.score(x2,y2))
