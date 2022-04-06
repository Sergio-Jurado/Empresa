#Preguntar al usuario un número y decir si es capicuo o no
numero = input("escriba una lista de caracteres y le pondré en una lista todas aquellas que sean capicuas: ")
if len(numero)%2 == 0:
    cad1 = numero[:len(numero) // 2]
    cad2 = numero[len(numero) // 2:]
    if cad1 == cad2[::-1]:
        print("es capicuo")  
else:
    cad3 = numero[:len(numero) // 2]
    cad4 = numero[(len(numero) // 2)+1:]
    if cad3 == cad4[::-1]:
        print("no es capicuo")