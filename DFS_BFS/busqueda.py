from instancias import generar_instancias
from time import time
from math import inf

def validar_sn(sn)->bool: 
    return sn == "s" or sn == "n"

def validar_dirigido()->bool: 
    dirigido = input("El grafo será dirigido? S/n: ").strip().lower()
    while not validar_sn(dirigido): 
        dirigido = input("Ingrese únicamente \"S\" o \"N\": ").lower()
    return dirigido == "s"

def validar_peso()->bool: 
    peso = input("Desea que el grafo tenga peso? S/n: ").strip().lower()
    while not validar_sn(peso): 
        peso = input("Ingrese únicamente \"S\" o \"N\": ").lower().strip()
    return peso == "s"

def validar_int(frase: str)->int: 
    num = 0
    while num <= 0: 
        try: 
            num = int(input(frase))
        except ValueError: 
            print("Entrada inválida, ingrese un valor entero mayor a cero")
            num = 0
    return num

def distancia_BFS(grafo: dict, ruta: list): 
    distancia = 0
    cola = [ruta[0]]
    usados = []
    while len(cola) > 0:
        for v in grafo[cola[0]]:
            if v[0] not in cola and v[0] not in usados and v[0] in ruta:
                distancia += v[1]
                cola.append(v[0])
        usados.append(cola.pop(0))
    return distancia

def distancia_DFS(grafo: dict, ruta: list): 
    distancia = 0
    pila = [ruta[0]]
    usados = []
    while len(pila) > 0: 
        terminal = True
        for v in grafo[pila[len(pila)-1]]: 
            if v[0] not in pila and v[0] not in usados and v[0] in ruta: 
                distancia += v[1]
                pila.append(v[0])
                terminal = False
                break
        if terminal: 
            usados.append(pila.pop())
    return distancia

def BFS(grafo: dict, meta: int, peso: bool, inicio = 1): 
    cola = [inicio]
    ruta = []
    while len(cola) > 0: 
        vertice = cola.pop(0)
        ruta.append(vertice)
        if vertice == meta: 
            break
        for v in grafo[vertice]: 
            if not peso: 
                temp = v
            else: 
                temp = v[0]
            if temp not in ruta and temp not in cola: 
                cola.append(temp)
    return ruta

def DFS(grafo: dict, meta: int, peso: bool, inicio = 1, ruta = []): 
    #pila.append(inicio)
    #ruta.append(inicio)
    ruta.append(inicio)
    #ruta.append(pila[len(pila)-1])
    if inicio == meta: 
        return ruta
    for v in grafo[inicio]: 
        if not peso: 
            temp = v
        else: 
            temp = v[0]
        if temp not in ruta: 
            ruta = DFS(grafo, meta, peso, temp, ruta)
        if ruta[len(ruta)-1] == meta: 
            break
    return ruta

if __name__=="__main__": 
    dirigido = validar_dirigido()
    #dirigido = True
    print("-"*5)
    
    peso = validar_peso()
    #peso = False
    print("-"*5)
    
    num_nodos = validar_int("Ingrese el número de nodos que contendrá el grafo: ")
    print("-"*5)
    
    k = validar_int("Ingrese el número mínimo de nodos adyacentes: ")
    print("-"*5)

    #grafo = { 1: [6, 8, 10], 2: [5], 3: [8, 4, 1], 4: [7, 6, 1], 5: [6, 9, 1], 6: [7, 4, 9], 7: [9, 3, 4], 8: [5, 10, 2], 9: [4, 10], 10: [2, 3, 6] }

    grafo = generar_instancias(dirigido, peso, num_nodos, k)
    
    print("-"*5)
    
    meta = int(input("Nodo que desea buscar? "))

    print("-"*10)
    print("Breadth First Search")
    tiempo_inicial = time()
    ruta = BFS(grafo, meta, peso)
    print("Recorrido: "+str(ruta))
    print("Nodos visitados: "+str(len(ruta)))
    if meta not in ruta: 
        print("No se encontró el vértice: "+str(meta))
    print("Tiempo de búsqueda: "+str(time()-tiempo_inicial)+"s")
    if peso: 
        print("Distancia: "+str(distancia_BFS(grafo, ruta)))

    print("-"*10)
    print("Depth First Search")
    tiempo_inicial = time()
    ruta = DFS(grafo, meta, peso)
    print("Recorrido: "+str(ruta))
    print("Nodos visitados: "+str(len(ruta)))
    if meta not in ruta: 
        print("No se encontró el vértice: "+str(meta))
    print("Tiempo de búsqueda: "+str(time()-tiempo_inicial)+"s")
    if peso: 
        print("Distancia: "+str(distancia_DFS(grafo, ruta)))
    
    