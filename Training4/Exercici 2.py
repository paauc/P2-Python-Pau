te_un_10 = False

while True:
    nota=float(input("Introdueix una nota entre 0 i 10: "))
    
    if nota < 0 or nota > 10:   
        print("Nota invàlida. Torna-ho a intentar.")
        continue
    if nota == 10:
        te_un_10 = True
        

if 10:
    print("Hi ha algun 10")
else:
    print("No hi ha cap 10")