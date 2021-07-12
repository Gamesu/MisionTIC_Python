""" Modulo Ciclos
    Funciones para practicas con ciclos
    Oscar Estrada Suazo
    Mayo 25-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def simulador_caida_libre(altura):
  # tiempo d= (1/2) g*t^2 --> d = (g*(t**2))/ 2
  GRAVEDAD = 9.8
  tiempo = 1

  while altura >= 0:
    distancia = round((GRAVEDAD * (tiempo**2)) / 2, 3)
    #distancia = "{0:.3f}".format(distancia)
    tiempo = tiempo + 1
    altura = altura - distancia
    if altura >= 0:
      print("La altura de caida es en", tiempo - 1, "segundos de ", altura, "metros")
    else:
      print("La altura de caida es en", tiempo - 1, "segundos de 0 metros")

  return "Fin de la simulación"

def generador_generaciones(generacion):
  xmen = 0
  personas = 1
  familia = 1

  while xmen < generacion:
    print("Total personas:", personas, "en la generación", xmen)
    personas = personas * 2
    familia = familia + personas
    xmen = xmen + 1        
  
  print("Total personas:", personas, "en la generación", xmen)
  return familia

def constructor_triangulos(pisos):
  if pisos <= 0:
    return "Debe ingresarse un numero mayor a cero"
  else:
    numPiso = 1
    filas = 1
    contador = 1
        
    while pisos >= numPiso:
      #print("piso", numPiso, "filas", numPiso)
      print("")
      while filas <= numPiso:
        print(contador, end=" ")
        contador = contador + 1
        filas = filas + 1
      numPiso = numPiso + 1
      filas = 1

  return "Fin de la simulación" 

def constructor_tableros(longitud):
  #epsBlancas = "   "
  epsBlancas = "^^^"
  epsNegras = "***"
  colorEspacio = True
  numEspacio = 0
  #validar_impar(longitud)

  if int(longitud[0]) <= 1:
    return "Debe ingresarse un numero mayor a uno"
  else:
    #valida la longitud del tablero a nivel de columnas
    for x in range(int(longitud[2])):
      #Imprime la linea del tablero
        numEspacio = 0
        while numEspacio < int(longitud[0]):
          #x = 0
          #Pinta los cuadros de acuerdo si son blancos o negros
          if colorEspacio == True:
            print(epsBlancas, end="")
            colorEspacio = False
          else:
            print(epsNegras, end="")
            colorEspacio = True
          numEspacio += 1
        print("")
        if validar_impar(longitud[0]) == 0:
          colorEspacio = False
        else:
          colorEspacio = False
  
  return "Fin de la simulación"

def validar_impar(longiud):
  longiud = int(longiud)
  esPar = longiud % 2
  return esPar

  """
        x = 0
      #Pinta los cuadros deacuerdo si son blancos o negros
      if colorEspacio == True:
        while x < 3:
          print(epsBlancas)
          colorEspacio = False
          x += 1
      else:
        while x < 3:
          print(epsNegras)
          colorEspacio = True
          x += 1
  """