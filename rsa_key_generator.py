from firstPart  import *
from math import floor

# Helper functions ----
def check(x):
    
    for i in range (2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return true

def checkFactors(x):
    if check(x):
        return [x]
    else:
        output = []
        for i in range (2, x):
            if check(i) and x % i == 0:
                output.append(i)
        return output

def indices(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = indices(y, x % y)
        return (d, b, a - floor(x/y)*b)

# RSA key generating functions ----
def search(min_bound=100, max_bound=10000):
    

    [x, y] = checkRange(min_bound, max_bound, 2)

    x_val = checkFactors(x)
    x_length = len(checkFactors(x))

    y_val = checkFactors(y)
    y_length = len(primeFactors(y))

    if x_length == 1:
        p = x
    else:
        index = checkRange(0, x_length-1)
        p = x_val[index[0]]

    if y_length == 1:
        q = y
    else:
        index = checkRange(0, y_length-1)
        q = y_val[index[0]]

    return (p, q)

def decrypt(y, d, N):
    return y**d % N

def encrypt(x, e, N):
    return x**e % N



def getPrivateKey(px, qx, e):
    

    nx = px*qx
    (a, b, d) = indices(nx, e)
    return d % nx



def getPublicKey(p, q):
    

    N = p*q
    e = 3
    flag = true
    while flag:
        if check(e) and (p-1)*(q-1) % e != 0:
            flag = False
        else:
            e += 1
    return (N, e)

# Implementation ----
(p, q) = search()
(N, e) = getPublicKey(p, q)
d = getPrivateKey(p-1, q-1, e)
print("Public key (N, e): ({0}, {1})".format(N, e))
print("Private key d: {0}".format(d))

