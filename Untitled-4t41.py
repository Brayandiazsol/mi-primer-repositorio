# pide una nota entre 0 y 100 e imprime la calificacion
nota= float(input("ingrese una nota de 1 a 100: "))
if 90<=nota<=100:
            print("exelente")
elif 70<=nota<=89:
    print("aprovado")
elif 0<=nota<=69:
    print("reprobado")
else:
    print("nota fuera de rango")