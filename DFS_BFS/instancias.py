from random import randint



def generar_instancias(dirigido: bool, peso: bool, num_nodos: int, k: int, peso_maximo = 100): 
    nodos = dict()
    for i in range(num_nodos): 
        nodos[i+1] = []

    if not peso: 
        for nodo in nodos: 
            for i in range(k): 
                adyacente = randint(1, len(nodos))
                if adyacente != nodo and adyacente not in nodos[nodo]: 
                    nodos[nodo].append(adyacente)
                    if not dirigido: 
                        nodos[adyacente].append(nodo)
    else: 
        for nodo in nodos: 
            disponibles = [i+1 for i in range(num_nodos)]
            if not dirigido: 
                for num in nodos[nodo]: 
                    disponibles.remove(num[0])
            for i in range(k): 
                adyacente = randint(1, len(nodos))
                p = randint(1, peso_maximo)
                if adyacente != nodo and adyacente in disponibles: 
                    nodos[nodo].append((adyacente, p))
                    if not dirigido: 
                        nodos[adyacente].append((nodo, p))
                    disponibles.remove(adyacente)
        


    for key in nodos: 
        print(str(key)+": "+str(nodos[key]))
    return nodos