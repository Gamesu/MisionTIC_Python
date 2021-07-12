# Oscar Estrada
# 25/05/2021
from colorama import Fore
import funciones_listas as funci
#===========================================================
# Ejercicio Menú
#===========================================================
def mostrar_menu():  
    print("===========================================================")    
    print(Fore.LIGHTYELLOW_EX, "1. Suma acumulada")
    print(Fore.LIGHTYELLOW_EX, "2. Traductor")
    print(Fore.LIGHTYELLOW_EX, "3. Vitamina A")
    #print(Fore.LIGHTYELLOW_EX, "4. Diseñador de tableros")
    print("===========================================================")
    opcion = int(input("Por favor digite al opción del menu:"))
    #opcion = 3

    return opcion

def simuladorListas(opcion):
    if opcion == 1:
        #===========================================================
        # Ejercicio 1
        #===========================================================
        print(Fore.LIGHTGREEN_EX, "Ejercicio 1")
        print("-------------------------------------------------------------")
        #altura = int(input("Por favor registre la altura en metros del edificio: "))
        lista = [4, 3, 6, 10]
        #print(funci.suma_acumulativa(lista))
        print("Lista_acumuladas=", funci.suma_acumulativa(lista))
        print("-------------------------------------------------------------")
    else:
        if opcion == 2:
            #===========================================================
            # Ejercicio 2
            #===========================================================
            print(Fore.LIGHTCYAN_EX, "Ejercicio 2")
            print("-------------------------------------------------------------")
            palabra = input("Por favor ingrese la palabra a traducir: ")
            #palabra = palabra.lower()
            print(funci.traductor_pig_latin(palabra))
            print("-------------------------------------------------------------")
        else:
            if opcion == 3:
                #===========================================================
                # Ejercicio 3
                #===========================================================
                print(Fore.LIGHTMAGENTA_EX, "Ejercicio 3")
                print("-------------------------------------------------------------")
                #lista_frutas = input("Por favor registre la lista de frutas: ")
                lista_frutas = ["Pera", "Mango", "lUlo", "KiWi", "PapaYa"]
                lista_frutas = funci.identificador_frutas(lista_frutas)
                print("")
                print(Fore.LIGHTGREEN_EX, "Las frutas con vitamina A son:", lista_frutas)
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
simuladorListas(mostrar_menu())


