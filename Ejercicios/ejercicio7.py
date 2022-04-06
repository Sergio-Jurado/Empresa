#Piedra papel o tijera
parar = False
while not parar:
    eleccion1 = input("Jugador 1, estás jugado a piedra papel o tijera, juega contra Jugador 2. \n 1. piedra. \n 2. papel. \n 3. tijera.\n")
    if eleccion1 == "1" or eleccion1 == "2" or eleccion1 == "3":
        print("El jugador 1 ha elegido " + eleccion1)
        parar = True
    else:
        print("Valor incorrecto. Vuelva a elegir.")

while parar == True:
    eleccion2 = input("Jugador 2, estás jugado a piedra papel o tijera, juega contra Jugador 1. \n 1. piedra. \n 2. papel. \n 3. tijera.\n")
    if eleccion2 == "1" or eleccion2 == "2" or eleccion2 == "3":
        print("El jugador 2 ha elegido " + eleccion2)
        parar = False
    else:
        print("Valor incorrecto. Vuelva a elegir.")
        
if eleccion1 == eleccion2:
    print("Habéis pensado lo mismo, es un empate.")
if eleccion1 == "1": 
    if eleccion2 == "2":
        print("Jugador 2 gana.")
    if eleccion2 == "3":
        print("Jugador 1 gana.")
if eleccion1 == "2": 
    if eleccion2 == "1":
        print("Jugador 1 gana.")
    if eleccion2 == "3":
        print("Jugador 2 gana.")
if eleccion1 == "3": 
    if eleccion2 == "1":
        print("Jugador 2 gana.")
    if eleccion2 == "2":
        print("Jugador 1 gana.")