""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Oscar Estrada Suazo
    Mayo 20-2021 """

#---------------- Zona librerias------------
import multas as mult
from colorama import Fore

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def capturar_datos():
    distancia1 = float(input("Ingrese el valor de la distancia 1 en KM: "))
    distancia2 = float(input("Ingrese el valor de la distancia 2 en KM: "))
    tiempo = float(input("Ingrese el lapso del tiempo en segundos: "))

    if distancia1 < 0 or distancia2 < 0 or tiempo <= 0:
        distancia1 = float(input(Fore.LIGHTMAGENTA_EX, "Se ha digitado algún valor incorrecto"))
    else:
        return distancia1, distancia2, tiempo

def convertir_seg_hrs(tiempo):
    # convierte segundos a horas
    tiempo = tiempo / 3600
    return tiempo

def calcular_velocidad(distancia1, distancia2, tiempo):
    #Calcula la espacio entre las dos distancias
    espacio = distancia1 - distancia2
    velocidad = espacio / tiempo
    return velocidad

# =======================================================================================
print(Fore.LIGHTCYAN_EX, "==============================================================")
print(Fore.LIGHTCYAN_EX, "=========         BIENVENIDO A SISTEMA DE MULTAS         =====")
print(Fore.LIGHTCYAN_EX, "==============================================================")

distancia1, distancia2, tiempo = capturar_datos()
tiempo = convertir_seg_hrs(tiempo)
velocidad = calcular_velocidad(distancia1, distancia2, tiempo)
multa, pruebaAlcoholemia = mult.multar_velocidad(velocidad)
if pruebaAlcoholemia == True:
    gradoAlcohol = float(input("Ingrese el grado de alcohol del conductor: "))
    multaAdicional = mult.multar_alcoholemia(gradoAlcohol)
    print(Fore.LIGHTRED_EX, multa)
    print(Fore.LIGHTRED_EX, multaAdicional)
else:
    print(Fore.LIGHTCYAN_EX, multa)

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
