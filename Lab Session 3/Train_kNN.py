from sklearn.neighbors import KNeighborsClassifier
n=KNeighborsClassifier(n_neighbors=3)
n.fit(x1,y1)
print(n.score(x2,y2))
