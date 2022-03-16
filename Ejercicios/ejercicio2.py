#Pregunta al ususario un número y dependiendo de si es par o impar imprime la respuesta adecuada
numero = int(input("Dígame un número y le adivinaré si es par o impar: "))
if numero%2 == 0:
    print("El número es par")
else:
    print("El número es impar")
