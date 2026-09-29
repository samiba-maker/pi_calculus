import math 

NMAX = 1000
eps = 1e-3
x = 3.14/4

def taylor(x, NMAX): 
    n = 0
    v = 0

    while n < NMAX:
        t = (-1)**n * x**(2*n) / math.factorial(2*n) 
        vold = v
        v = v + t

        if abs(vold - v) < eps:
            break
        n = n + 1 
    return v 

resultat = taylor(x, NMAX)
print(resultat)

    
