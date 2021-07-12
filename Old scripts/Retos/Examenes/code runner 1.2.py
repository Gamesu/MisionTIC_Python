def definir_tipo(formula_compuesto):
  #TODO: instrucciones, validación de características usando ciclos condicionales if y retorno de valor
    #valida el tipo de compuesto de acuerod la formula del compuesto seleccionada
    ultimaPosicionFormula = formula_compuesto[len(formula_compuesto) - 1]
    
    # Cationes
    if ultimaPosicionFormula == "+":
        tipoCompuesto = "Cation"
        #tipoCompuesto = "Catión"
    else:
        # Aniones
        if ultimaPosicionFormula == "-":
            tipoCompuesto = "Anion"
            #tipoCompuesto = "Anión"
        else:
            if formula_compuesto[0] == "H":
                    tipoCompuesto = "Ácido"
                    #tipoCompuesto = "Ácido"
            else:
                if ultimaPosicionFormula == "O" or formula_compuesto[len(formula_compuesto) - 2] == "O":
                    tipoCompuesto = "Óxido"
                    #tipoCompuesto = "Óxido"
                else:
                    if validar_hidroxilo(formula_compuesto) == True:
                        tipoCompuesto = "Hidróxido"
                        #tipoCompuesto = "Hidróxido"
                    else:
                        tipoCompuesto = " Compuesto Desconocido"

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

 	

print(definir_tipo("ClO-"))
print(definir_tipo("HF3PFO4"))
print("-----------")
print(definir_tipo("ClO-"))
print(definir_tipo("TiO2"))
print(definir_tipo("H3S+"))
print(definir_tipo("HF3PFO4"))
print(definir_tipo("Ca(OH)2"))
