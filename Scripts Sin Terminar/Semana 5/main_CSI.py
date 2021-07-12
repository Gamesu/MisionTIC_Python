""" Programa Saltando al 5
    Realiza codificación y decodificación 
    de mensajes
    incorpora al modulo csi.py
    Oscar Estrada Suazo
    Junio 02-2021 """

#---------------- Zona librerias------------
from colorama import Fore
import csi as sh


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def mostrar_menu():
    print("===========================================================")    
    print("BIENVENIDO AL SISTEMA DE CIFRADO DE MENSAJES")
    print("===========================================================")    
    print(Fore.LIGHTCYAN_EX, "1. Codificar un mensaje")
    print(Fore.LIGHTCYAN_EX, "2. Descodificar un mensaje")
    print("===========================================================")
    opcion = int(input("Por favor digite al opción del menu:"))
    #opcion = 1

    if opcion <= 2 and opcion >= 0:
        return opcion 
    else:
        return 0
    

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================}
opcion = int(mostrar_menu())
#mensaje_original = "Llamar después de las 12:15 al teléfono 1-800-329-8044"

if opcion == 1:
    print(Fore.LIGHTWHITE_EX, "")
    mensaje_original = input("Ingrese el mensaje de que desea codificar:")
    print("===========================================================")
    print(Fore.LIGHTGREEN_EX, "\n Mensaje CODIFICADO:", sh.codificar_mensaje(mensaje_original))
elif opcion == 2:
    print(Fore.LIGHTWHITE_EX, "")
    mensaje_codificado = input("Ingrese el mensaje de que desea decodificar:")
    print("===========================================================")
    print(Fore.LIGHTGREEN_EX, "\n Mensaje DECODIFICADO:", sh.decodificar_mensaje(mensaje_codificado))
else:
    print(Fore.LIGHTRED_EX, "\n ¡OPCION INCORRECTA DEBE UNA OPCION DEL MENU!")

print(Fore.LIGHTMAGENTA_EX, "\n ありがとうございました。") 