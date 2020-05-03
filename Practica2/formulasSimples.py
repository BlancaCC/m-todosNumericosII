"""
FORMULAS INTEGRACIÓN 
Granada 30/IV/20


"""

### ___ FÓRMULA SIMPLES ____
def rectangulo_izquierdo(f,a,b):
    return f(a)*(b-a)

def simpson(f, a, b):
    return 1/6*(f(a)+4*f((a+b)/2)+f(b))*(b-a)

def trapecio(f,a,b):
    return (f(a)+f(b))/2*(b-a)

##___ FÓRMULA COMPUESTA GENÉRICA ____

def formula_compuesta (f,formula,a,b,n):
    h = (b-a)/n
    return sum([formula(f,a+i*h,a+(i+1)*h) for i in range(n)])
