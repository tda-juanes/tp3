# Trabajo Práctico 3: Problemas NP-Completos
El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo de Backtracking para resolver un Problema NP-Completo, así como el análisis de posibles aproximaciones. La fecha de entrega del mismo es el 24/11.

## Introducción
Scaloni ya está armando la lista de 43 jugadores que van a ir al mundial 2026. Hay mucha presión por parte de la prensa para bajar línea de cuál debería ser el 11 inicial. Lo de siempre. Algunos medios quieren que juegue Roncaglia, otros quieren que juegue Mateo Messi, y así. Cada medio tiene un subconjunto de jugadores que quiere que jueguen. A Scaloni esto no le importa, no va a dejar que la prensa lo condicione, pero tiene jugadores jóvenes a los que esto puede afectarles.

Justo hay un partido amistoso contra Burkina Faso la semana que viene. Oportunidad ideal para poner un equipo que contente a todos, baje la presión y poder aislar al equipo.

El problema es, ¿cómo elegir el conjunto de jugadores que jueguen ese partido (entre titulares y suplentes que vayan a entrar)? Además, Scaloni quiere poder usar ese partido para probar cosas aparte. No puede gastar el amistoso para contentar a un periodista mufa que habla mal de Messi, por ejemplo. Quiere definir el conjunto más pequeño de jugadores necesarios para contentarlos y poder seguir con la suya. Con elegir un jugador que contente a cada periodista/medio, le es suficiente.

Ante este problema, Bilardo se sentó con Scaloni para explicarle que en realidad este es un problema conocido (viejo zorro como es, ya se comió todas las operetas de prensa así que se conoce este problema de memoria). Se sirvió una copa de Gatorei y le comentó:

"Esto no es más que un caso particular del Hitting-Set Problem. El cual es: Dado un conjunto 
$A$ de $n$ elementos y $m$ subconjuntos $B_1, B_2, ..., B_m$ de $A$
($B_i \subseteq A \forall i$) , queremos el subconjunto $C \subseteq A$ de menor tamaño tal 
que $C$ tenga al menos un elemento de cada
$B_i$ (es decir, $C \cap B_i \neq \emptyset$). En nuestro caso, $A$ son los jugadores 
convocados, los $B_i$ son los deseos de la
prensa, y $C$ es el conjunto de jugadores que deberían jugar contra Burkina Faso 
si o si". 

Bueno, ahora con un poco más claridad en el tema, Scaloni necesita de nuestra 
ayuda para ver si obtener este subconjunto se puede hacer de forma eficiente 
(polinomial) o, si no queda otra, con qué alternativas contamos.

## Consigna

Para los primeros dos puntos, considerar la versión de decisión del Hitting-Set Problem:

Dado un conjunto de elemento $A$ de $n$ elementos, $m$ subconjuntos $B_1, B_2, ..., B_m$ de $A$
($B_i \subseteq A \forall i$), y un número $k$, ¿existe un subconjunto $C \subseteq A$ con $|C| \leq k$ tal que $C$ tenga al menos un elemento de cada $B_i$ (es decir, 
$C \cap B_i \neq \emptyset$)?

1. 	Demostrar que el Hitting-Set Problem se encuentra en NP.

2. 	Demostrar que el Hitting-Set Problem es, en efecto, un problema NP-Completo. 

3. 	Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema. 
	Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos. 

4. 	Escribir un modelo de programación lineal que resuelva el problema de forma óptima. Ejecutarlo
	para los mismos sets de datos para corroborar su correctitud (o al menos hasta la mayor cantidad
	de volumen posible). Tomar mediciones de tiempos
	y compararlas con las del algoritmo que implementa Backtracking. 

6. 	El doctor Bilardo, como buen resultadista que es, le propone a Scaloni el siguiente algoritmo:
 	usar el mismo algoritmo planteado en el punto 4, pero permitiendo que las variables de decisión
	sean valores reales, y luego redondear el resultado final del modelo. Para redondear, obtenemos el
	valor $$b$$ como la cantidad de aquel conjunto entre los diferentes conjuntos (pedidos de la prensa)
	que tenga la mayor cantidad de jugadores, y  definimos que la variables de decisión de cada jugador
	serán 1 si su valor en el modelo relajado es mayor o igual a $$1/b$$.
   
	Este algoritmo sirve como una aproximación para resolver el hitting-set problem. 
	Implementar dicho algoritmo, analizar su complejidad
	y analizar cuán buena aproximación es. Para esto, considerar lo siguiente: 
	Sea $$I$$ una instancia cualquiera del Hitting-Set Problem, y $$z(I)$$ una
	solución óptima para dicha instancia, y sea $$A(I)$$ la solución aproximada, 
	se define $$\frac{A(I)}{z(I)} \leq r(A)$$ para todas las instancias posibles. 
	Calcular $$r(A)$$ para el algoritmo dado, demostrando que la cota está bien
	calculada. Realizar mediciones utilizando el algoritmo exacto y la aproximación,
	con el objetivo de verificar dicha relación. Realizar también mediciones
	que contemplen volúmenes de datos ya inmanejables para el algoritmo exacto,
	a fin de corroborar empíricamente la cota calculada anteriormente. 

8.	**Opcional**: Implementar alguna otra aproximación (u algoritmo greedy) que 
	les parezca de interés. Comparar sus resultados con los dados por la aproximación 
	del punto 5. Indicar y justificar su complejidad. No es obligatorio
	hacer este punto para aprobar el trabajo práctico (pero si resta puntos no hacerlo).

9. 	Agregar cualquier conclusión que parezca relevante.

## Entrega

Debe enviarse al corrector asignado, por mail o slack, el link
al repositorio donde se encuentre el código fuente, y donde debe encontrarse
el informe en formato PDF, que debe seguir los lineamientos establecidos en el TP1 y TP2.
Debe ser claro cómo ejecutar el programa pasando por parámetro un set de datos como
los que se dan de ejemplo. Esto puede ser dentro del `README.md` del repositorio,
u otra forma que les parezca clara. 

La nota del trabajo práctico tendrá en cuenta tanto la presentación y calidad de lo presentado, 
como también el desarrollo del trabajo. No será lo mismo un trabajo realizado con lo mínimo
indispensable, que uno bien presentado, analizado, y probado con diferentes volúmenes, set de 
datos, o estrategias de generación de sets, en el caso que corresponda.