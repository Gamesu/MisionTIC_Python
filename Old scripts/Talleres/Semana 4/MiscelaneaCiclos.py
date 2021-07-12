# Oscar Estrada
# 25/05/2021
from colorama import Fore
import funciones_ciclos as funci
#===========================================================
# Ejercicio Menú
#===========================================================
def mostrar_menu():  
    print("===========================================================")    
    print(Fore.LIGHTYELLOW_EX, "1. Simulador de caida")
    print(Fore.LIGHTYELLOW_EX, "2. Simulador de generaciones")
    print(Fore.LIGHTYELLOW_EX, "3. Simulador de triangulares")
    print(Fore.LIGHTYELLOW_EX, "4. Diseñador de tableros")
    print("===========================================================")
    opcion = int(input("Por favor digite al opción del menu:"))
    #opcion = 4

    return opcion

def simulador(opcion):
    if opcion == 1:
        #===========================================================
        # Ejercicio 1
        #===========================================================
        print(Fore.LIGHTGREEN_EX, "Ejercicio 1 // Y sin embargo se mueve")
        print("-------------------------------------------------------------")
        altura = int(input("Por favor registre la altura en metros del edificio: "))
        print(funci.simulador_caida_libre(altura))
        print("-------------------------------------------------------------")
    else:
        if opcion == 2:
            #===========================================================
            # Ejercicio 2
            #===========================================================
            print(Fore.LIGHTCYAN_EX, "Ejercicio 2 // Descendientes")
            print("-------------------------------------------------------------")
            generacion = int(input("Por favor registre la generación que desea calcular: "))
            #generacion = int(3)
            print("Total de personas en la familia:", funci.generador_generaciones(generacion))
            print("-------------------------------------------------------------")
        else:
            if opcion == 3:
                #===========================================================
                # Ejercicio 3
                #===========================================================
                print(Fore.LIGHTMAGENTA_EX, "Ejercicio 3 // Triangulares")
                print("-------------------------------------------------------------")
                pisos = int(input("Por favor registre la cantidad de pisos que desea pintar: "))
                #generacion = int(3)
                mensaje = funci.constructor_triangulos(pisos)
                print("")
                print(Fore.LIGHTGREEN_EX, mensaje)
                print("-------------------------------------------------------------")
            else:
                if opcion == 4:
                    #===========================================================
                    # Ejercicio 4
                    #===========================================================
                    print(Fore.LIGHTWHITE_EX, "Ejercicio 4 // Tableros")
                    print("-------------------------------------------------------------")
                    dimension = input("Por favor registre la longitud del tablero a pintar: ")
                    #dimension = "2x2"
                    dimension = funci.constructor_tableros(dimension)
                    print("")
                    print(Fore.LIGHTGREEN_EX, dimension)
                    print("-------------------------------------------------------------")
                else:
                    print(Fore.LIGHTRED_EX, "Opcion invalida, por seleccione una opción valida")

    return "FIN DEL PROGRAMA"

#===========================================================
# Inicio del programa
#===========================================================
simulador(mostrar_menu())


