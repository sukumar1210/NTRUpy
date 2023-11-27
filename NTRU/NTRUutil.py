from sympy import symbols, invert, poly, GF
from Crypto.Random.random import randint
import numpy as np
import math

# generate random numbers
# generate bits from a string

def isPrime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num))):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False    

def randPoly(N, df):
    if 2*df>=N:
        raise ValueError("df is too large")
    else:
        f = np.zeros((N,), dtype = int)
        for i in range((2*df)-1):
            if(i<df):
                f[i] = 1
            else:
                f[i] = -1
        # np.random.shuffle.seed(randint(N))
        np.random.shuffle(f)
        return f

    