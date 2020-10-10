{-

MÉTODO DE LA DELTA CUADRADO DE AITKEN


Aceleración de la covergencia, incluso aunque diverja
Granada 27/II/20
--------------------------
Ejemplos de ejecución:
g = \x -> 5.0*x +4
[1.0,9.0,49.0,249.0,1249.0,6249.0,31249.0,156249.0,781249.0,3906249.0,1.9531249e7,9.7656249e7,4.88281249e8,2.441406249e9,1.2207031249e10]
-- como vemos diverge
*Main> sucesionAitken iterantesDeg 
[-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0]
ya ha convergido en la primera iteración
--------------------------

Idea matemática:

en = xn - s ; donde xn es el valor n-ésimo de la suceción y s la solución  deseada

Cuando se tiene que

en/e_(n+1) aprox e_(n+1)/e_(n+2) podemos despejar s
--------------------------
-}

fAitken :: Double -> Double -> Double -> Double  
fAitken xa x xs = xs - ( (xs-x)**2 / (xs - 2*x + xa) )

sucesionAitken :: [Double] -> [Double]
sucesionAitken l = sucesionAitken' l []

sucesionAitken' :: [Double] -> [Double] -> [Double]
sucesionAitken' l lsalida
  | length l >= 3 && not (isNaN x') =  sucesionAitken' (drop 1 l) (lsalida <> [x'])
  | otherwise = lsalida
    where
      xa = l!!0
      x = l!!1
      xs = l!!2
      x' = (fAitken xa x xs)  -- Si es nan es porque (xs - 2*x + xa) = 0 es decir ya tenemos una buena aproximación en xn 




-- aproximación a raíz de 2 
mif :: Double -> Double
mif  = \x -> (x+2/x)/2

raizDe2 = take 20 $ iterate mif 100

-- ecuación divergente
-- queremos ver dónde g x = 0
-- g x = xs
g :: Double -> Double
g = \x -> 5.0*x +4
-- como vemos diverge
iterantesDeg = take 15 $ iterate g 1

{-
*Main> sucesionAitken iterantesDeg 
[-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0]
*Main>  iterantesDeg 
[1.0,9.0,49.0,249.0,1249.0,6249.0,31249.0,156249.0,781249.0,3906249.0,1.9531249e7,9.7656249e7,4.88281249e8,2.441406249e9,1.2207031249e10]
Como  vemos en la primera ya ha convergido 
-}
