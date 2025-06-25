#tuplas
#mas ligeras y rapidas que las listas y son INMUTABLES

persona = ("Juan", 25, "Mexico")

#print(persona[0]) #'Juan'
#print(persona[-1]) #"Mexico"

dias = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

#print(dias[0])
#print(dias[-1])

#dicionarios
#coleccion de pares clave:valor

alumno = {
    'nombre' : 'Ana',
    "edad" : 20,
    'carrera' : 'IA'
}

#print(alumno["edad"])


#metodos utiles 
#key() te dice las claves del diccionario
#print(alumno.keys())
#value() te regresa los valores del diccionario
#print(alumno.values())
#items() devuelve clave y valor
#print(alumno.items())
#get((clave) obtiene un valor (mejor practica)
#print(alumno.get("edad"))

#update() modificar/ agregar elementos

calificacion = {
    "edad" : 21,
    "promedio" : 70
}


alumno.update(calificacion)
#print(alumno)


#pop(clave) eliminar un par por clave
alumno.pop("edad")
#print(alumno)

#ejercicio rapido
#crear un diccionario que guarde datos de un libro (titulo, autor y year) luego pide al usuario cambio de nombre

libro = {
    "titulo" : 'Me robe el metodo de gauss jordan',
    "autor" : "montante",
    "year" : 1934
}

print("Datos  originales: ", libro)

nuevo_nombre = input("Nuevo nombre del libro: ")
#metodo para remplazar por clave
libro["titulo"] = nuevo_nombre

print("Datos actualizados: ", libro)
