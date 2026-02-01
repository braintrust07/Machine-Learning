import pandas as pd
import numpy as np
import matplotlib.pyplot as p
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="IRCTC_Stock_Price")
x=df["Open"].to_numpy()
print(np.mean(x))
print(np.var(x))
p.hist(x,bins=10)
p.show()
