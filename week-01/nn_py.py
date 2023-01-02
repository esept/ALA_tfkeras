import numpy as np
import math


def sigmoid(x):
    res = 1/(1 + math.exp(-1* x))
    return res

def calcul(w,b,x):
    z = np.dot(w,x)+b
    return sigmoid(z)

if __name__ == '__main__':
    x = np.array([200, 17])  # 1D array
    w1_1 = np.array([1,2])
    b1_1 = np.array([-1])
    a1_1 = calcul(w1_1,b1_1,x)
    a1_2 = calcul(np.array([-3,4]),np.array(1),x)
    a1_3 = calcul(np.array([5, 6]), np.array(2),x)
    a1 = np.array([a1_1,a1_2,a1_3])
    w2_1 = np.array([-7,8,9])
    b2_1 = np.array([3])
    a2_1 = calcul(w2_1,b2_1,a1)
    print(a2_1)