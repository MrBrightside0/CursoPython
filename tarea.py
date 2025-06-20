#un programa que cheque si una palabra es palindromo 
palabra = "python"


for i in range(0,len(palabra)):
    j = (i * -1) -1
    if palabra[i] == palabra[j]:
        continue
    else:
        print("la palabra no es un palindromo")
        break
else:
    print("la palabra es un palindromo")

#hacer una ruleta rusa

eleccion = int(input("escoge un numero del 1 al 6: "))
if eleccion == 3:
    while 0 == 0:
        print("gg te moriste")
else:
    print("saliste vivo yay")