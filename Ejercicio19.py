year = int(input("Ingresa el año: "))  

if year < 1582:
    print("No esta dentro del rango o calendario Gregoriano")
else:
    if year % 4 != 0 :
        print("Se trata de un año comun")
    elif year % 100 != 0 :
        print("Se trata de un año bisiesto")
    elif year % 400 != 0:
        print("Se trata de un año comun")
    else:
        print("Se trata de un año bisiesto")