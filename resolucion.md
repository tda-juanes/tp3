## 	Demostrar que el Hitting-Set Problem se encuentra en NP.

Todo problema perteneciente a $NP$ puede ser validado como tal si existe una prueba $P$ que pueda ser verificada en tiempo polinomial, en nuestro caso dada una prueba $P \subseteq A$, $|P| \leq k$, puede verificarse en tiempo polinomial si para todo subconjunto $B_i$ existe un elemento $p \in P$ tal que $p \in B_i$.

```python
def is_hitting_set(A, B, P):
    for b in B:
        for p in P:
            if p in b:
                break
        else:
            return False
    return True
```

El algoritmo es de tiempo polinomial ya que la maxima cantidad de subsets $B$ es $m$ y la máxima cantidad de elementos en $P$ es $k \leq n$, por lo tanto la complejidad es $O(n^2)$.

## Demostrar que el Hitting-Set Problem es NP-Completo.

Demostrar que el problema es NP-completo, ya habiendo demostrado que pertenece a NP, nos queda por demostrar que es NP-hard. Para esto reduciremos un problema NP-completo a nuestro problema, [Vertex Cover](https://en.wikipedia.org/wiki/Vertex_cover).

Vertex cover nos dice que dado un grafo $G = (V, E)$, existe un vertex cover $V' \subseteq V$ tal que para todo $(u, v) \in E$, $u \in V'$ o $v \in V'$.
El input de un problema de vertex cover es un grafo $G = (V, E)$ y un número $k$, para transformarlo a un problema de hitting set, por cada arista $(u, v) \in E$ creamos un subset $B_i = \lbrace u, v \rbrace$. Esto lo realizamos en tiempo polinomial $O(|E|)$.

```python
def vertex_cover_to_hitting_set(G, k):
    A = G.V
    B = [{u, v} for (u, v) in G.E]
    return A, B, k
```

Una vez que obtenemos la solución al Hitting-set $H$, esta estara compuesta por un subconjunto de vertices de $G$, los cuales forman un vertex cover. Esta transformación es en tiempo constante $O(1)$.

```python
def vertex_cover(G, k):
    A, B, k = vertex_cover_to_hitting_set(G, k)
    H = hitting_set(A, B, k)
    V = H
    return V
```


