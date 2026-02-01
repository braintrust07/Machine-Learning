import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
df=pd.read_excel("Lab Session Data.xlsx",sheet_name="IRCTC_Stock_Price")
X=df[["Open","High","Low","Volume"]].to_numpy()
y=(df["Close"].shift(-1)>df["Close"]).astype(int).to_numpy()
X=X[:-1]
y=y[:-1]
x1,x2,y1,y2=train_test_split(X,y,test_size=0.3)
n=KNeighborsClassifier(n_neighbors=3)
n.fit(x1,y1)
yp=n.predict(x2)
print(confusion_matrix(y2,yp))
print(precision_score(y2,yp))
print(recall_score(y2,yp))
print(f1_score(y2,yp))
