'''
Método de Butcher 
y algunos implemetados a partir de él: 
RK4: runge-kuta clásico 
RK2, con alfa beta parámetros
'''

import sympy as sp
import numpy as np

def succ_butcher(F,x,y,a,b,h):
    '''
    f derivada
    y(x) = y que es el valor inicial 
    h = variación
    a,b son coeficiente del arreglo de butcher
    | c_1 | a11 a12 ...a1n
    | c_2 | a21 a22 ...a2n
             ...
    | c_n | an1 an2 ...ann
    ------------------------
          | b1   b2 ... bn
          
    y representa 
    
    x_{n+1} = x_n + h \sum_{j=1}^n b_j K_j(t_n, x_n)
    k_i(t,x) = f(t+c_i h, x+ h \sum_{j=1}^n a_{ij} k_j(t,x))
          
    '''
    n=len(b)
    c = [ sum(a[i]) for i in range(n)]
    K = sp.symbols('k0:'+str(n))
    
    def fk(f,i,t,x,h):
        '''Representa K_i(t,x) = f(t+c_ih, sum a K_j) )
        '''
        return f( t+c[i]*h, x+h*sum(
        [ a[i][j]*K[j] for j in range(n)]) )

    l=[ - K[i] + fk(F,i,x,y,h)    for i in range(n)]
    
    sk =sp.solve(l, K)

    
    def solk(K, sk):
        '''Solve puede que no nos devuelva todas las soluciones si son 0'''
        l = [j for j in range(n)]
        for i in range(n):
            if K[i] in sk:
                l[i] = sk[K[i]]
            else:
                l[i] =0
        return l

    sk =solk(K,sk)
    
    return y + h*sum([ b[i]*sk[i] for i in range(n)] ) 
    
  
def complete_butcher(F, x0, y0,xfinal, N, a, b):
    '''
    F función
    x,y condiciones iniciales y(x_0) = y_0
    xfinal = valor final hasta el que calcular
    N número de intervalos 
    '''
    t,z = sp.symbols('t z')
    X = np.linspace(x0,xfinal,N+1)
    Y = [y0]
    h = (xfinal - x0)/N
    
    # Calculamos la aproximación 
    rk= succ_butcher(F,t,z,a,b,h)

    for n in range(N):
        Y.append(rk.subs({t:X[n],z:Y[n]}) )
    return X,Y

def succ_RK4(f,x, y, h):
    n=4
    a = [[0,0,0,0],
         [1/2,0,0,0],
         [0,1/2,0,0],
         [0,0,1,0]
        ]
    
    b = [1/6,1/3,1/3,1/6]
    
    return succ_butcher(f,x,y,a,b,h)

def succ_RK2(f,x,y,h, alpha=1, beta=1/2):
    '''
    Recordemos que es óptimo en alpha*beta = 1/2
    - Si alpha = 1, beta = 1/2: método Punto medio
    - Si alpha 1/2, beta = 1: Heun (trapecio)
    '''
    n=2
    a = [
        [0,0],
        [beta, 0]
    ]
    b = [1-alpha, alpha]
    
    return succ_butcher(f,x,y,a,b,h)




def complete_RK2(F, x0, y0, xfinal, N, alpha=1, beta=1/2):
    n=2
    a = [
        [0,0],
        [beta, 0]
    ]
    b = [1-alpha, alpha]
    return complete_butcher(F, x0, y0, xfinal, N, a, b)
    
def complete_RK4(F, x0, y0, xfinal, N):
    '''
    F función
    x,y condiciones iniciales y(x_0) = y_0
    xfinal = valor final hasta el que calcular
    N número de intervalos 
    '''
    t,z = sp.symbols('t z')
    X = np.linspace(x0,xfinal,N+1)
    Y = [y0]
    h = (xfinal - x0)/N
    
    # Calculamos la aproximación 
    rk4= succ_RK4(F,t,z,h)

    for n in range(N):
        Y.append(rk4.subs({t:X[n],z:Y[n]}) )
    return X,Y
