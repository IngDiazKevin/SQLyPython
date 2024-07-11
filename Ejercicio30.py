lista = [1,2,3,4,5]
#PAso 1
lista[2] = int(input("Ingrese el numero para reemplazar: "))

#Paso 2
del lista[-1]

#Paso 3
print("La longitud de la lista es: ", len(lista))

print(lista)