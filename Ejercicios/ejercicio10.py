import Tablero

cuadricula = [
    ["1","1","1"],["","",""],["","",""]
]


def comprobar_filas(cuadricula):
    
    if cuadricula[0][0] == "1" and cuadricula[0][1] == "1" and cuadricula[0][2] == "1":
        return 1
    elif cuadricula[0][0] == "2" and cuadricula[0][1] == "2" and cuadricula[0][2] == "2":
        return 2
    elif cuadricula[1][0] == "1" and cuadricula[1][1] == "1" and cuadricula[1][2] == "1":
        return 1
    elif cuadricula[1][0] == "2" and cuadricula[1][1] == "2" and cuadricula[1][2] == "2":
        return 2
    elif cuadricula[2][0] == "1" and cuadricula[2][1] == "1" and cuadricula[2][2] == "1":
        return 1
    elif cuadricula[2][0] == "2" and cuadricula[2][1] == "2" and cuadricula[2][2] == "2":
        return 2
    else:
        return -1


def comprobar_columnas(cuadricula):

    if cuadricula[0][0] == "1" and cuadricula[1][0] == "1" and cuadricula[2][0] == "1":
        return 1
    elif cuadricula[0][0] == "2" and cuadricula[1][0] == "2" and cuadricula[2][0] == "2":
        return 2
    elif cuadricula[0][1] == "1" and cuadricula[1][1] == "1" and cuadricula[2][1] == "1":
        return 1
    elif cuadricula[0][1] == "2" and cuadricula[1][1] == "2" and cuadricula[2][1] == "2":
        return 2
    elif cuadricula[0][2] == "1" and cuadricula[1][2] == "1" and cuadricula[2][2] == "1":
        return 1
    elif cuadricula[0][2] == "2" and cuadricula[1][2] == "2" and cuadricula[2][2] == "2":
        return 2
    else:
        return -1


def comprobar_diagonales(cuadricula):

    if cuadricula[0][0] == "1" and cuadricula[1][1] == "1" and cuadricula[2][2] == "1":
        return 1
    elif cuadricula[0][0] == "2" and cuadricula[1][1] == "2" and cuadricula[2][2] == "2":
        return 2
    elif cuadricula[0][2] == "1" and cuadricula[1][1] == "1" and cuadricula[2][0] == "1":
        return 1
    elif cuadricula[0][2] == "2" and cuadricula[1][1] == "2" and cuadricula[2][0] == "2":
        return 2
    else:
        return -1
        


def calcular_resultado(cuadricula):

    resultado = comprobar_filas(cuadricula)
    if resultado == 1 or resultado == 2:
        return resultado
    else:
        resultado = comprobar_columnas(cuadricula)
        if resultado == 1 or resultado == 2:
            return resultado
        else:
            resultado = comprobar_diagonales(cuadricula)
            if resultado == 1 or resultado == 2:
                return resultado
            else:
                return -1


def preguntar_jugador(cuadricula, jugador):

    valor_x = int(input(f"Jugador {jugador}, coordenada x: "))
    valor_y = int(input(f"Jugador {jugador}, coordenada y: "))

    if cuadricula[valor_x][valor_y] == "1" or cuadricula[valor_x][valor_y] == "2":
        print("Lo sentimos, esta casilla está ya ocupada, seleccione otra.")
        valor_x = int(input(f"Jugador {jugador}, coordenada x: "))
        valor_y = int(input(f"Jugador {jugador}, coordenada y: "))

    if valor_x >= 0 or valor_x < 3 and valor_y >= 0 or valor_y < 3:
        cuadricula[valor_x][valor_y] = jugador
        T = (Tablero.tablero(cuadricula))
        print(T)

    
final = False

resultado = None

T = (Tablero.tablero(cuadricula))
print(T)

def comprobar_vacia(cuadricula):
    for fila in cuadricula:
        for celda in fila:
            if celda == "":
                return True

    return False        
"""   
comprobar = comprobar_vacia(cuadricula)
print(comprobar)
resultado = calcular_resultado(cuadricula)
print(resultado)
"""

while not final and resultado != -1:
    vacia1 = comprobar_vacia(cuadricula)
    if vacia1:
        jugador1 = preguntar_jugador(cuadricula, "1")
        resultado = calcular_resultado(cuadricula)
        if resultado != -1:
            if resultado ==1:
                print("Jugador 1 gana")
            else:
                print("Jugador 2 gana")
            final = True
        else:
            vacia2 = comprobar_vacia(cuadricula)
            if vacia2:
                jugador2 = preguntar_jugador(cuadricula, "2")
                if calcular_resultado(cuadricula) != -1:
                    if resultado ==1:
                        print("Jugador 1 gana")
                    else:
                        print("Jugador 2 gana")
                    final = True
    else:
        print("esto es un empate")
        final = True
"""            
Hacer función que compruebe si la casilla está ocupada. Si está ocupada que de a elegir otra casilla. Hacerlo bonito

"""        
    
    
    