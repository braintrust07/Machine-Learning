import pandas as pd
from scipy.spatial.distance import minkowski
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="IRCTC_Stock_Price")
X=df[["Open","High","Low","Volume"]].to_numpy()
a=X[0]
b=X[1]
def md(a,b,pv):
    return sum(abs(a[i]-b[i])**pv for i in range(len(a)))**(1/pv)
print(md(a,b,3))
print(minkowski(a,b,3))
