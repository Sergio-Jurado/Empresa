#imprimir una lista con los números menores de 5.
L= [1,1,2,3,5,8,13,21,34,55,89]
P= []
for elemento in L:
    if elemento<5:
        P.append(elemento)

print(f"Esta es la lista principal: {L}")
print(f"Esta es la lista con los números menores de 5:{P}")