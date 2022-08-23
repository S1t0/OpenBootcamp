from datetime import datetime 
from datetime import timedelta


horaActual=datetime.now()
horaActualBien=horaActual.strftime("%H:%M:%S")
horaDeSalida="21:00:00"
print(horaActualBien)
print("Hora de salida",horaDeSalida)
if horaActualBien >= horaDeSalida:
    print("Hora de salir, son las",horaActualBien)

else:
    if horaActualBien >= "09:00:00" and horaActualBien < "21:00:00":
        tiempo=horaActual + timedelta(hours=21,seconds=00,minutes=00)
        print("Falta para salir",tiempo.strftime("%H:%M:%S"))

