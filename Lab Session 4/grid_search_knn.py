import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
if __name__ == "__main__":
    d = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")
    x = d[["Open", "High"]]
    y = (d["Price"] > d["Open"]).astype(int)
    g = GridSearchCV(KNeighborsClassifier(), {"n_neighbors": range(1,21)})
    g.fit(x, y)
    print(g.best_params_)
