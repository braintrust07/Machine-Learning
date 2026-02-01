from scipy.spatial.distance import minkowski
a=X[0]
b=X[1]
print(md(a,b,3))
print(minkowski(a,b,3))
