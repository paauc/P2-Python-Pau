#Training 1 Exercici 1

def calcul_area():
   base = float(input("Base: "))
   altura = float(input("Altura: "))
   area = (base * altura) / 2
   print(f"L'àrea del cuadrat és: {area}") 

#Training 1 Exercici 2

def operacions():
    num1=float(input("Primer nombre:"))
    num2=float(input("Segon nombre:"))
    
    suma=num1+num2  # ✅ Dentro de la función
    resta=num1-num2  # ✅ Dentro de la función
    multiplicacio=num1*num2
    
    if num2!=0:
        divisio=num1/num2
    else:
        divisio="No es pot dividir entre 0"
    
    print(f"suma {suma}")
    print(f"resta {resta}")
    print(f"multiplicacio {multiplicacio}")
    print(f"divisio {divisio}")


#Training 2 Exercici 3


def frases():
    paraula1=input("Introdueix la 1ra paraula:")
    paraula2=input("Introdueix la 2na paraula:")
    paraula3=input("Introdueix la 3ra paraula:")

    enter1=int(paraula1)
    enter2=int(paraula2)    

    frase=paraula1+""+paraula2+""+paraula3
    print("La frase resultant és:",frase)   

#Training 2 Exercici 4

def casting():
    a=float(input("Primer nombre:"))
    b=float(input("Segon nombre:"))

    print(int(a+b))


#Training 3 Exercici 1

def edat():
    edat=int(input("Introdueix la teva edat:"))
    if edat>=18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")



#Training 3 Exercici 2


def NombreMajor():
    num1=float(input("Primer nombre:"))
    num2=float(input("Segon nombre:"))
    if num1>num2:
        print(f"El nombre major és: {num1}")
    elif num2>num1:
        print(f"El nombre major és: {num2}")
    else:
        print("Els dos nombres són iguals")


#Training 3 Exercici 3


def PositiuNegatiu():
    num=float(input("Introdueix un nombre:"))
    if num>=0:
        print("El nombre és positiu")
    else:
        print("El nombre és negatiu")


#Training 4 Exercici 1 


def Bucles():
    for i in range(1,201):
        if i % 2 == 0:
            print(i)


#Training 4 Exercici 2


def HiHaUn10():
    te_un_10 = False

    while True:
        nota=float(input("Introdueix una nota entre 0 i 10: "))
        
        if nota < 0 or nota > 10:   
            print("Nota invàlida. Torna-ho a intentar.")
            continue
        if nota == 10:
            te_un_10 = True
            break  

    if te_un_10:
        print("Hi ha algun 10")
    else:
        print("No hi ha cap 10")



#Training 4 Exercici 3


def PositiuNegatiu():
    negatiu=False
    for i in range (10):
        num=float(input("Introdueix un nombre:"))
        if num<0:
            negatiu=True



#Menu 

def menu():
    print("Menu")
    print("1.Calcul de l'àrea d'un cuadrat")
    print("2.Operacions")
    print("3.Frases")
    print("4.Casting")
    print("5.Edat")
    print("6.Nombre Major")
    print("7.Positiu i Negatiu")
    print("8.Sortir")

if __name__ == "__main__":
    while True:
        menu()
        opcio = input("Tria una opcio (1-8): ")
        
        if opcio == "1":
            calcul_area()
        elif opcio == "2":
            operacions()
        elif opcio == "3":
            frases()
        elif opcio == "4":
            casting()
        elif opcio == "5":
            edat()
        elif opcio == "6":
            NombreMajor()   
        elif opcio == "7":
            PositiuNegatiu()
        
        elif opcio == "8":
            print("Sortint del programa...")
            break





          









