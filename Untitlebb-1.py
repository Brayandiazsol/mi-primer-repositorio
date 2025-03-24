#solicita tres numeros y determina cual es el mayor 
q= int(input("ingrese el primer numero: "))
e= int(input("ingrese el segundo numero: "))
w= int(input("ingrese el tercer numero: "))
if q !=w and q !=e and e !=w:
    if q > w:
        if q > e:
            print("el numero mayor es: ",q,)
        else:
            print("el numero mayor es: ",e,)
    else:
         if w > e:
            print("el numero mayor es: ",w,)
         else:
             print("el numero mayor es: ",e,)
else:
    print("hay valores iguales, escriba otros")