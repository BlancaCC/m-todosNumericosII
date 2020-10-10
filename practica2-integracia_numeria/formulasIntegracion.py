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


### FÓRMULA ADAPTATIVA

def adaptativa(formula,f, a,b,error=10**(-4)):
    m = (a+b)/2
    s = formula(f,a,b)
    sa = formula(f,a,m)
    sb = formula(f,m,b)

    if abs(s - sa-sb) < 10*error:
        return sa + sb
    else:
        return adaptativa(formula,f, a,m,error/2) + adaptativa(formula,f, m,b,error/2)
