import math 

NMAX = 1000
eps = 1e-3

def arctan(x, NMAX):
	n = 0
	v = 0
	
	while n < NMAX:
		t = ((-1)**n) * (x**(2*n+1)) / (2*n+1)
		vold = v
		v = v + t 

		if abs(vold-v) < eps:
			break 

		n = n + 1

	return v

def machin(NMAX):
	pisur4 = 4 * arctan(1/5, NMAX) - arctan(1/239, NMAX) 
	return pisur4

pisur4 = machin(NMAX)
result = 4 * pisur4
print(result)

