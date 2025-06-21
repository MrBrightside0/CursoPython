#indice en computadora
palabra = "computadora"
#print(palabra[0])

#imprimir ultimo caracter 
#print(palabra[-1])

#imprimir ciertos caracteres
#print(palabra[3:7])

#bucle for 
#for i in range(100):
#    print(i + 1)
    
#bucle while
#num = 2
#while num <= 10000000000000000000000000000000000000000000000000000000000000:   
#    print(num)
#    num += 2
#    
#    #uso del break
#    if num >= 1000:
#        break
    
#uso de continue
#for i in range(1,6):
#    if i == 3:
#        continue
    
#    print(i)

#uso de else (programa que busca un numero en una lista)
numeros = [3,7,12,5,9]
buscado = 5

for hu in numeros:
    if hu == buscado:
        print("Se encontro el numero!!!")
        break
else:
    print("No se encontro un numero")
    