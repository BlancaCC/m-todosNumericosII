"""
POLINOMIO DE INTERPOLACIÓN DE NEWTON 

Dada una lista de nodos, devuelve su polinomio de 
interpolación de newton 

Ejemplo de uso abajo del fichero

Blanca Cano Camarero 
Granada 3/v/20

"""

import numpy as np
import sympy as sp

def polinomioNewton (x,y=[]):
    """
    Devuelve el polinomio de interpolación de newton.
    Argumentos: 
        x: lista de nodos simbólicos, ejmplo [a-h,a,a+h] donde  a,h = sp.symbols('a,h').
        y: valores interpolatorios, se pasa para ahorrar cálculos, DEJAR VACÍO.
    """
    f = sp.Function('f')
    n = len(x)-1
    z = sp.Symbol('z')

    if n == 0: 
        return f(x[0])
    else: 
        # valores interpolatorios 

        if(y == []):
            y = [ f(i) for i in x]  

        #polinomio anterior
        p = polinomioNewton(x[0:-1],y)
        
        #D = f[x0,x1..x_{n}]
        D = sp.Symbol('D')

        #polinomio sucesor (el que vamos a devolver)
        ps = p + np.prod([z - x[i] for i in range(n)])*D

        ## Despejamos D para que garantice que p(xn) = yn
        D = (sp.solve(ps.subs({z:x[n]})-y[n],D))[0]
        ps = p +  np.prod([z - x[i] for i in range(n)])*D

        return ps

## ejemplo de ejecución 

if __name__ == '__main__':
    f = sp.Function('f')
    a,h,z = sp.symbols('a,h,z')
    x = [a-h, a, a+h]

    print(polinomioNewton(x))
## esto imprime en pantalla
## f(a - h) + (f(a) - f(a - h))*(-a + h + z)/h + (-a + z)*(-a + h + z)*(-2*f(a) + f(a - h) + f(a + h))/(2*h**2)
