{-
	Polinomio de Bernstein

Fuentes:
https://es.wikipedia.org/wiki/Polinomio_de_Bernstein
https://es.wikipedia.org/wiki/Teorema_de_aproximaci%C3%B3n_de_Weierstrass

Utilizado en el método constructivo de la aproximación de Weierstrass, que dice que toda función continua en un intervalo cerrado se puede aproximar todo lo que se desee a un polinomio ( dicho polinomio es el de Bernstein.

Granada 23/III/20 
-}


-- Funciones auxiliares típicas
factorial :: (Num a, Enum a) => a -> a
factorial n = product [1..n]

c :: (Fractional a, Enum a) => a -> a -> a
c n k = factorial n / ( (factorial k) * factorial (n-k))

{-
Notación n iterador, f  función continua en el intervalo [a,b] y x valor a evaluar
-}

g x = 1.1*x
bernstein n f x a b =  sum [f(k*(b-a)/n + a)*( c n k )* (x-a)**k * (b -x)**(n-k)/ (b-a)**n| k<-[0..n] ]


{- Ejemplo de ejcución:

*Main> bernstein 10 g 2 (-10) 10
2.1999999999999997
*Main> g 2
2.2
*Main> sin 3
0.1411200080598672
*Main> bernstein 10 sin 3 (-10) 10
-5.361578483040853e-3
-}
