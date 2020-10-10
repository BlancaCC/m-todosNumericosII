"""
    MÉTODO PUNTO MEDIO O EULER MEJORADO 
    __ funciones__ 
    complete_integrate: devuelve soluciones de nodos y soluciones
    succ_integrate: dado un nodo devuelve la siguiente solución 
     
    __ significado variables __ 
    X,Y     = integrate(F,x0,y0,xfinal,N).
    {y}'    = {F(x,{y})}, donde
    {y}     = {y[0],y[1],...y[N-1]}.
    x0,y0   = condiciones iniciales 
    xfinal  = valor final de la variable x
    h       = incremento de x usado para la integración
    F       = función suplida por el usuario que devuelve 
            el array F(x,y) = {y'[0],y'[1],...,y'[N-1]}.
"""
import numpy as np
def succ_euler(F, x,y,h):
    '''método de euler explícito 
    F (x,y) función derivada
    x, y valores de los que se parte
    incremento
    Salida : y_{n+1}
    '''
    return y + h* F(x,y)

def succ_integrate(F,x,y,h):
    '''PUNTO MEDIO siguiente solución
    '''
    return y + h*F(x+h/2, succ_euler(F,x,y,h/2))

def complete_integrate(F,x0, y0,xfinal, N ):
    X = np.linspace(x0,xfinal,N+1)
    Y = [y0]
    h = (xfinal - x0)/N
    
    for n in range(N):
        Y.append(succ_integrate(F,X[n],Y[n],h))
    return X,Y

