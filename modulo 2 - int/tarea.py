#pide al usuario su nombre,edad, y año actual.
#crea una funcion que calcule su año de nacimiento y devuelve el mensaje "Hola juan, naciste en 2005"

def informacion(nombre, year, edad):
    print(f"Hola {nombre}, naciste en {year - edad}")


while 0 == 0:
    try:
        nombre = input("Cual es tu nombre? ")
        edad = int(input("Cual es tu edad? (solo numeros) "))
        year = int(input("Cual es el año actual? (solo numeros) "))
        informacion(nombre,year,edad)
        break
    except ValueError:
        print("Vuelve a intentar y especifica los valores correctamente") 
        

#investiguen sobre la llistas mixtas o matrices y listas vacias y traer un ejemplo

