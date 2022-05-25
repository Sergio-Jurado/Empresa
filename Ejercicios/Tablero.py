def horizontal(columna):
    resultado = ""
    for elemento in range(columna):
        resultado += " ---"
    return resultado

def vertical(lista):
    resultado = ""
    for elemento in (lista):
        resultado += "|"
        if elemento == "1":
            resultado += " O "
        elif elemento == "2":
            resultado += " X "
        else:
            resultado += "   "

    resultado += "|"
    return resultado


def tablero(cuadricula):
    resultado = ""
    
    for elemento in (cuadricula):
        resultado += horizontal(len(elemento))
        resultado += "\n"
        resultado += vertical(elemento)
        resultado += "\n"
        
    
    resultado += horizontal(len(elemento))
    return resultado