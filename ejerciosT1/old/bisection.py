# BISECTION METHOD

import numpy as np

def calcIterations (a,b, error, maxIter = 10000): 
    return min(maxIter,np.ceil(np.log((b-a)/error)/np.log(2)))


## bisection method



def bisection(f,a,b,error = 10**(-5), tolerance=10**(-13)):
    n = int(calcIterations(a,b,error)  ) 
    for i in range (n):
        xs = (b-a)/2
        evaluation = f(xs)
        if np.absolute(evaluation) < tolerance:
            return xs, 'tolerance'
        elif evaluation * f(a) > 0:
            a = xs
        else:
            b = xs
    return xs,'iteration'
