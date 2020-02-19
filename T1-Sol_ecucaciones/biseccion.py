#
#  Resolución de ecuaciones por el algoritmo de bisección 
#  Blanca Cano Camarero 
#  19/II/20 

from math import exp 


def Biseccion ( f, intervalo , precision = 10**(-5) , iteracionesMaximas = 10**(5) ):
    a = intervalo[0]
    b = intervalo[1]
    encontrado = False
    cnt = 0  # contador de iteraciones cnt < iteracionesMaximas
    
    if f(a)*f(b) > 0 :
        print ('Para el dominio dado no se asegura la existenca de solución')
        
    elif abs( f(a) )< precision:
        resultado = a
        encontrado = True

    elif abs(f(b)) < precision : 
        resultado = b
        encontrado = True


    else:
        while not encontrado and cnt < iteracionesMaximas :
            resultado = (b+a)/2
            #print ( f'punto medio= {resultado}, a={a} , b={b} ,  vueltas= {cnt}')
             
            if abs(f( resultado)) < precision :
                print (" se ha encontrado por precisión")
                encontrado = True
            elif f(resultado ) < 0 :
                a = resultado
                
            else :
                b = resultado
                
                
            cnt += 1
    print ( f'el número de vueltas es {cnt} el máximo  es {iteracionesMaximas}')
    return resultado 


if __name__ == '__main__' :

    print (' funcion x:x intervalo [-1,4] sol: 0')
    print (Biseccion (lambda x:x, [-1,4], iteracionesMaximas=1000))

    
    print ("El siguiente no sé lo que debería dar")
    # --- Parámetro ajustables -- 
    def f(x):
        return exp(x)*2*x-5   # función a la que calcular las raíces 
    intervalo = [-1,4]     # intervalo de definición 
    print ( Biseccion ( f, intervalo) )
   
