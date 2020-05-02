"""
MÉTODO DE BISECCIÓN 
Blanca Cano Camarero
Granada 10/IV/20
"""

import numpy as np

def calcIterations (a:float, b:float, error:float, maxIter:int = 10000 ) -> int:
    """Devuele el mínimo entre el número de iteraciones necesarias para alcanzar como máximo un error  en bisección
    y un máximo intruducido (que por defecto es 10000
    """
    return min(maxIter,np.ceil(np.log((b-a)/error)/np.log(2)))


## bisection method



def bisection(f,a:float,b:float,error = 10**(-5), tolerance=10**(-13)) -> tuple:
    n = int(calcIterations(a,b,error)  ) 
    for i in range (n):
        xs = (b+a)/2
        evaluation = f(xs)
        if abs(evaluation) < tolerance:
            return xs, 'tolerance'
        elif evaluation * f(a) > 0:
            a = xs
        else:
            b = xs
    return xs,'iteration'
