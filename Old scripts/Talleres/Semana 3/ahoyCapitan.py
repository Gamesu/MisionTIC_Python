""" Programa para apoyar al marinero Seijo
    Oscar Estrada Suazo
    Mayo 20 - 2021 """

import utilidades as util
from colorama import Fore

def probar_funciones():
  criatura= util.aparecer_criatura()
  direccion=util.aparecer_direccion()
  return criatura, direccion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

def validar_cantidad(criatura):
    ultimaLetra = len(criatura) - 1
    criatura = criatura[ultimaLetra -1: len(criatura)]
    if criatura == "as":
        return 1
    else:
        if criatura == "es":
            return 2
        else:
            if criatura == "as":
                return 3
            else:
                return 4

def mensaje_capitan(cantidad, direccion, criatura):
    if cantidad == 1:
        if direccion == "babor" or direccion == "estribor":
            mensaje =  "Ahoy! capitán, unas " + criatura + " a " + direccion
        else:
            mensaje =  "Ahoy! capitán, unas " +  criatura + " por la " + direccion
    else:
        if cantidad == 2:
            if direccion == "babor" or direccion == "estribor":
                mensaje =  "Ahoy! capitán, unos " + criatura + " a " + direccion
            else:
                mensaje =  "Ahoy! capitán, unos " + criatura + " por la " + direccion
        else:
            if cantidad == 3:
                if direccion == "babor" or direccion == "estribor":
                    mensaje =  "Ahoy! capitán, una " + criatura + ' a ' + direccion
                else:
                    mensaje =  "Ahoy! capitán, una " + criatura + " por la " + direccion
            else:
                if direccion == "babor" or direccion == "estribor":
                    mensaje =  "Ahoy! capitán, un " + criatura + " a " + direccion
                else:
                    mensaje =  "Ahoy! capitán, un " + criatura + " por la " + direccion
    
    return mensaje

# Ejecuta el programa varias veces para ver su funcionamiento

criatura, direccion = probar_funciones()
cantidad = validar_cantidad(criatura)
mensaje = mensaje_capitan(cantidad, direccion, criatura)
print(Fore.LIGHTCYAN_EX, mensaje)
    

