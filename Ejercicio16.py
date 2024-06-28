#Leer los valores de entrada
n1= int(input('Ingresa el primer num: '))
n2= int(input('Ingresa el segun num: '))

#Desicion / elegir el num + grande
if n1>n2:
    numero_mas_grande = n1
    print('hola soy el if')
else:
    numero_mas_grande = n2
    print('hola soy el else')
#Mostrar el mensaje
print('Hola ya sali del if/else')    
print('El numero mas grande es:' , numero_mas_grande)