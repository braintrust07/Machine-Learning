import pandas as pd
import numpy as np
df = pd.read_excel("Lab Session Data",sheet_name="IRCTC Stock Price")
price = df.iloc[:, 3:4].to_numpy()
mean1 = np.mean(price)
var1 = np.var(price)
print("Mean(Caluclated using numpy): ", mean1)
print("Variance(Caluclated using numpy): ", var1)
def mean(x):
    sum = 0
    n = len(x)
    for i in x:
        sum += i
return sum/n
def var(x):
    total = 0
    n = len(x)
    mu = mean(x)
    for i in x:
        total += (i-mu)**2
return total/n
print("Mean(Caluclated using func): ", mean(price))
print("Variance(Caluclated using func): ", var(price))
wednesday_price = df[df["Day"] == "Wed"]["Price"]
mean_wed = np.mean(wednesday_price)
print("Mean of Prices on Wednesday: ", mean_wed)
print("Mean of Prices: ", mean1)
apr_price = df[df["Month"] == "Apr"]["Price"]
mean_apr = np.mean(apr_price)
print("Mean of Prices in April: ", mean_apr)
print("Mean of Prices: ", mean1)


