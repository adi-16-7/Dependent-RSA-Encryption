# Aditya Gupta
# 2017325
# Q2(a)

import sympy # pip install sympy
import gmpy2
from gmpy2 import mpz
import random

def Greatest_Common_Divisor(A, B):
    gvd = gmpy2.gcd(A, B)
    return gvd

def Multi_Inverse(e, Fi):
    return sympy.mod_inverse(e, Fi)

def Check_If_Prime(N):
    a = gmpy2.is_prime(N)
    return a

def Generate_Pair(P, Q):
    if P == Q:
        raise ValueError("P and Q cant be equal.")
    elif (Check_If_Prime(P) == False and Check_If_Prime(Q) == False):
        raise ValueError("Error: p and q, both must be prime.")

    N = gmpy2.mul(P,Q)
    Fi = gmpy2.mul((P-1),(Q-1))
    e = gmpy2.next_prime(q)
    d = Multi_Inverse(e, Fi)
    return ((e, N), (d, N))

def Encryption(publicKey, message):
    e, N = publicKey
    k = gmpy2.next_prime(N-e)
    C1 = gmpy2.powmod(k+1, e, N)
    C2 = gmpy2.mul(message,gmpy2.powmod(k, e, N))
    return (C1, C2, k, e)

if __name__ == "__main__":
    p = int(input("p : "))
    q = int(input("q : "))
    m = int(input("m : "))

    A, B = Generate_Pair(p, q)
    public_key = A
    private_key = B    

    C1, C2, k, e = Encryption(public_key, m)
    d, N = private_key
                                        
    print(C1)
    print(C2)
    print(k)
    print(e)
    print(d)
    print(N)



