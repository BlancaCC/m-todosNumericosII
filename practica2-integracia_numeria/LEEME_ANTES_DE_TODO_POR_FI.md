# Práctica 2

Blanca Cano Camarero

## Cuestiones sobre fórmulas de interpolación

### Mejora considerable del algoritmo de Newton

Ante todo me gustaría hacerle hincapíe en que analizara el algoritmo de
que deduce la forma del polinomio de newton que he implementado en el fichero
`polinomioNewton` ya que a mi parecer supone una ventaja considerable en
los método que usted propuso, ya que tiene ciertas mejoras considerables:

- Abstrae al caso particular: no es necesario calcular manualmente las diferencias dividas (que es una tarea repetitiva, pesada y  propensa a equivocaciones y que por tanto urge a automatizar).
- Moduladidad: cuantos menos líneas de código sueltas, si estas se van a repetir mejor.

### Cuestiones generales

He optado, puesto que me parece la fórmula más cómo y sencilla de trabajar de implementar los algoritmos en fichero a parte y de importarlos al pirncipio en
el notebook, para que este solo contenga los ejercicios resueltos.

### Sobre el ejercicio 7
(Este comentario se entiende mejor con el notebook delante)
He desarrollado un método que ni en teoría ni en práctica hemos visto, (no tampoco por internet)
y el cual me resulta de lo más natural y simple que consiste en obtnener la fórmula con el polinomio de newton construido en los nodo obtenidos pro la
cuadratura gaussiana. 

## otras cosas
También le dejo una versión muy bonita del método adpatativo por haskell
