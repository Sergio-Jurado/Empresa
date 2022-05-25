#Dibujar en el terminal un tablero se le pregunta al usuario el tamaño 
"""
 --- --- --- 
|   |   |   |
 --- --- --- 
|   |   |   |
 --- --- --- 
|   |   |   |
 --- --- ---

print(" --- \n|   |\n ---")
print(" --- --- \n|   |   |\n --- --- \t\n|   |   |\n --- --- ")
print(" --- --- --- \n|   |   |   |\n --- --- --- \t\n|   |   |   |\n --- --- --- \t\n|   |   |   |\n --- --- --- ")

i = int(input("Medida del cuadrado: "))
j = i
if i == 1:
    print(" --- \n|   |\n ---")
else: 
    for elemento in range (1,i+1):
        resultado1 = (" --- \n|   |\n ---")
        for elemento in range(1,j):
            resultado2 = ("\n|   |\n ---")
        resultadof = (resultado1 + resultado2)*i
        print (resultadof)

print(" ---")
print("|   |")
print(" ---")

print(" --- ---")
print("|   |   |")
print(" --- ---")
print("|   |   |")
print(" --- ---")

print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")


def horizontal(numero):
    resultado = ""
    for elemento in range (numero):
        resultado = resultado + (" ---")
    return resultado 


def vertical(numero):
    resultado = ""
    for elemento in range (numero+1):
        resultado = resultado + ("|   ")
    return resultado

def tablero(numero):
    resultado = ""
    
    for elemento in range (tamamo):
        resultado = resultado + (horizontal(tamamo) + "\n")
        resultado = resultado +(vertical(tamamo) + "\n")
    
    
    resultado = resultado + (horizontal(tamamo))
    return resultado

tamamo = int(input("escribe un número: "))

T = (tablero(tamamo))
with open("archivo.txt", "w" ) as f:
    f.write(T)
"""
from Tablero import tablero

def crear_tabla(numero):
    resultado=[]
    for i in range(numero):
        temporal=[]
        for j in range(numero):
            temporal+=[""]
        
        resultado+=[temporal]

        
    return resultado
    
    
 

tamano=int(input("¿De cuanto quieres que sea tu tablero? "))
crear=crear_tabla(tamano)
print(crear)  


p=tablero(crear)
print(p)