#Lista, conjunto de datos, vector, array

lista = [4, 9, -6 , 8, 12 , 0, 8, 15 , -44]

print("La lista ORIGINAL es: ",lista)
print("La longitud de la lista ORIGINAL es",  len(lista))
print("El primer elemento de la lista ORIGINAL es ", lista[0])

print("---- MODIFICANDO----")
  
del lista[1]
print("La lista MODIFICADA es: ",lista)
print("La longitud de la lista MODIFICA es",  len(lista))
print("El primer elemento de la lista MODIFICADA es ", lista[0])
