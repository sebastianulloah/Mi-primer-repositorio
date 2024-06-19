num1 = int(input("numero 1: ")) 
num2 = int(input("numero 2: ")) 
num3 = int (input ("numero 3: "))
valor = 0
while True:
    print("""seleccione opcion
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- dividir 
            5.- sumar 3 valores
            6.- sumar 5 valores
        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        print("la suma es",num1+num2)
        break;
    if valor == 2:
        print("la resta es",num1-num2)
        break;
    if valor == 3:
        print("la multiplicacion es",num1*num2)
        break;
    if valor == 4:
        print("la division es",num1/num2)
        break;
    if valor == 5:
        print (f"La suma es {num1+num2+num3}")
    if valor == 6:
        print (f"La suma es {num1 + num2 + num3 + num1 + num2}")
    else:
        print("Opcion incorrecta")
        break;
