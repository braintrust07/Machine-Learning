import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
def run(x, y):
    x1, x2, y1, y2 = train_test_split(x, y, test_size=0.3, random_state=1)
    m = KNeighborsClassifier(n_neighbors=3)
    m.fit(x1, y1)
    p1 = m.predict(x1)
    p2 = m.predict(x2)
    return (
        confusion_matrix(y1, p1),
        confusion_matrix(y2, p2),
        precision_score(y1, p1),
        precision_score(y2, p2),
        recall_score(y1, p1),
        recall_score(y2, p2),
        f1_score(y1, p1),
        f1_score(y2, p2)
    )
if __name__ == "__main__":
    d = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")
    x = d[["Open", "High"]]
    y = (d["Price"] > d["Open"]).astype(int)
    r = run(x, y)
    for i in r:
        print(i)
