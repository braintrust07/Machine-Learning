import pandas as pd
import numpy as np

df = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
types = df.dtypes
miss = df.isnull().sum()
num = df.select_dtypes(include=np.number)
m = num.mean()
v = num.var()


b = df.select_dtypes(include=[np.number]).iloc[:2]
b = b.loc[:, (b == 0).all() | (b == 1).all()]
x = b.iloc[0]
y = b.iloc[1]
f11 = ((x == 1) & (y == 1)).sum()
f00 = ((x == 0) & (y == 0)).sum()
f10 = ((x == 1) & (y == 0)).sum()
f01 = ((x == 0) & (y == 1)).sum()
jc = f11 / (f01 + f10 + f11)
smc = (f11 + f00) / (f00 + f01 + f10 + f11)


a1 = df.select_dtypes(include=np.number).iloc[0].to_numpy()
a2 = df.select_dtypes(include=np.number).iloc[1].to_numpy()
cos = np.dot(a1, a2) / (np.linalg.norm(a1) * np.linalg.norm(a2))


d = df.select_dtypes(include=np.number).iloc[:20].to_numpy()
n1 = len(d)
m1 = np.zeros((n1, n1))
for i in range(n1):
    for j in range(n1):
        m1[i][j] = np.dot(d[i], d[j]) / (np.linalg.norm(d[i]) * np.linalg.norm(d[j]))
sns.heatmap(m1, annot=True)

for c in df.columns:
    if df[c].dtype == "object":
        df[c].fillna(df[c].mode()[0], inplace=True)
    else:
        df[c].fillna(df[c].median(), inplace=True)

numbers = df.select_dtypes(include=np.number)
df[numbers.columns] = (numbers - numbers.min()) / (numbers.max() - numbers.min())