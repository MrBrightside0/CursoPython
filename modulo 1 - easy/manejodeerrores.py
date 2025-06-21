
#acosando a usuario para que me de un numero
#while 0 == 0:
#    try:
#        numero = int(input("Dime un numero y lo multiplicare por 10 "))
#        print(f"Tu numero multiplciado por 10 es {numero * 10}")
#        break
#    except:
#        print("Oye mamahuevo te pedi un numero")

#error personalizado
try:
    temperatura = float(input("Introduce la tenperatura en C`: "))
    print(f"la temperatura registrada es {temperatura}")
except ValueError:
    print("Oye baboso eos no es un numero")
    