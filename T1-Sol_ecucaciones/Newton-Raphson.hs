
{- Algoritmo Newton Raphson

Hipótesis que debe cumplir
i) si el intervalo de definición es [a,b] => f(a).f(b) <0 Para que exista solución
ii) La derivada primera no se puede anular nunca
iii) La derivada segunda no puede cambiar de signo

iv) (omitible si se utiliza semilla) max{ |f(a)/f'(a)|, |f(b)/f'(b)|} <= b-a
Esta condición es para que no se salga del intervalo

Bajo estas condiciones converge de forma única y el orden de convergencia es al menos lineal 

Granada 20/II/20
-}

type Intervalo = (Double,Double)
data Salida = Exacto  Double | Tolerancia Double | FinIteraciones   deriving Show

-- newtonPaphson  f f' x_n toleranca iteraciones_máximas
newtonRaphson :: (Eq t, Num t) =>  (Double -> Double)-> (Double -> Double) -> Double -> Double -> t -> Salida
newtonRaphson _ _ _ _ 0 = FinIteraciones 
newtonRaphson f f' x tol n 
  | fx == 0 = Exacto x
  | abs fx < tol = Tolerancia x
  | otherwise = newtonRaphson f f' xs tol (n-1)
  where
    fx = f x 
    xs = x - fx / (f' x)


semilla :: (Ord a, Num a) => (b -> a) -> (b -> a) -> (b, b) -> b
semilla f f'' intervalo
  | f a * f'' a > 0 = a
  | otherwise = b
  where
    a = fst intervalo
    b = snd intervalo 




{-  Ejemplo ejecución:

sean
mif = \ x -> x** 3 - 3
mif' = \ x -> 3 * x**2
mif'' = \ x -> 6.0 * x

*Main> semilla mif mif'' (0.1,3)
3.0
*Main> newtonRaphson mif mif' (semilla mif mif'' (0.1,3)) 0.000001 10
Tolerancia 1.4422496346010911
*Main> (3)**(1/3)
1.4422495703074083

-}
