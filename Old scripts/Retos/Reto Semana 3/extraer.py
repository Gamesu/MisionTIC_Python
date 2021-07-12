def extraer_compuesto(indice,compuestos):
  """ 
  Parameters
  ----------
  indice:int
     indica la posicion del compuesto a buscar
  compuestos:list string
     lista con compuestos
  Returns
  -------
  formula:string
    cadena con fórmula química    
  """  
  #TODO: instrucciones y retorno de valor
    #TODO: instrucciones, debe recibir un elemento de la lista, separar la formula y retornarla

  #Validamos si el numero del compuesto esta en la lista, sino mostramos error
  if indice <= len(compuestos) and indice > 0:
      #Se obtiene a continuación la formula del compuesto seleccionado
      indiceCompuesto = compuestos[indice - 1]
      posicionCaracter = indiceCompuesto.find(":") + 1
      compuesto = indiceCompuesto[posicionCaracter:len(indiceCompuesto)]
      return compuesto
  else:
      return "False"