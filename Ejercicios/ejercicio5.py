#Teniendo estas dos listas escribe un programa que devuelva una lista que solo tenga los elementos comunes sin duplicar
lista1=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lista2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lista3=[]
elemento = 0
for elemento in lista1:
    if elemento in lista2:
        if elemento not in lista3:
            lista3.append(elemento)
print(lista3)
    