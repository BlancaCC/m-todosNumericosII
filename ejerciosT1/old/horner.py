"""
Algoritmo de Horner para evaluación rápida de polinomios. 

la idea intuitica es ir sacando factor común las x
Autor: Blanca Cano Camarero

Fecha 27/IV/20

"""


def horner (coef, x):

    ret = coef[-1]
    for i in coef[-2:0:-1]:
        ret = i + x*ret
        print(f'valor de i {i} valor de ret {ret}')

    return ret




def hornerRecursivo(coef, x):
    """([a_0..a_n], x)->number
Donde a_0 son los coeficientes de un polinomio: sum a_i x^i
"""

    ret = coef[0]
    if len(coef) >1:
      ret+= x * horner(coef[1:], x)

    return ret


    
