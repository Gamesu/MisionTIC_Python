""" Modulo para el manejo de rostros de
    los habitantes del planeta ASCII
    Oscar Estrada Suazo
    Junio 8-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def cargar_rostros(archivo):
  archivo = open(archivo, 'r')
  matriz_rostros = []
  lista_alien = []

  for linea in archivo:
    linea = linea.splitlines()
    if linea[0] == "---":
      matriz_rostros.append(lista_alien)
      lista_alien = []
    else:
      lista_alien.append(linea[0])
  matriz_rostros.append(lista_alien)
  archivo.close()

  return matriz_rostros

def calcular_estadisticas(rostros, ndia):
  # [['10284567', '2\t ,1\t\\,5\t_,1\t/'], ['20284567', '2\t ,1\t\\,5\t_,1\t/']
  for x in range(0, len(rostros)):
    if ndia == int(rostros[x][0]):
      for y in range(1, len(rostros[x])):
        print('\n', rostros[x][y])
 
  #return rostros


"""
def cargar_rostros(archivo):
  archivoRostros = open(archivo, "r")
  lista_rotros = archivoRostros.readlines()
  matriz_rostros = []
  alien = []

  for x in range(len(lista_rotros)):
      if lista_rotros[x] == "---\n" or lista_rotros[x] == '':
          matriz_rostros.insert(0, alien)
          alien = []
      else:
          alien.insert(x, lista_rotros[x])

  matriz_rostros.insert(0, alien)
  
  return matriz_rostros
"""