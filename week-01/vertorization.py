import numpy as np
import math

def sigmoid(x):
    res = 1/(1 + np.exp(-x))
    return res

def calcul(w,b,x):
    z = np.dot(w,x)+b
    return sigmoid(z)

def dense(A_in,W,B):
    Z = np.matmul(A_in,W) + B
    A_out = sigmoid(Z)
    return A_out

if __name__ == '__main__':
    X = np.array([[200,17]])
    W = np.array([[1,-3,5],
                  [-2,4,-6]])
    B = np.array([[-1,1,2]])
    res = dense(X,W,B)
    print(res)
    