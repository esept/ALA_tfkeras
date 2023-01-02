import numpy as np

if __name__ == '__main__':
    A = np.array([[200,17]])
    W = np.array([[1,-3,5],[-2,4,-6]])
    print(A)
    b = np.array([[-1,1,2]])
    z = np.matmul(A,W) + b
    print(z)
    