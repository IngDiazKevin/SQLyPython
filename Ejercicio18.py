ingreso = float(input("Introduce el ingreso anual: "))

if ingreso < 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - 85528) * 0.32 + 14839.02
    
if impuesto < 0.0:
    impuesto = 0
    
impuesto_final = round(impuesto,0)

print("El impuesto a pagar es: ", impuesto_final, " pesos")
