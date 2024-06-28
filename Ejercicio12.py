hora = int(input('Ingresa la hora: '))
min = int(input('Inngresa los minutos: '))
duracion = int(input('Ingresa la duracion del evento en min: '))

suma  = min + duracion
hora_fin = suma//60
minutos_fin = suma  % 60

hora_total = (hora+hora_fin) % 24
print('El evento termina', hora_total, ':', minutos_fin)
