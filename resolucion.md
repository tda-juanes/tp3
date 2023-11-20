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

El algoritmo es de tiempo polinomial ya que la maxima cantidad de subsets $B$ es $m \leq n$ y la máxima cantidad de elementos en $P$ es $k \leq n$, por lo tanto la complejidad es $O(n^2)$.