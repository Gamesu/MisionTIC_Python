def calcular_numero_chewbaccas(num_vueltas,v_por_chewbacca):
  #TODO: comentarios
  # Formula de matematica --> V = X² / C
  # Formula aplicada cantidad de Chewbaccas --> Chew = canitidadVueltas / 3

  maxVueltasChewbacca = v_por_chewbacca
  cantidadChewbaccas = num_vueltas / maxVueltasChewbacca
  cantidadChewbaccas = round(cantidadChewbaccas)

  return cantidadChewbaccas


 	

print(calcular_numero_chewbaccas(11.797248280679321,3))
print(calcular_numero_chewbaccas(13.50474474235659,3))
print(calcular_numero_chewbaccas(11.253953951963826,3))