# Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema. 
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.

# Los archivos tienen 1 conjunto (pedido de la prensa) por línea, separdos por ", ".
# 
# Colidio,Barcon't,Palermo,Pity Martinez
# Soule,Dibu,Chiquito Romero
# Beltran,Buonanotte,Mauro Zarate
# Armani,Pity Martinez,Beltran,Luka Romero
# Pezzella,Dibu,Buendia,Tucu Pereyra
# Riquelme,Langoni,Wachoffisde Abila
# Casco,Cuti Romero,Dybala
# Pezzella,Palermo,Colo Barco,El fantasma de la B
# Barcon't,Luka Romero,Colo Barco,Dybala
# Di Maria,Burrito Ortega,Changuito Zeballos
# 
# Cantidad mínima: 6 (Riquelme, Dibu, Beltran, Dybala, Di Maria, Palermo)

def intersects(subset, sol):
    for elem in subset:
        if elem in sol:
            return True
    return False

def backtracking_aux(subsets, s_i, sol, k):
    # print(sol, k)
    if intersects(subsets[s_i], sol): 
        if s_i == len(subsets) - 1:
            # print("solucion encontrada")
            return (True, sol, k)
        else:
            # print("Ya hay interseccion, sigo al siguiente subset")
            return backtracking_aux(subsets, s_i + 1, sol, k)
    
    if len(sol) >= k or s_i == len(subsets) - 1:
        # print("No hay solucion posible, marcha atras")
        return (False, sol, k)
    
    # Pruebo con todos los elementos del set actual
    for elem in subsets[s_i]:
        if elem in sol:
            continue
        # print("pruebo agregando elemento")
        n_sol = sol.copy()
        n_sol.append(elem)
        (valid, n_sol, k) = backtracking_aux(subsets, s_i + 1, n_sol, k)
        if valid:
            return (True, n_sol, k)
        
    return (False, sol, k)

def backtracking(subsets):
    initial_set = subsets[0]
    print(initial_set)
    for i in range(1, 10):
        for j in initial_set:
            sol = [j]
            (valid, sol, k) = backtracking_aux(subsets, 1, sol, i)
            if valid:
                return (sol, k)
    
    return None
    
def main():
    file = open("./test/200.txt", "r")
    
    subsets = []    
    for line in file.readlines():
        subsets.append(line.strip().split(","))
    subsets = sorted(subsets, key=lambda x: len(x)) # no es necesario, 
                                                    # pero ayuda a encontrar 
                                                    # la solucion mas rapido

    sol = backtracking(subsets)
    print(sol)
        
main()