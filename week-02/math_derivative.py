import numpy as np
import matplotlib.pyplot as plt
def carre(w):
    res = w **2
    return res


def derivate(w,e):
    r1 = carre(w)
    r2 = carre(w + e)
    r3 = r2 - r1
    return abs(r3/e)

def draw(w,j,e):
    for i in np.arange(-w,w,j):
        r = derivate(i,e)
        plt.plot(i,r,'b+')
    plt.show()
    
    

if __name__ == '__main__':
    # print(derivate(3,0.0001))
    # print(derivate(2, 0.0001))
    # print(derivate(-3, 0.0001))
    # draw(3,0.001,0.001)
    a = 2.001
    j = a**2 /2
    print(j)