#Demana introduḯr dos nombres
num1=int(input("Introdueix el primer numero"))
num2=int(input("Introdueix el segon numero"))

#Fa les operacions que nosaltres volem amb el nombres que hem introduit antes
suma=num1+num2
resta=num1-num2
multiplicació=num1*num2

#És per a fer una condició en aquest cas es per a dir que entre 0 no es pot dividir
if num2 !=0:
    divisio=num1/num2
else:
    divisio="No es pot dividir entre 0"

#Resultats de les operacions
print(f"suma {suma}")
print(f"resta {resta}")
print(f"multiplicació {multiplicació}")
print(f"divisio {divisio}")


