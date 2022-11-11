from random import randint
from math import inf

def evaluar_peso(sol: str, w: list)->int: 
    peso = 0
    for i in range(len(sol)): 
        peso += w[i]*int(sol[i])
    return peso

def generar_solucion(w: list, p_max: int)->str: 
    n = len(w)
    solucion = ""
    for i in range(n): 
        solucion += str(randint(0, 1))
    while evaluar_peso(solucion, w) > p_max: 
        solucion = ""
        for i in range(n): 
            solucion += str(randint(0, 1))
    return solucion

def evaluar_beneficio(sol: str, b: list)->int: 
    beneficio = 0
    for i in range(len(sol)): 
        beneficio += b[i]*int(sol[i])
    return beneficio

def seleccion(pob: list, b: list): 
    n_muestra = len(pob)//20
    solucion = ""
    for i in range(n_muestra): 
        muestra = pob[randint(0, len(pob)-1)]
        if evaluar_beneficio(muestra, b) > evaluar_beneficio(solucion, b): 
            solucion = muestra
    return solucion

def cruce(padre, madre, w: list, p_max: int, probabilidad = 90): 
    if randint(1, 100) <= probabilidad: 
        n = len(padre)//2
        h1 = padre[:n] + madre[n:]
        h2 = madre[:n] + padre[n:]
        if evaluar_peso(h1, w) > p_max: 
            h1 = padre
        if evaluar_peso(h2, w) > p_max: 
            h2 = madre
        return h1, h2
    return padre, madre

def mutacion(sol: str, w: list, p_max: int, probabilidad = 5): 
    if randint(1, 100) <= probabilidad: 
        n = randint(0, len(sol)-1)
        mutante = sol[:n]
        mutante += "0" if sol[n] == "1" else "1"
        mutante += sol[n+1:]
        if evaluar_peso(sol, w) <= p_max: 
            return mutante
    return sol

def genetico(p_max: int, b: list, w: list, n_pob = 100, n_gen = 10): 
    poblacion = list()
    for p in range(n_pob): 
        poblacion.append(generar_solucion(w, p_max))
    mejor_solucion = ""
    mejor_valor = -inf*9
    for g in range(n_gen): 
        seleccionados = [seleccion(poblacion, b) for i in range(n_pob)]
        hijos = list()
        for i in range(0, n_pob, 2): 
            padre, madre = seleccionados[i], seleccionados[i+1]
            for hijo in cruce(padre, madre, w, p_max): 
                mutacion(hijo, w, p_max)
                hijos.append(hijo)
                if evaluar_beneficio(hijo, b) > mejor_valor: 
                    mejor_solucion = hijo
                    mejor_valor = evaluar_beneficio(hijo, b)
        poblacion = hijos
    return (mejor_solucion, mejor_valor)

if __name__ == "__main__":
    peso_maximo = 879
    beneficios = [91, 72, 90, 46, 55, 8, 35, 75, 61, 15, 77, 40, 63, 75, 29, 75, 17, 78, 40, 44]
    pesos = [84, 83, 43, 4, 44, 6, 82, 92, 25, 83, 56, 18, 58, 14, 48, 70, 96, 32, 68, 82]
    solucion, valor = genetico(peso_maximo, beneficios, pesos, 1000, 20)
    print("Mejor solución: "+solucion)
    print("Mejor valor: "+str(valor))