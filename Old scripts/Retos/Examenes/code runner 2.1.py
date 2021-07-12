import math
def calcular_longitud_polea(diametro):
 #TODO: 
  # Formula de pitagoras --> C = dπ
  # Formula aplicada longitudPolea --> C = polea * π

  longitudPolea = (float(diametro * math.pi))
  longitudPolea = "{0:.3f}".format(longitudPolea)

  return longitudPolea

print(calcular_longitud_polea(120))
print(calcular_longitud_polea(100))
print(calcular_longitud_polea(145))