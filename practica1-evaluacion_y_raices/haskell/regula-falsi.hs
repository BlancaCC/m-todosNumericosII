
{- Regula - falsi

Granada 19 /II/20-}


type Intervalo = (Double, Double)
data Salida = Exacto Double | Tolerancia Double | FinIteraciones Intervalo | DivisionEntreCero  Intervalo deriving Show

regulaFalsi :: (Eq a, Num a) =>(Double -> Double) -> Intervalo -> Double -> a -> Salida

regulaFalsi _ intervalo _ 0 = FinIteraciones intervalo
regulaFalsi f intervalo tolerancia iteraciones
  | diff == 0 = DivisionEntreCero intervalo
  | eva == 0 = Exacto x
  | abs eva < tolerancia = Tolerancia x
  | eva*f(b) < 0 = regulaFalsi f (x,b) tolerancia (iteraciones - 1)
  | otherwise = regulaFalsi f (a, x) tolerancia (iteraciones - 1)
  where
    a = fst intervalo 
    b = snd intervalo 
    diff = (f b) - (f a) 
    x = (a* (f b) - b * (f a)) / diff
    eva = f x


{- Ejemplo de ejcución

*Main> regulaFalsi  (\x -> x-5) (-1,106) 0.00001 1
Exacto 5.0
*Main> regulaFalsi  (\x -> 2 * x**3 - 4* x **2 + 3 * x) (-100,106) 0.00001 10
FinIteraciones (-3.906626219072675,106.0)
*Main> regulaFalsi  (\x -> 2 * x**3 - 4* x **2 + 3 * x) (-100,106) 0.00001 1000
xFinIteraciones (-1.411844217817583,106.0)
*Main> regulaFalsi  (\x -> 2 * x**3 - 4* x **2 + 3 * x) (-100,106) 0.00001 100000000000
Tolerancia (-3.33296567021431e-6)

-}
