""" Reto # 2 Protegiendo al castillo medieval
    Oscar Estrada Suazo
    Mayo 17-21 """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
import math
def calcular_longitud_cuerda(puerta,muro):
  #TODO: Se usa el teorema de pitágoras para calcular la longitud de la cuerda
  # Formula de pitagoras --> x² = a² + b² 
  # Formula aplicada longitudCuerda² = puerta² + muro²
  
  puerta =  puerta**2
  muro = muro**2
  longitudCuerda = float(math.sqrt(puerta + muro))

  return longitudCuerda
#-------------------------------------------
def calcular_longitud_polea(polea):
 #TODO: 
  # Formula de pitagoras --> C = dπ
  # Formula aplicada longitudPolea --> C = polea * π

  longitudPolea = (float(polea * math.pi)) / 100

  return longitudPolea
#-------------------------------------------
def calcular_numero_vueltas_polea(lcuerda,lpolea):
  #TODO: comentarios
  # Formula de matematica --> V = X² / C
  # Formula aplicada cantidad de vueltas --> numeroVueltas = longitudCuerda / longitudPolea

  numeroVueltas = lcuerda / lpolea

  return numeroVueltas
#-------------------------------------------
def calcular_numero_chewbaccas(num_vueltas):
  #TODO: comentarios
  # Formula de matematica --> V = X² / C
  # Formula aplicada cantidad de Chewbaccas --> Chew = canitidadVueltas / 3

  maxVueltasChewbacca = 3
  cantidadChewbaccas = num_vueltas / maxVueltasChewbacca

  return cantidadChewbaccas
#-------------------------------------------
def calcular_velocidad_giro(longitudCuerda,tiempoMaximo):
  #TODO: comentarios
  # # Formula de matematica --> V = longitudCuerda / tiempo
  
  #Convertir medida de cuerda a centimetros
  longitudCuerda = longitud_cuerda * 100

  #Calcular la velocidad
  velocidadGiros = longitudCuerda / tiempoMaximo

  return velocidadGiros

#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
#lectura longitud de la puerta
#TODO: instrucciones
print(" _____  _   _  _____ _    _______  ___  _____  _____   ___  ")
print("/  __ \| | | ||  ___| |  | | ___ \/ _ \/  __ \/  __ \ / _ \ ")
print("| /  \/| |_| || |__ | |  | | |_/ / /_\ \ /  \/| /  \// /_\ \ ")
print("| |    |  _  ||  __|| |/\| | ___ \  _  | |    | |    |  _  |")
print("| \__/\| | | || |___\  /\  / |_/ / | | | \__/\| \__/\| | | |")
print(" \____/\_| |_/\____/ \/  \/\____/\_| |_/\____/ \____/\_| |_/")

print("---------------------------------------------------------------")                                                                                                                     

print("---------------------------------------------------------------")
print("--     CAPTURA DE DATOS PARA CALCULAR PROBLEMA               --")
print("---------------------------------------------------------------")
#lectura de captura de valores
puerta = int(input("Ingrese el tamaño de la puerta en metros (mts):"))
muro = int(input("Ingrese el tamaño del muro en metros (mts):"))
polea = int(input("Ingrese el diámetro de la polea en centímetros (cms):"))
tiempo = int(input("Ingrese el tiempo máximo para cerrar la puerta en minutos (min):"))


longitud_cuerda=calcular_longitud_cuerda(puerta,muro)
longitud_polea=calcular_longitud_polea(polea)
numero_vueltas=calcular_numero_vueltas_polea(longitud_cuerda,longitud_polea)
numero_chewbaccas=calcular_numero_chewbaccas(numero_vueltas)
velocidad_giro=calcular_velocidad_giro(longitud_cuerda, tiempo)
print("---------------------------------------------------------------")
print("--                         RESULTADOS                        --")
print("---------------------------------------------------------------")
#Imprimir en pantalla los valores solicitados en el problema 
#print("cuerda", longitud_cuerda)
#print("polea", longitud_polea)
print(" 1. Total de vueltas para cerrar la puerta: ", numero_vueltas, "vueltas")
print(" 2. Total de chewbaccas para cerrar la puerta: ", numero_chewbaccas, "Chewbaccas")
print(" 3. Velocidad para cerrar la puerta en un máximo de minutos: ", velocidad_giro, "(cms/seg)")

