#Crear un programa que pregunte al usuario su nombre y su edad y responda en qué año tendrá 100 años


nombre = input ("¿Cómo te llamas?: ")
edad = input ("¿Cuántos años tienes?: ")
edad= int(edad)
total = 2022 - edad + 100
total = str(total)
edad = str(edad)
message = 'Hola ' + nombre + ' tienes ' + edad + ' años Y cumplirás 100 años en ' + total
print(message)