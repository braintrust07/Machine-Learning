import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
def run(d):
    x = d[["Open", "Volume"]]
    y = (d["Price"] > d["Open"]).astype(int)
    m = KNeighborsClassifier(n_neighbors=3)
    m.fit(x, y)
    p = m.predict(x)
    return x, p
if __name__ == "__main__":
    d = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")
    x, p = run(d)
    plt.scatter(x[p==0]["Open"], x[p==0]["Volume"])
    plt.scatter(x[p==1]["Open"], x[p==1]["Volume"])
    plt.show()
