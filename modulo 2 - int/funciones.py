#sintaxis de una funcion

def nombre_de_la_funcion():
    #bloque de codigo
    print("hola como estas!")

#Ejemplo 1
def mostrar_menu():
    print("1. Ver perfil")
    print("2. Editar perfil")
    print("3. Salir")
    
#mostrar_menu()

#hacer funciona que se llame mi_firma 
def mi_firma():
    print("Me llamo Edmundo y Estudio IA")


def sumar_numeros():
    num1 = int(input("dime un numero: "))
    num2 = int(input("dime otro numero: "))
    print(f"la suma de {num1} y {num2} es igual a {num1 + num2}")
    


#esta es una funcion con parametros
def multiplicacion_por_5(numero):
    print(f"tu numero multiplicado por 5 es: {numero * 5}")
    
#multiplicacion_por_5(23)

#return la palabra hace referencia a que una funcion devuelva un resultado
def suma(a,b):
    return a + b
# se usa return cuando queires guardar algo en una variable

#resultado = suma(4,5)
#print(f"la suma es: {resultado}")


#que pasa si no se usa return
def mostrar():
    print('Hola')
    
#resultado = mostrar()
#print(f"El resultado es {resultado}")
    
#verificar si un numero es par

def es_par(numero):
    return numero % 2 == 0

if es_par(6):
    print("el numero es par")
else:
    print("el numero es impar")
    
#funcion que reciba tres numeros y devuelva el mayor
def mayor_de_tres(a,b,c):
    return max(a,b,c)