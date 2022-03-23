#Crea un programa en el que se le pregunte al usuario un número y se realize una lista con todos sus divisores
lista =[]
print("introduzca el numero")
numero = int(input()) #aquí se lee el número entero
print("los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        lista.append(divisor)
print(lista)