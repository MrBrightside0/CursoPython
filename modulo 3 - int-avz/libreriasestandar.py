#libreria estandar
#python viene con una coleccion de modulos preinstalados, listos para usar. esta "Caja de herramientas"
#se llama libreria estandar e incluye modulos: matematicas, manejo  de fechas, aletoriedad, archivo
#texto, internet entre otros

#math, random y datetime
import math, random
from datetime import datetime

#matematicas
#print(math.sqrt(16))
#print(math.pow(2,3))
#print(math.pi)
#print(math.ceil(3.2)) # redondeo hacia arriba -> 4
#print(math.floor(3.8)) # redondeon hacia abajo -> 3

#random

#print(random.randint(1,6)) #numero aleatorio entre 1 y 6
#print(random.choice(["rojo","azul"])) #elige un elemento aleatorio
#print(random.random()) #decimal aleatorio entre 0 y 1
 
#date time

ahora = datetime.now()
print("Fecha y hora:", ahora)
print("year: ",ahora.year)
print("Mes", ahora.month)
print("Hora", ahora.hour)

#tambien se puede calcular diferencias entre fechas o formatear

fecha = ahora.strftime("%d/%m/%Y %H:%M")

print("Fecha formateada: ", fecha)

