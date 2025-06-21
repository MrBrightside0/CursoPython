nombres = ["Jacobo","Kelly", "Mauricio", "Rebecca"]
edades = [12,113,4,15,161]
mezcla = ["Hola", 12,16.0, True]

#acceder al elemnto de una lista
#print(mezcla[2])

#Slicing rebanado
#print(mezcla[0:2])

#metodos de listas

#append() agrega un elemento a la lista
nombres.append("Edmundo") #no necesariamente tiene que ser un string

#insert() inserta un elmento a la lista (lo inserta en la posicion dada)
edades.insert(2, 12)

#remove() remueve un elemento de una lista
edades.remove(12)

#pop() elimina y retorna un indice
#nombres.pop(0)

#sort()ordenar la lista
nombres.sort()

#reverse() invierte la lista
nombres.reverse()

#len() es una funcion NO ES UN METODO
print(len(nombres))

#FUNCION PRINT("HOLA") METODO VALOR.SORT()

#recorrer una lista
#for nombre in nombres:
#    print(f"Hola tu nombre es {nombre}")

#recoriendo una palabra
#for i in "hola":
#    print(i)

#pedirle al usuario 3 numeros y guardalos en una lista. despues suma todos los numeros
numeros = []

for i in range(3):
    num = int(input(f"Ingrese el  numero {i + 1} "))
    numeros.append(num)
    
print(f"LA suma total es {sum(numeros)}")

#crear una lista vacia, y usar bucle para llenar la lista con los cuadrados del 1 al 10
