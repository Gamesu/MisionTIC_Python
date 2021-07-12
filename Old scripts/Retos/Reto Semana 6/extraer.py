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

def extraer_compuesto_archivo(compuestos):
  #Se obtiene a continuación la formula del compuesto seleccionado
  lista_Formulas = []
  lista_nombres = []

  for x in compuestos:
    indiceCompuesto = x
    posicionCaracter = indiceCompuesto.find(":") + 1
    nombre = indiceCompuesto[:posicionCaracter - 1]
    lista_nombres.append(nombre)
    formula = indiceCompuesto[posicionCaracter:len(indiceCompuesto)]
    lista_Formulas.append(formula)
    
  return lista_nombres, lista_Formulas

#compuestos=["compuesto 1:CoO", "compuesto 2:HCl", "compuesto 3:HF"]
#print(extraer_compuesto_archivo(compuestos))