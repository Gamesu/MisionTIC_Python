import math as math
def calcular_longitud_cuerda(puerta,muro):
  #TODO: Se usa el teorema de pitágoras para calcular la longitud de la cuerda
  # Formula de pitagoras --> x² = a² + b² 
  # Formula aplicada longitudCuerda² = puerta² + muro²
  
  puerta =  puerta**2
  muro = muro**2
  #longitudCuerda = float((puerta + muro) ** (0.5)) * 100
  longitudCuerda = float(math.sqrt(puerta + muro))


  return longitudCuerda

print(calcular_longitud_cuerda(25, 25))