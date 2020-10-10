'''
FORMULA DE INTEGRACIÓN Y DERIVACIÓN DE TAYLOR

Ejemplo de ejecución: 
def f3(x,y):
    return sp.exp(3*x)

succ_taylor(f3,0,1,1/10, 2) # devolverá el resultado de ejecutar el métood de Taylor
complete_taylor(f3,0,1,1,10)    # nodos y su valor en el los distintos nodos
'''

import numpy as np
import sympy as sp

t,z = sp.symbols('t,z')

def fact(x):
    ''' factorial
    '''
    r = 1
    for i in range(2,x):
        r = r*i
    return r


def _diff(F,orden=1):
    '''CALCULA DERIVADA
    F(x,y(x)) (en función de sympy)
    orden es el número de derivada 
    '''
    def F_aux(x,y):
            return sp.diff(F(t,z),t).subs({t:x,z:y})  + sp.diff(F(t,z),z).subs({t:x,z:y}) * F(t,z).subs({t:x,z:y}) 
        
    if orden>1: 
        F_aux= _diff(F_aux, orden-1)
        
    return F_aux

def serieTaylor(y0,F,h, orden = 1, ordenAcumulado=1, T = None,):
    '''Devuelve serie de teylor de centrada en y0
    y0: es el valor primero 
    F(x,y) es el valor de la derivada
    
    Los parámetro ordenAcumulado y T NO SE TOCAN (son auxiliares a la función)
    '''
    
    if ordenAcumulado == 1:
        df = F
        def ret(x,y):
            return y0 + h*F(x,y)
    else:
        df = _diff(T)
        
        def ret(x,y):
            return F(x,y) + df(x,y)*h**ordenAcumulado/fact(ordenAcumulado)
        
    if orden == ordenAcumulado:
        return ret
    else:
        return serieTaylor(y0, ret, h, orden, (ordenAcumulado+1), df)
        
    
def succ_taylor(F,x,y,h, p = 1):
    '''Método de taylor, devuelve 
    y_{n+1} 
    calculado por el método de taylor 
    y_{n+1} = y_n + \sum_{i = 1} ^p \frac{h^i}{i!} derivada_orden_i(y_n)
    ''' 
    taylorcillo = serieTaylor(y,F,h,p)
    return taylorcillo(x,y)

def complete_taylor(F, x0, y0, xfinal, N, p= 1):
    X = np.linspace(x0,xfinal,N+1)
    Y = [y0]
    h = (xfinal - x0)/N
    
    # Calculamos la aproximación 
    taylorcillo = succ_taylor(F,t,z,h, p)

    for n in range(N):
        Y.append(taylorcillo.subs({t:X[n],z:Y[n]}) )
    return X,Y
