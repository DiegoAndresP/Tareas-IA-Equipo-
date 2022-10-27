from instancias import generar_instancias

def DFS(grafo: dict, inicio: int, meta: int, visitados = []):
    print(inicio)
    if inicio == meta: 
        return inicio
    print("->")
    visitados.append(inicio)
    nodo = inicio
    for adyacente in grafo[inicio]: 
        if adyacente not in visitados: 
            nodo = DFS(grafo, adyacente, meta, visitados)
            if nodo == meta: 
                break
    return nodo

def BFS(grafo: dict, inicio: int, meta: int): 
    visitados = [inicio]
    por_visitar = [inicio]
    while len(por_visitar) > 0: 
        nodo = por_visitar.pop(0)
        print(nodo)
        if nodo == meta: 
            return
        else: 
            print("->")
        for n in grafo[nodo]: 
            if n not in visitados: 
                visitados.append(n)
                por_visitar.append(n)

if __name__=="__main__": 
    grafo = generar_instancias()
    #BFS(grafo, 1, 5)
    DFS(grafo, 1, 5)