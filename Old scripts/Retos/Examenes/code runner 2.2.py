def calcular_numero_vueltas_polea(lcuerda,lpolea):
  #TODO: comentarios
  # Formula de matematica --> V = X² / C
  # Formula aplicada cantidad de vueltas --> numeroVueltas = longitudCuerda / longitudPolea

  numeroVueltas = lcuerda / lpolea
  numeroVueltas = round(numeroVueltas, 3)

  return numeroVueltas


print(calcular_numero_vueltas_polea(23, 88))