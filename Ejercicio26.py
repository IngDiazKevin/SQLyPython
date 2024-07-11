bloques = int(input("Ingresa el numero de bloques: "))

altura = 0

while bloques > altura:
    altura = altura + 1
    bloques = bloques - altura
    
print("LA altura de la piramide :" , altura)