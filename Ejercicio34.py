#Paso 1: Crear lista vacia
beatles = []

#Paso 2: agregar con append
beatles.append("John Lennon")
beatles.append("Paul Mc")
beatles.append("George Harrison")
print("Paso 2: ", beatles)

#PAso 3:
for miembros in ["Stu Sutcliffe ", "Pete Best"]:
    beatles.append(miembros)
    
print("PAso 3: ", beatles)

#paso 4: eliminar
del beatles[-1] #Eliminar a Pete
del beatles[-1] #Eliminar a Stu
print("PAso 4:" , beatles)

#Paso 5: insertar al principio:

beatles.insert(0,"Ringo Star")
print("Paso 5:" , beatles)