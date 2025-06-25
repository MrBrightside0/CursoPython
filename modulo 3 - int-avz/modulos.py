

#modulos
#un modulo es simplemente un archivo .py que contiene codigo reutilizable, como funciones, 
# variables o clases
#puedes crear tu propio modulo, importar los modulos de python o instalar modulos externos 

#importar modulo completo
#import math #importacion de un modulo completo
#print(math.sqrt(25))
#print(math.pi)

#importar una sola parte
#from math import sqrt, pi
#print(sqrt(25))
#print(pi)

#importar con alias
#import math as m
#print(m.pow(2,3))

import utils

print(utils.saludar("Mauricio"))
print(utils.cuadrado(4))