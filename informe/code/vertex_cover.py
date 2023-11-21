def vertex_cover(G, k):
    A = G.V
    B = [{u, v} for (u, v) in G.E]
    V = hitting_set(A, B, k)
    return V
