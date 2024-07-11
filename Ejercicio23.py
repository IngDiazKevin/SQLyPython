#break ejemplo con FOR

print("Inicio de la instruccion break:")

for i in range(1,6):
    if i == 3:
        break
    print("Estoy dentro del bucle for, el valor de i = ", i)
print("YA SALI , estoy fuera del bucle")