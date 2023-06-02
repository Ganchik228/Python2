from math import *
import numpy as np
n = 10 

def f(i):
    return sqrt(i+2) - sqrt(i) - 3/11

def g(j):
    return ((3*(j**2) - 11) / ((-j**3) - 2))

def matrix(n):
    a = np.empty((n, n))

    for i in range(n):
        for j in range(n):
            a[i, j] = f(i+1) + g(j+1)  


    sum = np.sum(a)
    itog = 1/100*sum
    print(round(itog, 6))

matrix(n)


