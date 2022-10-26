from random import randint

def validar_sn(sn): 
    return sn == "s" or sn == "n"

def validar_int(frase: str)->int: 
    while True: 
        try: 
            num = int(input(frase))
        except ValueError: 
            print("Entrada inválida, ingrese un valor entero")
        else: 
            return num

def generar_instancias(): 
    dirigido = input("El grafo será dirigido? S/n: ").lower()
    while not validar_sn(dirigido): 
        dirigido = input("Ingrese únicamente \"S\" o \"N\": ").lower()
    peso = input("Desea que el grafo tenga peso? S/n: ")
    while not validar_sn(peso): 
        peso = input("Ingrese únicamente \"S\" o \"N\": ").lower()
    num_nodos = validar_int("Ingrese el número de nodos que contendrá el grafo: ")
    k = validar_int("Ingrese el número mínimo de nodos adyacentes: ")
    peso_maximo = 100
    nodos = dict()
    for i in range(num_nodos): 
        nodos[i+1] = []

    if peso == "n": 
        for nodo in nodos: 
            for i in range(k): 
                adyacente = randint(1, len(nodos))
                if adyacente != nodo and adyacente not in nodos[nodo]: 
                    nodos[nodo].append(adyacente)
                    if dirigido == "n": 
                        nodos[adyacente].append(nodo)
    else: 
        for nodo in nodos: 
            disponibles = [i+1 for i in range(num_nodos)]
            if dirigido == "n": 
                for num in nodos[nodo]: 
                    disponibles.remove(num[0])
            for i in range(k): 
                adyacente = randint(1, len(nodos))
                p = randint(1, peso_maximo)
                if adyacente != nodo and adyacente in disponibles: 
                    nodos[nodo].append((adyacente, p))
                    if dirigido == "n": 
                        nodos[adyacente].append((nodo, p))
                    disponibles.remove(adyacente)
        


    for key in nodos: 
        print(str(key)+": "+str(nodos[key]))
    return nodos


if __name__=="__main__": 
    dirigido = input("El grafo será dirigido? S/n: ").lower()
    while not validar_sn(dirigido): 
        dirigido = input("Ingrese únicamente \"S\" o \"N\": ").lower()
    peso = input("Desea que el grafo tenga peso? S/n: ")
    while not validar_sn(peso): 
        peso = input("Ingrese únicamente \"S\" o \"N\": ").lower()
    num_nodos = validar_int("Ingrese el número de nodos que contendrá el grafo: ")
    k = validar_int("Ingrese el número mínimo de nodos adyacentes: ")
    peso_maximo = 100
    nodos = dict()
    for i in range(num_nodos): 
        nodos[i+1] = []

    if peso == "n": 
        for nodo in nodos: 
            for i in range(k): 
                adyacente = randint(1, len(nodos))
                if adyacente != nodo and adyacente not in nodos[nodo]: 
                    nodos[nodo].append(adyacente)
                    if dirigido == "n": 
                        nodos[adyacente].append(nodo)
    else: 
        for nodo in nodos: 
            disponibles = [i+1 for i in range(num_nodos)]
            if dirigido == "n": 
                for num in nodos[nodo]: 
                    disponibles.remove(num[0])
            for i in range(k): 
                adyacente = randint(1, len(nodos))
                p = randint(1, peso_maximo)
                if adyacente != nodo and adyacente in disponibles: 
                    nodos[nodo].append((adyacente, p))
                    if dirigido == "n": 
                        nodos[adyacente].append((nodo, p))
                    disponibles.remove(adyacente)
        


    for key in nodos: 
        print(str(key)+": "+str(nodos[key]))