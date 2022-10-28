from instancias import generar_instancias
import time

def DFS(grafo: dict, inicio: int, meta: int, visitados = []):
    visitados.append(inicio)
    if inicio == meta: 
        return visitados
    for adyacente in grafo[inicio]: 
        if adyacente not in visitados: 
            DFS(grafo, adyacente, meta, visitados)
            if meta in visitados: 
                break
    return visitados

def BFS(grafo: dict, inicio: int, meta: int): 
    visitados = []
    por_visitar = [inicio]
    while len(por_visitar) > 0: 
        nodo = por_visitar.pop(0)
        visitados.append(nodo)
        #print(nodo)
        if nodo == meta: 
            return visitados
        #else: 
        #    print("->")
        for n in grafo[nodo]: 
            if n not in visitados and n not in por_visitar: 
                por_visitar.append(n)
    return visitados

if __name__=="__main__": 
    grafo = generar_instancias()
    meta = int(input("Nodo que desea buscar? "))
    print("-"*10)
    print("Breadth First Search")
    tiempo_inicial = time.time()
    print("Recorrido: "+str(BFS(grafo, 1, meta)))
    print("Tiempo de búsqueda: "+str(time.time()-tiempo_inicial)+"s")
    print("-"*10)
    print("Depth First Search")
    tiempo_inicial = time.time()
    print("Recorrido: "+str(DFS(grafo, 1, meta)))
    print("Tiempo de búsqueda: "+str(time.time()-tiempo_inicial)+"s")