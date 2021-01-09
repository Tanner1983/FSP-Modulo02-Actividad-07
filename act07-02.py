
opcion = ""

while opcion != "0":

    print("************ Servicio de estacionamiento ***********")
    print("[1] Minutos y total a pagar")
    print("[0] Salir")

    opcion = input("Ingrese su opcion: ")

    if opcion == "1":
       minutos=int(input("Ingrese cantidad de minutos\n: "))
       if minutos <=30:
           valor_pagar=600
           print("El valor a pagar es: ", valor_pagar)
           break
       else:
            valor_pagar=((minutos-30)*25)+600
            print("El valor a pagar es: ", valor_pagar)
            break
    elif int(opcion) > 1 or int(opcion) < 0:
        print("opcion no válida")
