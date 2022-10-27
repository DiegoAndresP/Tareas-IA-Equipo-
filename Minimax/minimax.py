from ast import While
from math import inf
from random import randint
import time

from numpy import disp

def imprimir_tablero(tablero: dict): 
    print(tablero[7]+"|"+tablero[8]+"|"+tablero[9])
    print("-+-+-")
    print(tablero[4]+"|"+tablero[5]+"|"+tablero[6])
    print("-+-+-")
    print(tablero[1]+"|"+tablero[2]+"|"+tablero[3])

def final(tablero: dict, disponibles: list): 
    for i in range(3): 
        if tablero[i*3+1] == tablero[i*3+2] == tablero[i*3+3] and tablero[i*3+1] != " ": 
            return True
        elif tablero[i+1] == tablero[i+4] == tablero[i+7] and tablero[i+1] != " ": 
            return True
    if tablero[1] == tablero[5] == tablero[9] and tablero[1] != " ": 
        return True
    elif tablero[3] == tablero[5] == tablero[7] and tablero[3] != " ": 
        return True
    if len(disponibles) == 0: 
        return True
    return False

def ganador(tablero: dict, marca: str): 
    for i in range(3): 
        if tablero[i*3+1] == tablero[i*3+2] == tablero[i*3+3] != " ": 
            if tablero[i*3+1] == marca: 
                return 1
            else: 
                return -1
        elif tablero[i+1] == tablero[i+4] == tablero[i+7] and tablero[i+1] != " ": 
            if tablero[i+1] == marca: 
                return 1
            else: 
                return -1
    if tablero[1] == tablero[5] == tablero[9] and tablero[1] != " ": 
        if tablero[1] == marca: 
            return 1
        else: 
            return -1
    elif tablero[3] == tablero[5] == tablero[7] and tablero[3] != " ": 
        if tablero[3] == marca: 
            return 1
        else: 
            return -1
    return 0

def turno_jugador(tablero: dict, disponibles: list, marca: str): 
    movimiento = 0
    while movimiento not in disponibles: 
        print("Disponibles: "+str(disponibles))
        movimiento = int(input("Movimiento: "))
    tablero[movimiento] = marca
    disponibles.remove(movimiento)

def funcion_heuristica(disponibles: list)->int: 
    return len(disponibles) + 1

def minimax(tablero: dict, disponibles: list, marca: str, Max = True):
    enemigo = "O" if marca == "X" else "X"
    if final(tablero, disponibles): 
        return {"posicion": 0, "valor": ganador(tablero, marca) * funcion_heuristica(disponibles)}
    if Max: 
        movimiento = {"posicion": 0, "valor": -inf}
        valor = -inf
        for num in disponibles: 
            temp_disponibles = disponibles.copy()
            temp_disponibles.remove(num)
            tablero[num] = marca
            valor = max(valor, minimax(tablero, temp_disponibles, marca, False)["valor"])
            tablero[num] = " "
            if movimiento["valor"] != valor: 
                movimiento["valor"] = valor
                movimiento["posicion"] = num
    else: 
        movimiento = {"posicion": 0, "valor": inf}
        valor = inf
        for num in disponibles: 
            temp_disponibles = disponibles.copy()
            temp_disponibles.remove(num)
            tablero[num] = enemigo
            valor = min(valor, minimax(tablero, temp_disponibles, marca, True)["valor"])
            tablero[num] = " "
            if movimiento["valor"] != valor: 
                movimiento["valor"] = valor
                movimiento["posicion"] = num
    return movimiento

def turno_bot_genio(tablero: dict, disponibles: list, marca: str):
    tiempo_inicio = time.time()
    movimiento = minimax(tablero, disponibles, marca)
    print("Movimiento: "+str(movimiento))
    print("Tiempo de execución: "+str(time.time()-tiempo_inicio)+"s")
    tablero[movimiento["posicion"]] = marca
    disponibles.remove(movimiento["posicion"])

def turno_bot_tonto(tablero: dict, disponibles: list, marca: str): 
    mov = disponibles[randint(0, len(disponibles)-1)]
    tablero[mov] = marca
    disponibles.remove(mov)

def validar_zero_uno()->int: 
    while True: 
        num = 0
        try: 
            num = int(input("Ingrese 0 para jugar primero, 1 para que el bot juegue primero: ").strip())
        except ValueError: 
            print("Ingrese un valor válido")
        else: 
            if num == 1 or num == 0: 
                return num

def validar_sn()->bool: 
    sn = ""
    while sn != "s" and sn != "n": 
        sn = input("Desea recibir ayuda? S/n: ")
    return sn == "s"

if __name__=="__main__": 
    tablero = dict()
    for i in range(9): 
        tablero[i+1] = " "
    disponibles = [i+1 for i in range(9)]
    jugador = "X"
    bot = "O"
    turno = validar_zero_uno()
    ayuda = validar_sn()
    for i in range(9): 
        imprimir_tablero(tablero)
        if i%2 == turno: 
            if ayuda: 
                tiempo_inicial = time.time()
                print("Mejor movimiento: "+str(minimax(tablero, disponibles, jugador)))
                print("Tiempo: "+str(time.time()-tiempo_inicial))
            turno_jugador(tablero, disponibles, jugador)
        else:
            if ayuda: 
                turno_bot_tonto(tablero, disponibles, bot)
            else: 
                turno_bot_genio(tablero, disponibles, bot)
        print("-"*20)
        if i>=4 and final(tablero, disponibles): 
            break
    imprimir_tablero(tablero)
    campeon = ganador(tablero, jugador)
    if campeon == 1: 
        print("Ganó la humanidad")
    elif campeon == -1: 
        print("Ganó el bot")
    else: 
        print("Empate")