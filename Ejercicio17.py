#Encontrar el numero mas grande entre tres numeros

n1 = int(input("Ingresa el primer numero: "))  # 15
n2 = int(input("Ingresa el segundo numero: ")) # 8
n3 = int(input("Ingresa el tercer numero: "))

#Asumirmos temporalmente que el primero numero es el mas grande
numero_mas_grande = n1 #15 

#Comprobara si n2 es mas grande que n1 (numero_mas_grande)
if n2 > numero_mas_grande:   # 8 > 15 - > False
    numero_mas_grande = n2

#Comprobar si n3 es el mas grande     
if n3 > numero_mas_grande:
    numero_mas_grande = n3
    
print("EL numero mas grande es : ", numero_mas_grande)

