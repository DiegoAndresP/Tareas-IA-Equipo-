from random import randint, randrange

def calcular_peso(sol: str, p: list)->int: 
    peso = 0
    for i in range(len(sol)): 
        peso += int(sol[i])*p[i]
    return peso


def generar_solucion(p: list, p_max: int)->int: 
    solucion = ""
    for i in range(len(p)): 
        solucion += str(randint(0, 1))
    while calcular_peso(solucion, p) > p_max: 
        solucion = ""
        for i in range(len(p)): 
            solucion += str(randint(0, 1))
    return solucion

def evaluar_beneficio(sol: str, b: list)->int: 
    valor = 0
    for i in range(len(sol)): 
        valor += int(sol[i])*b[i]
    return valor

def seleccion(pob: list, val: list): 
    n_muestra = len(pob)//10
    seleccionados = [randint(0, len(pob)-1) for i in range(n_muestra)]
    mejor = seleccionados[0]
    for selec in seleccionados: 
        if val[selec] > val[mejor]: 
            mejor = selec
    return pob[mejor]

def cruce(p1: str, p2: str, pesos: list, p_max: int, p_cruce = 90): 
    hijo1 = p1
    hijo2 = p2
    if randint(1, 100) <= p_cruce: 
        medio = len(p1)//2
        if calcular_peso(p1[:medio]+p2[medio:], pesos) <= p_max: 
            hijo1 = p1[:medio]+p2[medio:]
        if calcular_peso(p2[:medio]+p1[medio:], pesos) <= p_max: 
            hijo2 = p2[:medio]+p1[medio:]
    return [hijo1, hijo2]

def mutacion(hijo: str, pesos: list, p_max: int, probabilidad = 5): 
    if randint(1, 100) <= probabilidad: 
        pos = randint(0, len(hijo)-1)
        bit = "1" if hijo[pos] == "0" else "0"
        if calcular_peso(hijo[:pos]+bit+hijo[pos+1:], pesos) <= p_max: 
            hijo =  hijo[:pos]+bit+hijo[pos+1:]

def algoritmo_genetico(p_max: int, beneficios: list, pesos: list, n_poblacion: int, n_gen: int): 
    poblacion = [generar_solucion(pesos, p_max) for i in range(n_poblacion)]
    #print(poblacion)
    mejor = poblacion[0]
    mejor_valor = evaluar_beneficio(poblacion[0], beneficios)
    for gen in range(n_gen): 
        valores = [evaluar_beneficio(i, beneficios) for i in poblacion]
        print(valores)
        for i in range(n_poblacion): 
            if valores[i] > mejor_valor: 
                mejor = poblacion[i]
                mejor_valor = valores[i]

        seleccionados = [seleccion(poblacion, valores) for i in range(n_poblacion)]

        hijos = list()
        for i in range(0, n_poblacion, 2): 
            padre1, padre2 = seleccionados[i], seleccionados[i+1]
            for hijo in cruce(padre1, padre2, pesos, p_max): 
                mutacion(hijo, pesos, p_max)
                hijos.append(hijo)
        poblacion = hijos
    return mejor, mejor_valor
        


if __name__ == "__main__":
    peso_maximo = 879
    beneficios = [91, 72, 90, 46, 55, 8, 35, 75, 61, 15, 77, 40, 63, 75, 29, 75, 17, 78, 40, 44]
    pesos = [84, 83, 43, 4, 44, 6, 82, 92, 25, 83, 56, 18, 58, 14, 48, 70, 96, 32, 68, 82]
    mejor, mejor_valor = algoritmo_genetico(peso_maximo, beneficios, pesos, 5000, 20)
    print("Mejor solución: "+mejor)
    print("Mejor valor: "+str(mejor_valor))
