#Estructura completa: try/ except/ else/finally

#try:
#    #intento de codigo
#except:
#    #que hace si hay un error
#else:
#    #si no hay error 
#finally:
#    #siempre se ejecuta

#try: 
#    numero = int(input("Ingresa un numero"))
#    resultado = 10 / numero
#except ValueError:
#    print("Eso no es un numero valido")
#except ZeroDivisionError:
#    print("No se puede dividir entre 0")
#else:
#    print("Resultado: ", resultado)
#finally:
#    print("Gracias por usar este programa")
    

#ValueError : Conversion invalida
#ZeroDivisionError : error al dividir entre 0
#IndexError: Accedes a un indice que no existe 
#KeyError: CLave inexistente en un diccionario
#TypeError: Operacion entre tipos incompatibles
#FileNotFoundError: EL archivo no existe

#try:
#    lista = [1,2,3]
#    print(lista[3])
#except (IndexError, ValueError) as e:
#    print("Error: ", e)

#Lanzar tus propios errores con raise

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    print("Edad valida:", edad)

try:
    verificar_edad(-5)
except ValueError as e:
    print("Error", e)

