import numpy as np
import matplotlib.pyplot as plt
def gen():
    x = np.random.randint(1, 11, 20)
    y = np.random.randint(1, 11, 20)
    c = (x + y > 10).astype(int)
    return x, y, c
if __name__ == "__main__":
    x, y, c = gen()
    plt.scatter(x[c==0], y[c==0], color="blue")
    plt.scatter(x[c==1], y[c==1], color="red")
    plt.show()
