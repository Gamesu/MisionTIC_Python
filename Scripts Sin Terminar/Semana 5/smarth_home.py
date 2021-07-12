""" Modulo para el manejo de datos de dispositivos IoT 
    Oscar Franco-Bedoya
    Mayo 20-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
import collections as colle

#----------Definición de Funciones (Dividir)------------

def separar_cadenas(lista_datos):
  lista_IoT = []
  lista_dispositivosIoT = lista_datos.split("@")
  DispositivoIoT = colle.namedtuple('DispositivoIoT', 'tipo identificador estado')

  # -- Crea un ciclo para separar datos y crear la tupla con nombres --
  for x in range (0, len(lista_dispositivosIoT)):
    lista_datosIoT = lista_dispositivosIoT[x].split(",")
    datos_IoT = DispositivoIoT(tipo=lista_datosIoT[0], identificador=lista_datosIoT[1], estado=lista_datosIoT[2])
    lista_IoT.insert(x, datos_IoT)
  
  return lista_IoT


def calcular_estadisticas(lista_IoT):
  lista_IoTON = []
  lista_IoTOFF = []

  for x in range (0, len(lista_IoT)):
    if lista_IoT[x].estado == "ON":
        lista_IoTON.insert(x, lista_IoT[x])
    else:
        lista_IoTOFF.insert(x, lista_IoT[x])

  return lista_IoTON, lista_IoTOFF