{-
MÉTODO DE LA SECANTE
características:
conocemos valores de la función pero no su derivada => aproximamos derivada
Granada 22/II/20
-}


{-
Significado valores que devuelve la función:
  Exacto x => f x = 0
  Tolerancia x_n => |x_n - x_{n-1}| < tolerancia ( Resultado próximo a la solución )
  FinInteraciones => Se ha alcanzado el número de iteraciones máximo indicado en n
  DivisionEntreCero => En la fórmul aque calcula el siguiente iterante (xs) se ha dividido entre 0
-}

data Salida = Exacto Double | Tolerancia Double | FinIteraciones  | DivisionEntreCero   deriving Show

secante ::  (Double -> Double) -> Double -> Double -> Double -> Int -> Salida
secante f x xa tol n
  | n == 0 = FinIteraciones 
  | diff == 0 = DivisionEntreCero
  | (f x) == 0 = Exacto x
  | abs(x - xa) < tol = Tolerancia x
  | otherwise = secante f xs x tol (n-1)
  where
    diff = (f x) - (f xa)
    xs = x - ( (f x) * ( x - xa) / diff)


{-- Ejemplo de ejecución 
f = \x -> x**3 - 1

*Main> secante (\x->x) 10.1 (-10.9) 0.0001 10
Exacto 0.0
*Main> secante f 10.1 (-10.9) 0.0001 10
Tolerancia 0.9999999972158184
*Main> secante f (-10.9) 2 0.0001 10
Tolerancia 1.0000000004887155
*Main> secante f (-10.9) 1 0.0001 10
Exacto 1.0

--}
