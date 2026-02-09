import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
def run():
    x = np.random.randint(1, 11, (20, 2))
    y = (x[:,0] + x[:,1] > 10).astype(int)
    t = np.array([[i, j] for i in np.arange(0,10,0.1) for j in np.arange(0,10,0.1)])
    m = KNeighborsClassifier(n_neighbors=3)
    m.fit(x, y)
    p = m.predict(t)
    return t, p
if __name__ == "__main__":
    t, p = run()
    plt.scatter(t[p==0][:,0], t[p==0][:,1], s=1)
    plt.scatter(t[p==1][:,0], t[p==1][:,1], s=1)
    plt.show()
