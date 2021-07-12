def extraer_compuesto(indice,compuestos):
  #TODO: instrucciones y retorno de valor
  #Se obtiene a continuación la formula del compuesto seleccionado
    lista_Formulas = []
    lista_nombres = []

    for x in range(0, len(indice)):
        indiceCompuesto = compuestos[indice[x]]
        posicionCaracter = indiceCompuesto.find(":") + 1
        nombreCompuesto = indiceCompuesto[0 : posicionCaracter]
        lista_nombres.insert(x, nombreCompuesto)
        formula = indiceCompuesto[posicionCaracter:len(indiceCompuesto)]
        lista_Formulas.insert(x, formula)
    
    return lista_nombres, lista_Formulas