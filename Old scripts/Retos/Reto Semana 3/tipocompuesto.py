def validar_compuesto(compuesto):
    """ 
  Parameters
  ----------
  formula_compuesto:string
    cadena con fórmula química 
  Returns
  -------
  tipo_compuesto:string
    cadena que indica el tipo óxido, ácido, hidroxilo, cation, anion  
  """  
  #TODO: instrucciones, validación de características usando ciclos condicionales if y retorno de valor
    #valida el tipo de compuesto de acuerod la formula del compuesto seleccionada
    ultimaPosicionFormula = compuesto[len(compuesto) - 1]
    
    # Cationes
    if ultimaPosicionFormula == "+":
        tipoCompuesto = compuesto + " // Catión"
        #tipoCompuesto = "Catión"
    else:
        # Aniones
        if ultimaPosicionFormula == "–":
            tipoCompuesto = compuesto + " // Anión"
            #tipoCompuesto = "Anión"
        else:
            if compuesto[0] == "H" and compuesto[1].isupper() == True:
                    tipoCompuesto = compuesto + " // Ácido"
                    #tipoCompuesto = "Ácido"
            else:
                if ultimaPosicionFormula == "O" or compuesto[len(compuesto) - 2] == "O":
                    tipoCompuesto = compuesto + " // Óxido"
                    #tipoCompuesto = "Óxido"
                else:
                    if validar_hidroxilo(compuesto) == True:
                        tipoCompuesto = compuesto + " // Hidróxido"
                        #tipoCompuesto = "Hidróxido"
                    else:
                        tipoCompuesto = compuesto + " Compuesto Desconocido"

    return tipoCompuesto


def validar_hidroxilo(compuesto):
    # Busca en cada posicion con un ciclo si esta el hidroxilo (OH)
    # Retorna true o false
    compuesto = compuesto.partition("(OH)")
    x = 0
    while x <= len(compuesto):
        if compuesto[x] == "(OH)":
            return True
        else:
            x = x + 1



