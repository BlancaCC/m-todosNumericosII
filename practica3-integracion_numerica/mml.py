'''
MML BASADOS EN CUADRATURA

Aunque las abreviaturas las carga el diablo, 
las utilizadas aquí son: 

AM

Nota: En algunos casos la variabel k es superflua, se ha añadido para que la cabecera 
tenga el mismo formato y sea totalmente versatil :)
'''
import numpy as np
from eulerexplrapido import integrate as euler 

def succ_AB (F, B,t, X,h,k=None):
    '''ADAMS-BASHFORTH
    F derivada
    B vectori coeficientes del métdodo (de aquí se obtiene la k)
    h diferencia
    matriz de X anteriores
    ojo se está usando notación (t,x)
    ''' 
    return X[-1] + h* sum([B[i]*F(t+h*i, X[i]) for i in range(len(B))])

def complete_AB(F,x0,y0,xfinal,N, beta, m_inicial=euler):
    '''
    ojo se está usando notación (x,y)
    '''
    k = len(beta)
    X = np.linspace(x0,xfinal,N+1)
    h = (xfinal-x0)/N
    Y = [y0]
    
    #calculamos primeras aprox con m_inicial 
    for i in range(k-1):
        Y.append(m_inicial(F,X0[i],Y[-1], h))

    for n in range(N-1):
        Y.append(succ_AB(F,B,X[n],Y[-k:], h,k))
                                
    return np.array(X),np.array(Y)


def succ_AM (F, B,t, X,h,k=None):
    '''
    F derivada
    B vectori coeficientes del métdodo (de aquí se obtiene la k)
    h diferencia
    matriz de X anteriores
    ojo se está usando notación (t,x)
    ''' 
    return X[-2] + h* sum([B[i]*F(t+h*i, X[i]) for i in range(len(B))])

def complete_AM(F,x0,y0,xfinal,N, beta, m_inicial, k=None):
    '''
    ojo se está usando notación (x,y)
    '''
    if(k==None):
        k = len(beta)
    X = np.linspace(x0,xfinal,N+1)
    h = (xfinal-x0)/N
    Y = [y0]
    
    #calculamos primeras aprox con m_inicial 
    for i in range(k-1):
        Y.append(m_inicial(F,X0[i],Y[-1], h))

    for n in range(N-1):
        Y.append(succ_AM(F,B,X[n],Y[n],X[-k:], h,k))
                                
    return np.array(X),np.array(Y)

def succ_MS (F, B,t, X,h,k=None):
    '''
    Milne-simpson
    F derivada
    B vectori coeficientes del métdodo (de aquí se obtiene la k)
    h diferencia
    matriz de X anteriores
    ''' 
    return X[-3] + h* sum([B[i]*F(t+h*i, X[i]) for i in range(len(B))])

def complete_MS(F,x0,y0,xfinal,N, beta, m_inicial):
    k = len(beta)
    X = np.linspace(x0,xfinal,N+1)
    h = (xfinal-x0)/N
    Y = [y0]
    
    #calculamos primeras aprox con m_inicial 
    for i in range(k-1):
        Y.append(m_inicial(F,X0[i],Y[-1], h))

    for n in range(N-1):
        Y.append(succ_MS(F,B,X[n],Y[n],X[n:], h))
                                
    return np.array(X),np.array(Y)

def succ_Nystrom (F, B,t, X, h, k):
    '''
    METODO NYSTROM
    F derivada
    B vectori coeficientes del métdodo va hasta la k-r
    h diferencia
    matriz de X anteriores
    ''' 
    return X[k-3] + h* sum([B[i]*F(t+h*i, X[i]) for i in range(len(B))])

def complete_Nystrom(F,k,x0,y0,xfinal,N, beta, m_inicial):
    k = len(beta)
    X = np.linspace(x0,xfinal,N+1)
    h = (xfinal-x0)/N
    Y = [y0]
    
    #calculamos primeras aprox con m_inicial 
    for i in range(k-1):
        Y.append(m_inicial(F,X0[i],Y[-1], h))

    for n in range(N-1):
        Y.append(succ_Nystrom(F,B,X[n],Y[n],X[n:], h,k))
                                
    return np.array(X),np.array(Y)

## Metodos para calcular alphas y betas con el mayor orden posible 
## Basado en la teoría de que tendrá orden p si pata todo i \in {0..p} Ci = 0 y C_{p+1} \neq 0
def fact(n):
    if n == 0:
        return 1
    else:
        return n* fact(n-1)
    
def C(i, A, B, k):
    '''
    X_{n+k} = \sum a_i x_{n+i} + h\sum b_i f_i 
    A = [a_0, ...a_{k-1}]
    B = [b_0,... b_{k}]
    '''
    if (i==0):
        return 1 - sum(A)
    else:
        f = fact(i-1)
        return k**i/(f*i) - sum( [ j**k/(f*i)*A[j] for j in range(1,len(A))]) - sum( [ j**(k-1)/f *B[j] for j in range(1,len(B))])
