#Demana tres nombres diferents
num1 = (int(input("Introduïx el primer nombre")))
num2 = (int(input("Introduïx el segon nombre")))
num3 = (int(input("Introduïx el tercer nombre")))

#Determinar quin és el major
if num1 > num2 and num1 > num3:
    print("El nombre més gran és:", num1)
elif num2 > num1 and num2 > num3:
    print("El nombre més gran és:", num2)
else:
    print("El nombre més gran és:", num3)