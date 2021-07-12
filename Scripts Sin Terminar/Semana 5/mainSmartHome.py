""" Programa IoT#
    Realiza lel calculo de estadisticas de Una 
    Smarth Home
    incorpora al modulo smarth_home.py
    Oscar Estrada Suazo
    Junio 1-2021 """

#---------------- Zona librerias------------
from colorama import Fore
import smarth_home as sh

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def imprimir_resultado(lista_IoTON, lista_IoTOFF):
  
    print(Fore.LIGHTCYAN_EX, "\n DISPOSITIVOS ENCENDIDOS:", len(lista_IoTON))
    for x in lista_IoTON:
        print("Tipo dispositivo: {} // Dispositivo IoT: {}".format(*x))

    print(Fore.LIGHTGREEN_EX, "\n DISPOSITIVOS APAGADOS:", len(lista_IoTOFF))
    for x in lista_IoTOFF:
        print("Tipo dispositivo: {} // Dispositivo IoT: {}".format(*x))

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
print("---------------------------------------------------------------")
print("                   INICIO DE PROGRAMA")
print("---------------------------------------------------------------")

lista_datos = input("Ingrese la cadena de dispositivos IoT:")
#lista_datos = "sensor,humedad,ON@electricos,luces,OFF@alarma,movimiento,OFF"
lista_IoT = sh.separar_cadenas(lista_datos)
lista_IoTON, lista_IoTOFF = sh.calcular_estadisticas(lista_IoT)


print("---------------------------------------------------------------")
print("                   REPORTES DE DISPOSITIVOS")
print("---------------------------------------------------------------") 

imprimir_resultado(lista_IoTON, lista_IoTOFF)

print("---------------------------------------------------------------")
