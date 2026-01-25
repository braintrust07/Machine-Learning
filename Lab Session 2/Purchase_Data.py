import pandas as pd
import numpy as np
import time

df = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")
p = df.iloc[:, 3].to_numpy()
m1 = np.mean(p)
v1 = np.var(p)
def mean(a):
    s = 0
    for i in a:
        s += i
    return s / len(a)
def var(a):
    m = mean(a)
    s = 0
    for i in a:
        s += (i - m) ** 2
    return s / len(a)
t1 = []
t2 = []
for _ in range(10):
    st = time.time()
    mean(p); var(p)
    t1.append(time.time() - st)
for _ in range(10):
    st = time.time()
    np.mean(p); np.var(p)
    t2.append(time.time() - st)
w = df[df["Day"] == "Wed"].iloc[:, 3].to_numpy()
apr = df[df["Month"] == "Apr"].iloc[:, 3].to_numpy()
chg = df.iloc[:, 8]
loss_p = len(chg[chg < 0]) / len(chg)
wed = df[df["Day"] == "Wed"]
profit_w = len(wed[wed.iloc[:, 8] > 0]) / len(df)
cond_p = len(wed[wed.iloc[:, 8] > 0]) / len(wed)
