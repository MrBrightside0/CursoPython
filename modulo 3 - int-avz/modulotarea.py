import random as r
from datetime import datetime

def saludar(nombre):
    print(f"Hola, {nombre}!")
    
def despedir(nombre):
    print(f"Adios, {nombre}!")

nombre = input("Escribe tu nombre: ")

bienvenidas = ["Hola como estas ", "Que onda, que cuentas ","Eyeye Aqui "]
print(r.choice(bienvenidas) + nombre)
tiempo = datetime.now()
print(tiempo.strftime("%d/%m/%Y %H:%M"))