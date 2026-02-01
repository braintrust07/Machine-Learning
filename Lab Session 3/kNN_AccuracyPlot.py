import matplotlib.pyplot as p
a=[]
k=range(1,12)
for i in k:
    n=KNeighborsClassifier(n_neighbors=i)
    n.fit(x1,y1)
    a.append(n.score(x2,y2))
p.plot(k,a)
p.show()
