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

