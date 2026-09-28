import math 

from leibniz import leibniz
from machin import machin 
from montecarlo import montecarlo 

NMAX = 100000 

pi1 = 4 * leibniz(NMAX)
pi2 = 4 * machin(NMAX)
pi3 = 4 * montecarlo(NMAX) 

print(abs(pi1 - math.pi))
print(abs(pi2 - math.pi))
print(abs(pi3 - math.pi))



