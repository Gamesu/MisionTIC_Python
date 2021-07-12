""" Programa rostros#
    Programa para el manejo de rostros codificados 
    incorpora al modulo rostros.py
    Oscar Estrada Suazo
    Junio 9-2021 """

#---------------- Zona librerias------------
import rostros as rt

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

archivo = "rostros.txt"
#print(rt.cargar_rostros(archivo))
ndia = int(input("Ingrese el numero del NDIA:"))
rt.calcular_estadisticas(rt.cargar_rostros(archivo), ndia)
