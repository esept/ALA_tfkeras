def relu(a):
    return max(0,a)

def calZ(t,b):
    return t + b

def calT(w,x):
    return w * x

def calA(a):
    return relu(a)

def calJ(a,y):
    return (a - y)**2 / 2

def layer1(w1,x,b1):
    t1 = calT(w1, x)
    print(t1)
    z1 = calZ(t1, b1)
    print(z1)
    a1 = calA(z1)
    print(a1)
    return a1

if __name__ == '__main__':
    x = 1
    y = 5
    w1 = 2
    b1 = 0
    w2 = 3
    b2 = 1
    a1 = layer1(w1,x,b1)
    a2 = layer1(w2,a1,b2)
    J1 = calJ(a2,y)
    print(J1)
    sigma = 0.001
    a1 = layer1(w1, x, b1)
    a2 = layer1(w2 + sigma, a1, b2)
    J = calJ(a2, y)
    print(J)
    print("derivate = ",int((J-J1)/sigma))
    
    
    
    