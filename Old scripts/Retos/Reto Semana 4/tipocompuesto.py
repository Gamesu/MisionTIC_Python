def validar_lista_Formulas(lista_Formulas):
#def definir_tipo(formula_compuesto):
    #lista_oxidos, lista_acidos, lista_hidroxido, lista_aniones, lista_cationes = []
    tipolista_Formulas = []
    #valida el tipo de lista_Formulas de acuerod la formula del lista_Formulas seleccionada

    for x in range(0, len(lista_Formulas)):
        compuesto = lista_Formulas[x]
        ultimaPosicionFormula = compuesto[len(compuesto) - 1]
        # Cationes
        if ultimaPosicionFormula == "+":
            #tipocompuesto = compuesto + " : Catión"
            #lista_Formulas.insert(x, compuesto)
            tipocompuesto = "Catión"
            tipolista_Formulas.insert(x, tipocompuesto)
        else:
            # Aniones
            if ultimaPosicionFormula == "-":
                #tipocompuesto = compuesto + " : Anión"
                tipocompuesto = "Anión"
                tipolista_Formulas.insert(x, tipocompuesto)
            else:
                if compuesto[0] == "H" and compuesto[1].isupper() == True:
                        #tipocompuesto = compuesto + " : Ácido"
                        tipocompuesto = "Ácido"
                        tipolista_Formulas.insert(x, tipocompuesto)
                else:
                    if ultimaPosicionFormula == "O" or compuesto[len(compuesto) - 2] == "O":
                        #tipocompuesto = compuesto + " : Óxido"
                        tipocompuesto = "Óxido"
                        tipolista_Formulas.insert(x, tipocompuesto)
                    else:
                        if validar_hidroxilo(compuesto) == True:
                            #tipocompuesto = compuesto + " : Hidróxido"
                            tipocompuesto = "Hidróxido"
                            tipolista_Formulas.insert(x, tipocompuesto)
                        else:
                            tipocompuesto = compuesto + " compuesto Desconocido"
 
    return tipolista_Formulas

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
    