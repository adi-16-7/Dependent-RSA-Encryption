# Aditya Gupta
# 2017325
# Q2(b)

import sympy # pip install sympy
import gmpy2
from gmpy2 import mpz
import random

def Decryption(C1, C2, e, d, N):
    k = gmpy2.powmod(C1, d, N)-1
    m = gmpy2.div(C2, gmpy2.powmod(k, e, N))
    return (m, k)

if __name__ == "__main__":
    C1 = int(input("C1 : "))
    C2 = int(input("C2 : "))
    e = int(input("e : "))
    d = int(input("d : "))
    N = int(input("N : "))

    m, k = Decryption(C1, C2, e, d, N)

    print(int(m))
    print(k)

# 4198320198763482653315
# 13712284708959731896779049649798125073212693417
# 28567093412058936249583
# 182302015927
# 4252488962800942372855
# 28567093412241238265507
# 1237849889230930954275