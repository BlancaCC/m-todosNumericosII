"""
ACELERACIÓN CONVERGENCIA  
Método delta cuadrado de Aithe
Blanca Cano Camarero
Granada 2/V/20
"""


def xs(x0, x1, x2):
    return x2-((x2 - x1)**2/(x2-2*x1+x0))

def tablasAceleracion(g, semilla):
    s = [list(),list(),list()]
    s[0].append(semilla)  
    print(f'Xn\t | Aitken \t |Stepheson '.expandtabs(25))
    print(f'{s[0][0]}\t | \t | '.expandtabs(25))
    for i in range(1,13):
        s[0].append(g(s[0][-1]))
        a = s[0][-1]
        b=c=''
        if i>=2:
            s[1].append(xs(s[0][-3],s[0][-2],s[0][-1]))
            b = s[1][-1]
        if i >=4: 
            s[2].append(xs(s[1][-3],s[1][-2],s[1][-1]))
            c = b = s[2][-1]
        print(f'{a}\t | {b}\t | {c}'.expandtabs(25))
        
    return s
