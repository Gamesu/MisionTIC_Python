""" Reto # 6 Clasificación y organización de sustancias químicas inorgánicas del anaquel del laboratorio de química - Parte IV
    Oscar Estrada Suazo
    Mayo xx-XX """
    
# importar módulos diseñados por el alumno (Dividir)
#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================
# LIBRERIAS A INSTALAR
# 1. pip install numpy
# 2. pip install pandas
from colorama import Fore
import menu as mn
import tipo_compuesto as tc
import clasificar_compuesto as cc
import pandas as pd 

def mensaje_salir():
    print(Fore.LIGHTWHITE_EX, "===============================================================")
    print(Fore.LIGHTWHITE_EX, "Fin de la simulacion, ¡Hasta una proxima ocasión!, ありがとうございました。")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
opcion = mn.menu_opciones()
if opcion == 1:
    compuestos = pd.read_csv("data/compuestos.csv", sep = ';', index_col=0, encoding='iso-8859-1')
    #compuestos = pd.read_csv("data/compuestos.csv", sep = ';', index_col=0, encoding='utf-8')
    print(Fore.LIGHTCYAN_EX, compuestos)
elif opcion == 2:
    compuestos = pd.read_csv("data/compuestos.csv", sep = ';', index_col=0, encoding='iso-8859-1')
    cc.clasificar_compuesto(compuestos)
elif opcion == 3:
    print("3")
else:
    print(Fore.LIGHTYELLOW_EX, "Saliendo del programa")

mensaje_salir()
