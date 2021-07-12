def calcular_velocidad_giro(d,tmax):
  #TODO: comentarios
  # # Formula de matematica --> V = longitudCuerda / tiempo
  
  #Convertir medida de cuerda a centimetros
  d = d / 60
  #Calcular la velocidad
  velocidadGiros = d / tmax
  velocidadGiros = round(velocidadGiros, 3)

  return velocidadGiros

print(calcular_velocidad_giro(3535.5339059327375,3))
print(calcular_velocidad_giro(4242.640687119285,4))
print(calcular_velocidad_giro(5374.011537017761,5))