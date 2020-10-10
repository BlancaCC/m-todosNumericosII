{-- MÉTODO DE INTEGRACIÓN ADAPTATIVA
Blanca Cano
Granada 28-IV-20

Ejemplo de ejecución
*Main> f x = 1/(x**2 + 1)
*Main> iterAdaptativa f (-5) 5 0.00001
2.7468037248859707

--}


{- Aproximación de Simpson-}

simpson :: Fractional a => (a -> a) -> a -> a -> a
simpson  f a b = h/3*(f a + 4* (f m) + f b)
  where
    h = (b-a)/2
    m = (b+a)/2


{- Método de iteración adaptativa Simpson -}
*Main> :t iterAdaptativa 
iterAdaptativa :: (Ord a, Fractional a) => (a -> a) -> a -> a -> a -> a
iterAdaptativa f a b e
  | error < 10*e = sa + sb
  | otherwise = iterAdaptativa f a m (e/2) + iterAdaptativa f m b (e/2)
    where
      m = (b+a)/2
      sa = simpson f a m
      sb = simpson f m b
      s = simpson f a b
      error = abs(s - sa - sb)


