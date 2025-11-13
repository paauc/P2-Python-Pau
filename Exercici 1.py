def calcul_area(base, altura):
    area = base * altura
    print(f"\n=== CÀLCUL ÀREA ===")
    print(f"Base: {base}, Altura: {altura}")
    print(f"Àrea: {area}")
    return area


def calcul_edat(any_actual, any_naixement):
    edat = any_actual - any_naixement
    print(f"\n=== CÀLCUL EDAT ===")
    print(f"Edat: {edat} anys")
    return edat


def calculadora(num1, num2):
    print(f"\n=== CALCULADORA ===")
    print(f"Número 1: {num1}, Número 2: {num2}")
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicació: {num1 * num2}")
    if num2 != 0:
        print(f"Divisió: {num1 / num2}")
    else:
        print("Divisió: No es pot dividir per 0")


def parell_o_senar(num):
    print(f"\n=== PARELL O SENAR ===")
    print(f"Número: {num}")
    if num % 2 == 0:
        print("És PARELL")
        return "PARELL"
    else:
        print("És SENAR")
        return "SENAR"


# PROGRAMA PRINCIPAL
while True:
    print("\n" + "="*30)
    print("MENÚ")
    print("="*30)
    print("1. Càlcul Àrea")
    print("2. Càlcul Edat")
    print("3. Calculadora")
    print("4. Parell o Senar")
    print("S. Sortir")
    
    opcio = input("\nTria opció: ").upper()
    
    if opcio == '1':
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        calcul_area(base, altura)
        
    elif opcio == '2':
        any_actual = int(input("Any actual: "))
        any_naixement = int(input("Any naixement: "))
        calcul_edat(any_actual, any_naixement)
        
    elif opcio == '3':
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        calculadora(num1, num2)
        
    elif opcio == '4':
        num = int(input("Número: "))
        parell_o_senar(num)
        
    elif opcio == 'S':
        print("\nAdéu!")
        break
        
    else:
        print("\nOpció no vàlida!")