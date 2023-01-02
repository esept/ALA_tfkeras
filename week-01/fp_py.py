# forward propagation with python
import numpy as np
import math

def sigmoid(x):
    res = 1/(1 + np.exp(-x))
    return res

def calcul(w,b,x):
    z = np.dot(w,x)+b
    return sigmoid(z)

def dense(a_in,W,b):
    '''
    构建一个神经网络层
    :param a_in: 输入参数
    :param W: 参数矩阵
    :param b: 截距矩阵
    :return: 该层神经网络的输出值（units个数值的向量）
    '''
    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range(units):
        w = W[:,j] # 截取 W矩阵中j列向量
        print(w)
        r = calcul(w,b[j],a_in)
        if  r > 0.5:
            a_out[j] = 1
        else:
            a_out[j] = 0
    print(a_out)
    return a_out

def sequential(x):
    '''
    构建一个四层的神经网络，且进行正向传播
    :param x:
    :return:
    '''
    a1 = dense(x, W1, b1)
    a2 = dense(a1, W2, b2)
    a3 = dense(a2, W3, b3)
    a4 = dense(a3, W4, b4)
    return a4




if __name__ == '__main__':
    # 为了完成矩阵乘法，W矩阵应该按照竖向排列参数
    W = np.array([[1,-3,5],
                  [-2,4,-6]])
    b = np.array([-1,1,2])
    a_in = np.array([200,17])
    dense(a_in,W,b)