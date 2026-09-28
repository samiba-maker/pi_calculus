import math

NMAX = 1000

def arctan(x,NMAX):
    n = 0
    r = 0

    while n < NMAX:
        r = r + (((-1)**n * x**(2*n + 1)) / (2*n + 1))
        n = n + 1

    return r


def machin(NMAX):
    pisur4 = 4 * arctan(1/5, NMAX) - arctan(1/239, NMAX)

    return pisur4


pisur4 = machin(NMAX)
environpi = 4 * pisur4

print(environpi)