#Continue - ejemplo

print("Ejemplo de la instruccion continue")

for i in range(1,6):
    if i == 3:
        continue
    print("Estoy dentro del bucle FOR, i =", i)
print("YA SALI del bucle for")