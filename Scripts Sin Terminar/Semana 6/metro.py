""" Modulo ModuleNotFoundError
    Funciones para el manejo de las lineas de metro
    con matrices
    Oscar Estrada Suazo
    Junio 7-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
import numpy as np
from numpy.lib.function_base import insert

def leer_numero_estaciones():
  cantidad_estaciones = int(input("Ingrese la cantidad de estaciones:"))
  #cantidad_estaciones = 2
  matriz_estaciones = []
    
    # --- Se llena la matriz principal con los valores de las estaciones
  for i in range(0, cantidad_estaciones):
    lista_estaciones = []
    for j in range(0, cantidad_estaciones):
      # --- Valida si es la misma estacion para omitir pregunta
      if i != j:
        print("Estaciones:", [i+1 , j+1], "¿tienen conexión?")
        #print("Estaciones:", [i , j], "¿tienen conexión?")
        conexionEstacion = input("Por favor ingrese T (si tiene) o F (No tiene): ")
        lista_estaciones.insert(j, conexionEstacion)
      else:
        lista_estaciones.insert(j, "T")
    matriz_estaciones.insert(i, lista_estaciones)
  
  #print(matriz_estaciones)
  return matriz_estaciones 

def leer_conexiones(numero_estaciones):
  matriz_conexiones = []

  for i in range(0, len(numero_estaciones)):
    lista_conexiones = []
    for j in range(0, len(numero_estaciones)):
      #print(numero_estaciones[i][j])
      if numero_estaciones[i][j] == "T":
        #print(j + 1)
        lista_conexiones.insert(j, j + 1)
    matriz_conexiones.insert(i, lista_conexiones)
  
  #print(matriz_conexiones)
  return matriz_conexiones

def obtener_lista_conexiones_estacion(matriz_conexiones,numero_estacion):
  lista_conexion_estacion = matriz_conexiones[numero_estacion - 1]

  return lista_conexion_estacion

def obtener_estacion_mas_conectada(matriz_conexiones):
  mayor_conexiones = 0
  lista_estaciones_conexiones = []

  for y in matriz_conexiones:
    if len(y) >= mayor_conexiones:
      mayor_conexiones = len(y)

  for x in range(0, len(matriz_conexiones)):
    if len(matriz_conexiones[x]) >= mayor_conexiones:
      lista_estaciones_conexiones.insert(x, x + 1)

  #print(lista_estaciones_conexiones)
  return lista_estaciones_conexiones
