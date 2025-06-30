#Que es un archivo txt

#"r" (read) leer [error si no existir el archivo]
#"w" (write) escribir [borra todo lo anterior]
#"a" (add) agrega al final
#"x" crear un nuevo archivo (error si ya existe)

#Leyendo archivo linea por linea
#with open("archivo.txt","r") as archivo:
#    for linea in archivo:
#        print(linea.strip())
        
#Escribir y sobrescribir ("w")

#with open("datos.txt","w") as archivo:
#    archivo.write("Segunda linea\n")
#    archivo.write("Primera linea\n")
    
    
#agregamos datos sin borrar
#with open("datos.txt","a") as archivo:
#    archivo.write("Linea added\n")


#Leer y guardar datos de archivo en lista
with open("nombres.txt","r") as archivo:
    lista_nombres = [linea.strip() for linea in archivo]
    print(lista_nombres)
    
    