#Demana 10 nombres i indica si hi ha algun nombre negatiu
negatiu = False
for i in range(10):
    nombre = float(input("Introdueix un nombre: "))
    if nombre < 0:
        negatiu = True
        break

if negatiu:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")


