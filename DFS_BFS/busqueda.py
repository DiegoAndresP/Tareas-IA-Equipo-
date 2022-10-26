from instancias import generar_instancias
def DFS(grafo: dict, inicio: int, meta: int, visitados = []):
    print(inicio)
    if inicio == meta: 
        return
    print("->")
    visitados.append(inicio)
    for n in grafo[inicio]: 
        if n not in visitados: 
            DFS(grafo, n, meta, visitados)

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