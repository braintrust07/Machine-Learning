import numpy as np
def d(a,b):
    return sum(a[i]*b[i] for i in range(len(a)))
def l(a):
    return (sum(i*i for i in a))**0.5
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="IRCTC_Stock_Price")
X=df[["Open","High","Low","Volume"]].to_numpy()
a=X[0]
b=X[1]
print(d(a,b))
print(np.dot(a,b))
print(l(a))
print(np.linalg.norm(a))

