import random

NMAX = 100000

def montecarlo(NMAX): 
    n = 0
    dans = 0

    while n < NMAX:
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        
        if x**2 + y**2 <= 1:
            dans = dans + 1

        n = n + 1

    pisur4 = dans / NMAX
    return pisur4 

pisur4 = montecarlo(NMAX)
environpi = 4 * pisur4

print(environpi)
        







        

    