import pandas as pd
import numpy as np
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="IRCTC_Stock_Price")
X=df[["Open","High","Low","Volume"]].to_numpy()
y=(df["Close"].shift(-1)>df["Close"]).astype(int).to_numpy()
X=X[:-1]
y=y[:-1]
c1=X[y==0]
c2=X[y==1]
m1=np.mean(c1,axis=0)
s1=np.std(c1,axis=0)
m2=np.mean(c2,axis=0)
s2=np.std(c2,axis=0)
print(m1)
print(s1)
print(m2)
print(s2)
print(np.linalg.norm(m1-m2))
