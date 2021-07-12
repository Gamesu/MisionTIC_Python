""" Taller 2.3 Distancia mas corta #
    Oscar Estrada Suazo
    Mayo 18-21 """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
def calcular_distancia_c1_a1(xc1,yc1,xa1,ya1):
  #TODO: comentarios
  #TODO: instrucciones
  #Calcular distancia = √(Cx-Ax)^2+(Cy-Ay)^2
  distanciaC1A1 = (((xc1 - xa1)**2) + ((yc1 - ya1)**2) ** (0.5))

  return distanciaC1A1
#-------------------------------------------
def calcular_distancia_a1_ch(xa1,ya1,xch,ych):
  #TODO: comentarios
  #TODO: instrucciones
  #Calcular distancia = √(CHx-Ax)^2+(CHy-Ay)^2
  distanciaA1CH = (((xch - xa1)**2) + ((ych - ya1)**2) ** (0.5))

  return distanciaA1CH
#-------------------------------------------
def calcular_distancia_ch_a2(xch,ych,xa2,ya2):
  #TODO: comentarios
  #TODO: instrucciones
  #Calcular distancia = √(CHx-Ax)^2+(CHy-Ay)^2
  distanciaCHA2 = (((xch - xa2)**2) + ((ych - ya2)**2) ** (0.5))

  return distanciaCHA2
#-------------------------------------------
def calcular_distancia_a2_c2(xa2,ya2,xc2,yc2):
  #TODO: comentarios
  #TODO: instrucciones
  #Calcular distancia = √(Cx-Ax)^2+(Cy-Ay)^2
  distanciaA2C2 = (((xc2 - xa2)**2) + ((yc2 - ya2)**2) ** (0.5))

  return distanciaA2C2
#-------------------------------------------
def obtener_distancia_total (d1,d2,d3,d4):
  #TODO: comentarios
  #TODO: instrucciones
  #Calcular distancia total = suma de todas las distancias
  diastanciaTotal = d1 + d2 + d3 + d4
  
  return diastanciaTotal

#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================
print(" _____ ______  _____ ")
print("|  __ \| ___ \/  ___|")
print("| |  \/| |_/ /\ `--. ")
print("| | __ |  __/  `--. \\")
print("| |_\ \| |    /\__/ /")
print(" \____/\_|    \____/ ")

print("---------------------------------------------------------------")                                                                                                                     

print("---------------------------------------------------------------")
print("--     CAPTURA DE DATOS PARA CALCULAR PROBLEMA               --")
print("---------------------------------------------------------------")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
#lectura coordenadas celular 1
#TODO: instrucciones
xc1 = float(input("Ingrese la coordenada del celular 1 en x:"))
yc1 = float(input("Ingrese la coordenada del celular 1 en y:"))

#lectura coordenadas antena 1
#TODO: instrucciones
xa1 = float(input("Ingrese la coordenada de la antena 1 en x:"))
ya1 = float(input("Ingrese la coordenada de la antena 1 en y:"))

#lectura coordenadas central holi 
#TODO: instrucciones
xch = float(input("Ingrese la coordenada de la central en x:"))
ych = float(input("Ingrese la coordenada de la central en y:"))

#lectura coordenadas antena 2
#TODO: instrucciones
xa2 = float(input("Ingrese la coordenada de la antena 2 en x:"))
ya2 = float(input("Ingrese la coordenada de la antena 2 en y:"))

#lectura coordenadas celular 2
#TODO: una vez haga os puntos anteriores quite el simbolo de comentarios
# y organice la identación
xc2 = float(input("Ingrese la coordenada del celular 1 en x:"))
yc2 = float(input("Ingrese la coordenada del celular 1 en y:"))

d1=calcular_distancia_c1_a1(xc1,yc1,xa1,ya1)
d2=calcular_distancia_a1_ch(xa1,ya1,xch,ych)
d3=calcular_distancia_ch_a2(xch,ych,xa2,ya2)
d4=calcular_distancia_a2_c2(xa2,ya2,xc2,yc2)
distancia_total=obtener_distancia_total (d1,d2,d3,d4)

print("---------------------------------------------------------------")
print("--                         RESULTADOS                        --")
print("---------------------------------------------------------------")

print("R1. La distancia total entre el celular 1 y la antena 1 es:",d1)
print("R2. La distancia total entre la antena 1 y la central holl es:",d2)
print("R3. La distancia total entre la central holl y la antena 2 es:",d3)
print("R4. La distancia total entre la antena 2 y el celular 2 es:",d4)
print("R5. La distancia total es:",distancia_total)


