'''
FÓRMULA DE HEUN O EULER MEJORADO 
(Idea utilizar integración del trapecio)
'''

import numpy as np

def succ_integrate(F,x,y,h):
    '''método de de euler mejorado 
    F (x,y) función derivada
    x, y valores de los que se parte
    h:incremento
    Salida : y_{n+1}
    '''
    return y + h/2*(F(x,y) + F(x+h, y + h*F(x,y) ) )


def complete_integrate(F,x0, y0,xfinal, N ):
    '''método de de euler mejorado 
    F (x,y) función derivada
    x, y valores de los que se parte
    N: número de intervalos 
    Salida : vector de nodos, vector de soluciones apriximadas a esos nodos
    '''
    X = np.linspace(x0,xfinal,N+1)
    Y = [y0]
    h = (xfinal - x0)/N
    
    for n in range(N):
        Y.append(succ_integrate(F,X[n],Y[n],h))
    return X,Y


