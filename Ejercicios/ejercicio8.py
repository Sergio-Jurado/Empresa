# Escribir en un fichero de texto y después leerlo.
"""
mensaje = input("Escriba el mensaje que desa escribir dentro de un archivo txt: ")
with open("archivo.txt", "w" ) as f:
    f.write(mensaje)
"""
mensaje = input("Escriba el mensaje que desa escribir dentro de un archivo txt: ")
f = open("archivo.txt", "w")
f.write(mensaje)
f.close()
with open("archivo.txt", "r" ) as f:
    lectura = f.read()
print(lectura)