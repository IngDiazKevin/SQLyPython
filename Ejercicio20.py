contador_par = 0
contador_impar = 0

while True:
    numero = int(input("Ingresa un numero: "))
    
    if numero == 0:
        break
    
    #Analisis de un numero par
    if numero %2 == 0: 
        contador_par = contador_par + 1
    #Analisis de un numero impar    
    else:
        contador_impar = contador_impar + 1
        
    
    
print("Numeros pares introducidos: ", contador_par)
print("Numero impares introducidos: ", contador_impar)
        
