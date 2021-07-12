""" Programa lineas de metro
    Programa para el manejo de conexiones entre estaciones de metro
    incorpora al modulo rostros.py
    Oscar Estrada Suazo
    Junio 2-2021 """

#---------------- Zona librerias------------
from colorama import Fore
import metro as mt

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def capturar_estacion():

    estacion = int(input("\nIngrese la estación donde se encuentra:"))

    return estacion

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
print(Fore.LIGHTWHITE_EX, "-----------------------------------------")
print(Fore.LIGHTWHITE_EX, "PROGRAMA DE ESTACIONES")
print(Fore.LIGHTWHITE_EX, "-----------------------------------------")

matriz_conexiones = mt.leer_conexiones(mt.leer_numero_estaciones())
print(Fore.LIGHTWHITE_EX, "-----------------------------------------")
numero_estacion = capturar_estacion()
lista_conexion_estacion = mt.obtener_lista_conexiones_estacion(matriz_conexiones, numero_estacion)
print(Fore.LIGHTMAGENTA_EX, "Lista de estaciones con conexion estacion", numero_estacion)
print ("\n{:<15} {:<20}".format('Estación','Estación conexión'))
print("----------------------------------------------")
for x in lista_conexion_estacion:
  print ("{:<15} {:<20}".format(numero_estacion, x))

print(Fore.LIGHTGREEN_EX, "\n La estación con mas conexiones es:", mt.obtener_estacion_mas_conectada(matriz_conexiones))