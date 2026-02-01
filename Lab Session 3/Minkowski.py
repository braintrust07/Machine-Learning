import pandas as pd
import matplotlib.pyplot as p
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="IRCTC_Stock_Price")
X=df[["Open","High","Low","Volume"]].to_numpy()
a=X[0]
b=X[1]
def md(a,b,pv):
    return sum(abs(a[i]-b[i])**pv for i in range(len(a)))**(1/pv)
r=[]
k=range(1,11)
for i in k:
    r.append(md(a,b,i))
p.plot(k,r)
p.show()
