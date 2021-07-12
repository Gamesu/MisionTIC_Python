""" Programa ventas 
    Programa para el manejo de ventas por mes
    incorpora al modulo ventas.py
    Oscar Estrada Suazo
    Junio 9-2021 """

#---------------- Zona librerias------------
import numpy as np
import ventas as vt

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def cantidad_empleados():
    empleados = int(input("Ingrese la cantidad de empleados:"))
    return empleados

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

plantilla = np.zeros((cantidad_empleados(),12))
#print(plantilla)
lista_empleados = vt.leer_numero_empleados()
#print(lista_empleados) # 1651,6548,96184,02386,16898,164866
plantilla = vt.leer_ventas_empleados_mes(plantilla, lista_empleados)
print(plantilla) # 23,46,159,23,86,78,105,46,12,16,159,222
ventasTotales = vt.ordenar_vendedores_por_ventas(plantilla, lista_empleados)
print(ventasTotales)