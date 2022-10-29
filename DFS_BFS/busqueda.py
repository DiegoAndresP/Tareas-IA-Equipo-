from instancias import generar_instancias
import time

def DFS(grafo: dict, meta: int, inicio = 1, visitados = []):
    visitados.append(inicio)
    if inicio == meta: 
        return visitados
    for adyacente in grafo[inicio]: 
        if adyacente not in visitados: 
            DFS(grafo, adyacente, meta, visitados)
            if meta in visitados: 
                break
    return visitados

def DFS_con_peso(grafo: dict, meta: int, inicio = 1, peso = 0, visitados = [], ruta = []): 
    visitados.append(inicio)
    ruta.append((inicio, peso))
    if inicio == meta: 
        return ruta
    for adyacente in grafo[inicio]: 
        if adyacente[0] not in visitados: 
            DFS_con_peso(grafo, meta, adyacente[0], adyacente[1], visitados, ruta)
            if meta in visitados: 
                break
    return ruta

def BFS(grafo: dict, meta: int, inicio = 1): 
    visitados = []
    por_visitar = [inicio]
    while len(por_visitar) > 0: 
        nodo = por_visitar.pop(0)
        visitados.append(nodo)

        if nodo == meta: 
            return visitados

        for n in grafo[nodo]: 
            if n not in visitados and n not in por_visitar:  
                    por_visitar.append(n)
    return visitados

def BFS_con_peso(grafo: dict, meta: int, inicio = 1): 
    visitados = []
    ruta = []
    nodos_por_visitar = [(inicio, 0)]
    por_visitar = [inicio]
    while len(nodos_por_visitar) > 0: 
        nodo = nodos_por_visitar.pop(0)
        por_visitar.pop(0)
        visitados.append(nodo[0])
        ruta.append(nodo)

        if nodo[0] == meta: 
            return ruta
        
        for n in grafo[nodo[0]]:
            if n[0] not in visitados and n[0] not in por_visitar: 
                nodos_por_visitar.append(n)
                por_visitar.append(n[0])
    return ruta

if __name__=="__main__": 
    grafo = generar_instancias()

    meta = int(input("Nodo que desea buscar? "))


    print("-"*10)
    print("Breadth First Search")
    tiempo_inicial = time.time()
    recorrido = BFS(grafo, meta) if type(grafo[1][0]) != tuple else BFS_con_peso(grafo, meta)
    print(recorrido)
    print("Tiempo de búsqueda: "+str(time.time()-tiempo_inicial)+"s")
    
    
    print("-"*10)
    print("Depth First Search")

    tiempo_inicial = time.time()
    recorrido = DFS(grafo, meta) if type(grafo[1][0]) != tuple else DFS_con_peso(grafo, meta)
    print(recorrido)
    print("Tiempo de búsqueda: "+str(time.time()-tiempo_inicial)+"s")
    