import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
def calc(y, p):
    mse = mean_squared_error(y, p)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y - p) / y)) * 100
    r2 = r2_score(y, p)
    return mse, rmse, mape, r2
if __name__ == "__main__":
    d = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")
    x = d[["Open"]]
    y = d["Price"]
    x1, x2, y1, y2 = train_test_split(x, y, test_size=0.3, random_state=1)
    p = x2.squeeze()
    r = calc(y2, p)
    for i in r:
        print(i)
