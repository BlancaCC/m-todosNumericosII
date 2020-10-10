
from eulerexplrapido import integrate as euler 
import numpy as np

def pc(metodo_predictor,F, Bp,x0, y0,xfinal, metodo_corrector,Bc,N,metodo_inicial=euler, num_correciones =1):

    
    k = len(Bp)
    X = np.linspace(x0,xfinal,N+1)
    h = (xfinal-x0)/N
    Y = [y0]
    
    #calculamos primeras aprox con m_inicial 
    for i in range(k-1):
        Y.append(metodo_inicial(F,X[i],Y[-1], h))

    for n in range(N-1):
        ys = metodo_predictor(F,Bp,X[n],Y[-k:], h,k)
        
        for i in range(1,num_correcciones):
            ys = metodo_corrector(F,Bc,X[n],X[-k:]+[ys], h,(k+1))
        
        Y.append(metodo_corrector(F,Bc,X[n],X[-k:]+[ys], h,(k+1)))
                    
    
    return np.array(X),np.array(Y)

    
    
    
    
