""" Modulo para la codificación y decodificación de
    mensajes con la técnica saltando al 5
    Oscar Estrada Suazo
    Junio 02-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def codificar_mensaje(mensaje_original):
  dic_Codificado = {"1": 9, "2":8, "3":7, "4":6, "5":0, "6":4, "9":1, "8":2, "7":3, "0":5}
  mensaje_codificado = ""

  for x in range(0, len(mensaje_original)):
      if str.isdigit(mensaje_original[x]) == True:
        mensaje_codificado = mensaje_codificado + str(dic_Codificado[mensaje_original[x]])
      else:
        mensaje_codificado = mensaje_codificado + str(mensaje_original[x])

  return mensaje_codificado

def decodificar_mensaje(mensaje_codificado):
  dic_Descodificado = {"9": 1, "8":2, "7":3, "6":4, "0":5, "4":6, "1":9, "2":8, "3":7, "5":0} 
  mensaje_decodificado = ""

  for x in range(0, len(mensaje_codificado)):
      if str.isdigit(mensaje_codificado[x]) == True:
        mensaje_decodificado = mensaje_decodificado + str(dic_Descodificado[mensaje_codificado[x]])
      else:
        mensaje_decodificado = mensaje_decodificado + str(mensaje_codificado[x])

  return mensaje_decodificado

