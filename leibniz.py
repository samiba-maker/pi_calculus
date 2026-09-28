import math

NMAX = 1000

def leibniz(NMAX):
    n = 0
    r = 0

    while n < NMAX:
        r = r + ((-1)**n / (2*n + 1)) 
        n = n + 1

    return r

pisur4 = leibniz(NMAX)
environpi = 4 * pisur4 

print(environpi) 


