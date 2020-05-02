"""
NEWTON-PAPHSON 
Blanca Cano Camarero 

"""


import numpy as np
import sympy as sp

x = sp.symbols('x')


def newtonRaphson(f, inicio, tolerancia =10*(-5), precision=10*(-5), max_iter=20, df=None):

    if df == None:
        df = sp.lambdify(x, sp.diff(f,x), "numpy")           
    f = sp.lambdify(x, f)
    c = inicio
    cnt = 1
    no_encontrado = True
    salida = "max_iter"
    while cnt < max_iter and no_encontrado : 
        
        cs = c - f(c)/df(c)
        #cs = f(c)
        
        if abs(f(cs)) < precision: 
            salida = "precision"
            no_encontrado = False
        if abs(cs-c) < tolerancia:
            salida = "tolerancia"
            no_encontrado = False
        else: 
            c = cs 
            cnt +=1
            
    return cs , salida, cnt


def newtonRaphsonSinInicio(f,a,b, tolerancia=10**(-5), precision=10**(-10), max_iter=100):
    # Calculamos derivadas
    
    ddf = sp.lambdify(x,sp.diff(f,x,2),"numpy")
    
    #calculamos punto inicial 
    if f.evalf(subs={x:a})*ddf(a) > 0 : 
        c = a
    else :
        c = b
    
   
    return newtonRaphson(f,inicio=c , tolerancia = tolerancia, precision = precision, max_iter = max_iter)



def newtonRaphsonAcelerado (f, inicio, tolerancia =10*(-5), precision=10*(-5), maxIter=30, df = None):

    if df == None:
        df = sp.simplify(sp.diff(f,x))

    return newtonRaphson((f/df), inicio, tolerancia,precision)

                            
                            

def horner(x,coef, d = 0):
    """Algoritmo de horner para evaluación rápida de polinomio
x es el punto en el que evaluar el polinomio 
coef es una lista con los coeficientes a evaluar de $p = \sum_{i=0}^n \alpha_i x^i$ 

d es la derivada del polinomio a calcular 
    """  
    
    n = len(coef)
    
    salida = 0
    for i in range(n,d,-1):
        salida = sp.factorial(i-1)/sp.factorial(i-d-1)*coef[i-1] + x*salida
      
    return salida



## Aprovechamos nuestras implementaciones ya hechas
def newtonRapshonHorner(coef,semilla, tolerancia =10*(-5), precision=10*(-5), max_iter=20):
    """ Algoritmo de newtonRapshon para evaluar polinomio sde manera rápida"""
    f = horner(x,coef,0)
    midf = sp.lambdify(x, horner(x,coef,1))
    return newtonRaphson(f, 10, tolerancia =10*(-5), precision=10*(-5), max_iter=20,df=midf)
