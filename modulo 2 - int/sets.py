#set
#set o conjunto es una coleccion no ordenada y sin elementos repetidos se representa con
#llaves o usando set()

colores = {"Rojo","Azul","Amarillo","Violeta","Blanco","Rojo"} 
colores_pastel = {"Azul","Amarillo","Violeta","Negro","Verde"}
#print(colores)

#metodos y operaciones

#add() agrega un elemento
#colores.add("Morado")
#print(colores)
##remove() elimina un elemento (error si no existe)
#colores.remove("Violeta")
#print(colores)
##discard() elimina sin error si no existe
#colores.discard("violeta")
#print(colores)
##union(colores_pastel) o | une todos los elementos de ambos conjunto sin repetir
#
#print(colores.union(colores_pastel))
#
#print(colores | colores_pastel)
#
##intersection(colroes_pastel) o & devuelve solo los elementos comunes
#
#print(colores.intersection(colores_pastel))
#print(colores & colores_pastel)
#
##difference(colores_pastel) o - devuelve los elementos de colores que no estan en colores_pastel
#print(colores.difference(colores_pastel))
#
#print(colores - colores_pastel)

#Ejercicio rapido
#Crear una BD lista de nombre, tupla con el grupo (A,B,C), un diccionario con nombre: calificacion,
#y un set con calificaciones unicas

nombres = ["Ana","Luis","Pedro","Ana"]
grupo = ("A","B","C")

calificaciones = {
    "Ana" : 90,
    "Luis" : 85,
    "Pedro" : 90
}

calif_unicas = set(calificaciones.values())

print("Estudiantes:",nombres)
print("Grupo:",grupo[0])
print("Calificaciones:",calificaciones)
print("Calificaciones unicas:", calif_unicas)