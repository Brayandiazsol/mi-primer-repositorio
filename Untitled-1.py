# Escribir un programa que determine si un numero ingresado es poositivo, negativo o cero
n = int(input("igrese un numero: "))
if n == 0:
   print("el numero",n," es cero ")
else:
    if n<0:
        print("el numero",n,"es negativo ")
    else:
        print("el numero",n,"es positivo ")