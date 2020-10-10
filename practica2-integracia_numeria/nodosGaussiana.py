"""
Cálculo de los nodos de de la CUADRATURA gaussiana
Blanca Cano Camarero 
Granada 4/V/20
"""
import sympy as sp

def nodos_gaussiana (a, b, n,w):
    """ Devuelve los nodos de la fórmula de la gaussiana
    a,b: intervalo [a,b] de definición
    n: número de nodos 
    w: función peso
    """
    x = sp.Symbol("x")
    c = list(sp.symbols('c0:'+ str(n)))
    pi = np.prod([ (x - c[i]) for i in range(n)])
    #print('Voy a computar la integral (esto puede tardar)...')
    I = [sp.integrate(pi*w(x)*x**i,(x, a, b)) for i in range(n)]
    #print(f'El valor de la integrales es {I}')
    #print('la solución buscada es: ')
    s = sp.solve(I,c)
    return list(s[0])