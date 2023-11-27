from sympy import symbols, invert, poly, GF, Poly
from NTRUutil import *
import numpy as np


# generate keys
    # generate f, inverse of fmodp and fmodq, g, h
# inverse of fmodp and fmodq
# inverse of polynomial



class NTRUdecrypt:
    def __init__(self, N = 503, p = 3, q = 257, df = 61, dg = 20, dr = 18):
        self.N = N
        self.p = p
        self.q = q
        self.df = df
        self.dg = dg
        self.dr = dr
        
        self.f = np.zeros((self.N,), dtype = int)
        self.fp = np.zeros((self.N,), dtype = int)
        self.fq = np.zeros((self.N,), dtype = int)
        self.g = np.zeros((self.N,), dtype = int)
        self.h = np.zeros((self.N,), dtype = int)
        
        self.I = np.zeros((self.N+1,), dtype = int)
        self.I[self.N] = -1
        self.I[0] = 1

    # setting the values of f, p, q, df, dg, dr
    def setNpq(self, N = None, p = None, q = None, df = None, dg = None, dr = None):
        if N is not None:
            if (not isPrime(N)):
                raise ValueError("N must be a prime number")
            else:
                if df is None:
                    if self.df*2 >= N:
                        raise ValueError("Input df if too small than the default N")
                    else:
                        self.df = df
                if dg is None:
                    if self.dg*2 >= N:
                        raise ValueError("Input dg if too small than the default N")
                    else:
                        self.dg = dg
                if dr is None:
                    if self.dr*2 >= N:
                        raise ValueError("Input dr if too small than the default N")
                    else:
                        self.dr = dr
                self.N = N
                
                # setting the respective polynomial arrays
                self.f = np.zeros((self.N,), dtype = int)
                self.fp = np.zeros((self.N,), dtype = int)
                self.fq = np.zeros((self.N,), dtype = int)
                self.g = np.zeros((self.N,), dtype=int)
                self.h = np.zeros((self.N,), dtype=int)
                self.I = np.zeros((self.N+1,), dtype = int)
                self.I[self.N] = -1
                self.I[0] = 1
                
                
        if p is not None and q is not None:
            if (not isPrime(p) or not isPrime(q) or p*8>q or math.gcd(p, q) != 1):
                raise ValueError("Invalid values for p or q")
            else:
                self.p = p
                self.q = q
        if df is not None:
            if df*2 >= self.N:
                raise ValueError("Input df if too small than the N")
            else:
                self.df = df
        if dg is not None:
            if dg*2 >= self.N:
                raise ValueError("Input dg if too small than the N")
            else:
                self.dg = dg
        if dr is not None:
            if dr*2 >= self.N:
                raise ValueError("Input dr if too small than the N")
            else:
                self.dr = dr

    def invf(self, f, I, modulo):
        print("inside invf", modulo)
        print(len(I))
        x=symbols('x')
        ff=Poly(f, x)
        II=Poly(I, x)
        if(isPrime(modulo)):
            try:
                return poly(invert(ff.as_expr(), II.as_expr(), domain=GF(modulo,symmetric=False))).all_coeffs()
            except:
                # print("not isPrime(modulo)")
                return np.array([])
        else:
            return np.array([])


    # generate polynomials f, g, fp, fq
    def genfg(self):
        print("inside genfg")
        maxTries=100
        #  we don't care about invertability of g
        self.g = randPoly(self.N, self.dg)
        # we generate f until we find one that is invertible mod p and q
        
        temp_fq = np.zeros((self.N,), dtype = int)
        temp_fp = np.zeros((self.N,), dtype = int)
        for i in range(maxTries):
            temp_f = randPoly(self.N, self.df)
            temp_fp = self.invf(temp_f, self.I, self.p)
            temp_fq = self.invf(temp_f, self.I, self.q)
            print(f"temp_fp: {len(temp_fp)}\ttemp_fq: {len(temp_fq)}")
            if len(temp_fp) != 0 and len(temp_fq) != 0:
                self.f=temp_f
                self.fp=temp_fp
                self.fq=temp_fq
                if(len(self.fp) < self.N):
                    self.fp = np.concatenate((temp_fp, np.zeros((self.N-len(temp_fp),), dtype = int)))
                if (len(self.fq) < self.N):
                    self.fq = np.concatenate((temp_fq, np.zeros((self.N-len(temp_fq),), dtype = int)))
                break
            else:
                temp_f = randPoly(self.N, self.df)
    def genh(self):
        print("inside genh")
        x = symbols("x")
        self.h = Poly((Poly(self.p*self.fq,x).trunc(self.q)*Poly(self.g,x)).trunc(self.q)%Poly(self.I,x)).all_coeffs()

if __name__ == "__main__":
    dec=NTRUdecrypt()
    dec.genfg()
    dec.genh()
    # print("f", dec.f, len(dec.f))
    # print("fp", dec.fp, len(dec.fp))
    # print("fq", dec.fq, len(dec.fq))
    # print("g", dec.g, len(dec.g))
    # print("h", dec.h, len(dec.h))