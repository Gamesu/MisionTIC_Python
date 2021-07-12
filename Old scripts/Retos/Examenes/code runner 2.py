import math as math
def calcular_longitud_cuerda(lpuerta,lmuro):
  #TODO: Se usa el teorema de pitágoras para calcular la longitud de la cuerda
  # Formula de pitagoras --> x² = a² + b² 
  # Formula aplicada longitudCuerda² = puerta² + muro²
  
  lpuerta =  lpuerta**2
  lmuro = lmuro**2
  #longitudCuerda = float((puerta + muro) ** (0.5)) * 100
  longitudCuerda = float(math.sqrt(lpuerta + lmuro)) * 100
  longitudCuerda = "{0:.3f}".format(longitudCuerda)

  return longitudCuerda

print(calcular_longitud_cuerda(25, 25))
print(calcular_longitud_cuerda(30,30))
print(calcular_longitud_cuerda(38,38))