{-
 Algortimo de bisección para encontrar raíces
Granada 19 /II/20 
-}

data Salida = Cero  Double | Tolerancia Double | FinIteraciones (Double,Double)  deriving Show
biseccion :: (Num a, Num t, Ord t, Eq a) =>
     (Double -> t) -> (Double, Double) -> t -> a -> Salida

biseccion  _ intervalo _ 0 = FinIteraciones intervalo
biseccion f intervalo tolerancia iteraciones 
  | x == 0 = Cero m
  | abs x <= tolerancia = Tolerancia m
  | x * (f b)< 0 = biseccion f (m,b) tolerancia (iteraciones-1)
  | otherwise = biseccion f (a,m) tolerancia (iteraciones-1)
  where
    a = fst intervalo 
    b = snd intervalo 
    m = (a + b) / 2
    x = f m


{-
Ejemplo de ejecución   
*Main> biseccion (\x -> x) (-1,3) 0.00001 30
Cero 0.0
*Main> biseccion (\x -> x) (-1,100) 0.00001 30
Tolerancia 5.7220458984375e-6
*Main> biseccion (\x -> x) (-1,100) 0.00001 2
FinIteraciones (-1.0,24.25)

-}
