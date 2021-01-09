import os

def menu(): 
    
    print ("Selecciona una opción")
    print ("\t1 - Estreno ($4.200)")
    print ("\t2 - 3D ($5.500)")
    print ("\t3 - Documentales ($1.800)")    
    print ("\t4 - salir")

def pelicula(cantidad, valor, tipo):
    print(f"Pelicula de tipo {tipo} -- {cantidad} Entradas -- Total a cancelar: $", round(valor *cantidad))	
    pagado=int(input("Con cuanto desea pagar? : ") )
    print("Su vuelto es: ", pagado -(round(valor *cantidad)))  		        
    input("\npulsa una tecla para continuar")
    return

def menuDia():
    print ("Selecciona día de Funcion")
    print ("\t1 - Lunes")
    print ("\t2 - Martes")
    print ("\t3 - Miercoles")    
    print ("\t4 - Jueves")
    print ("\t5 - Viernes")
    print ("\t6 - Sabado")
    print ("\t7 - Domingo")    

while True:
    os.system ("cls")  
    menu()
    opcionMenu = input("inserta un numero valor >> ")
    dscto_adicional=0
    dscto_dia=0
    
    if opcionMenu == "1":
        menuDia()
        dia_funcion = input("Ingrese el n° correspondiente al día >> ")
        print ("Ingrese cantidad de entradas")
        cantidad=int(input(": "))
        pelicula(cantidad, 4200, tipo="Estreno")
        
    elif opcionMenu == "2":
        menuDia()
        dia_funcion = input("Ingrese el n° correspondiente al día >> ")
        if dia_funcion=="3":
            dscto_adicional = 5500*0.2
            dscto_dia = 5500*0.55
            
        print ("Ingrese cantidad de entradas")
        cantidad=int(input(": "))
        valor=5500-dscto_adicional-dscto_dia  
        pelicula(cantidad, valor, tipo="3D")
        
    elif opcionMenu == "3":
        menuDia()
        dia_funcion = input("Ingrese el n° correspondiente al día >> ")
        if dia_funcion=="1":
            dscto_adicional = 1800*0.1
            dscto_dia = 1800*0.3
        elif dia_funcion=="2":
            dscto_dia = 1800*0.4
        elif dia_funcion=="3" :
            dscto_dia = 1800*0.55
            
        print ("Ingrese cantidad de entradas")
        cantidad=int(input(": "))
        valor=1800-dscto_adicional-dscto_dia        
        pelicula(cantidad, valor, tipo="Documentales")
            
    elif opcionMenu == "4":
        print("Hasta pronto!!")
        break
    else:
        print ("")
        input("No ha pulsado una opcion válida\npulsa una tecla para continuar")
        

    
