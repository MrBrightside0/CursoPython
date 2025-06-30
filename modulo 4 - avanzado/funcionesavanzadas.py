#Ampliar el dominio de las funciones
#USar multiples de retorno: una funcion puede devolver mas de un valor usando comas, python los regres acomo tuplas

#def estadisticas(lista):
#    suma = sum(lista)
#    promedio = suma / len(lista)
#    maximo = max(lista)
#    return suma, promedio, maximo
#
#datos = [1,2,3,4,5,6,7]
#
#sumatoria, promedio, maximo = estadisticas(datos)
#print("Suma:", sumatoria)
#print("Promedio:", promedio)
#print("Maximo:", maximo)

#Definir valores por defecto
#def bienvenida(nombre="invitado",idioma="espanol"):
#    if idioma == "espanol":
#        print(f"Hola {nombre}, bienvenido")
#    elif idioma == "ingles":
#        print(f"Hello {nombre}, welcome")
#    else:
#        print(f"{nombre}, idioma no soportado")
#
#bienvenida()
#bienvenida("alex","ingles")

#Usar argumentos

#def producto(nombre, precio, categoria):
#    print(f"Producto: {nombre} | Precio: {precio} | Categoria: {categoria}")
#
#producto(precio=150,categoria="Ropa",nombre="Camisa") #Unicamente se puede hacer si conoces el nombre de las variables

#Ver que es *args  permite una cantidad indefinida de argumentos posicionales como una tupla
#def sumar(*numeros):
#    print("Recibi: ", numeros)
#    return sum(numeros)
#
#print(sumar(1,2,3,4,5))

# **kwargs permite pasar una cantidad indefinida de argumentos nombrados, como un diccionario
#def mostrar_info(**datos):
#    for clave, valor in datos.items():
#        print(f"{clave}: {valor}")
#
#mostrar_info(nombre="Ana", edad=22,carrera="IIA")