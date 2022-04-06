#Piedra papel o tijera con funciones
def menu (nombre):
    parar = False
    while not parar:
        eleccion = input(f"{nombre}, estás jugado a piedra papel o tijera. \n 1. piedra. \n 2. papel. \n 3. tijera.\n")
        if eleccion == "1" or eleccion == "2" or eleccion == "3":
            if eleccion == "1":
                print(f"{nombre} ha elegido piedra")
            if eleccion == "2":
                print(f"{nombre} ha elegido papel")
            parar = True
            if eleccion == "3":
                print(f"{nombre} ha elegido tijera")
        else:
            print("Valor incorrecto. Vuelva a elegir.")
    return eleccion


J1 = input("Nombre del jugador 1: ")
eleccion1 = menu(J1)

J2 = input("Nombre del jugador 2: ")
eleccion2 = menu(J2)

if eleccion1 == eleccion2:
    print("Habéis pensado lo mismo, es un empate.")
if eleccion1 == "1": 
    if eleccion2 == "2":
        print(f"{J2} gana.")
    if eleccion2 == "3":
        print(f"{J1} gana.")
if eleccion1 == "2": 
    if eleccion2 == "1":
        print(f"{J1} gana.")
    if eleccion2 == "3":
        print(f"{J2} gana.")
if eleccion1 == "3": 
    if eleccion2 == "1":
        print(f"{J2} gana.")
    if eleccion2 == "2":
        print(f"{J1} gana.")
