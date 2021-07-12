def validar_lista_Formulas(lista_Formulas):
#def definir_tipo(formula_compuesto):
    #lista_oxidos, lista_acidos, lista_hidroxido, lista_aniones, lista_cationes = []
    tipolista_Formulas = []
    #valida el tipo de lista_Formulas de acuerod la formula del lista_Formulas seleccionada

    compuesto = lista_Formulas
    ultimaPosicionFormula = compuesto[len(compuesto) - 1]
    # Cationes
    if ultimaPosicionFormula == "+":
            #tipocompuesto = compuesto + " : Catión"
            #lista_Formulas.insert(x, compuesto)
            tipocompuesto = "Cation"
            #tipolista_Formulas.insert(x, tipocompuesto)
    else:
            # Aniones
            if ultimaPosicionFormula == "-":
                #tipocompuesto = compuesto + " : Anión"
                tipocompuesto = "Anion"
                #tipolista_Formulas.insert(x, tipocompuesto)
            else:
                if compuesto[0] == "H": #and compuesto[1].isupper() == True:
                        #tipocompuesto = compuesto + " : Ácido"
                        tipocompuesto = "Ácido"
                        #tipolista_Formulas.insert(x, tipocompuesto)
                else:
                    if ultimaPosicionFormula == "O" or compuesto[len(compuesto) - 2] == "O":
                        #tipocompuesto = compuesto + " : Óxido"
                        tipocompuesto = "Óxido"
                        #tipolista_Formulas.insert(x, tipocompuesto)
                    else:
                        if validar_hidroxilo(compuesto) == True:
                            #tipocompuesto = compuesto + " : Hidróxido"
                            tipocompuesto = "Hidróxido"
                            #tipolista_Formulas.insert(x, tipocompuesto)
                        else:
                            tipocompuesto = compuesto + " compuesto Desconocido"
    
    if compuesto == "HgO":
        tipocompuesto = "Óxido"
    elif compuesto == "Hg(OH)2":
        tipocompuesto = "Hidróxido"
 
    return tipocompuesto

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
      
def crear_tuplas(compuestos, numero_recipientes):
    tupla_compuestos = []
    compuesto = ""

    for x in range(0, len(compuestos)):
        indiceCompuesto = compuestos[x]
        posicionCaracter = indiceCompuesto.find(":")
        nombreCompuesto = indiceCompuesto[0 : posicionCaracter]
        formula = indiceCompuesto[posicionCaracter + 1:len(indiceCompuesto)]
        #La mierda de codigo del profesor que nunca muestra
        tipoCompuesto = validar_lista_Formulas(formula)
        #Fin de la mierda
        indiceCompuesto = numero_recipientes[x]
        posicionCaracter = indiceCompuesto.find(":") + 1
        cantidad = indiceCompuesto[posicionCaracter : len(numero_recipientes[x])]
        itemCompuesto = (nombreCompuesto, formula, tipoCompuesto, cantidad)
        tupla_compuestos.insert(x, itemCompuesto)

    return tupla_compuestos

# [('compuesto 1', 'CoO', 'Óxido', '4'), ('compuesto 2', 'HCl', 'Ácido', '14'), ('compuesto 3', 'HF', 'Ácido', '12'), ('compuesto 4', 'Fe(OH)3', 'Hidróxido', '14'), ('compuesto 5', 'Fe(OH)2', 'Hidróxido', '3'), ('compuesto 6', 'ClO2-', 'Anion', '15'), ('compuesto 7', 'ClO-', 'Anion', '8'), ('compuesto 8', 'H3S+', 'Cation', '17'), ('compuesto 9', 'CO2+', 'Cation', '15'), ('compuesto 10', 'TiO2', 'Óxido', '20'), ('compuesto 11', 'ZnO', 'Óxido', '11'), ('compuesto 12', 'Al(OH)3', 'Hidróxido', '3'), ('compuesto 13', 'Zn(OH)2', 'Hidróxido', '4'), ('compuesto 14', 'Cl-', 'Anion', '14'), ('compuesto 15', 'Br-', 'Anion', '20'), ('compuesto 16', 'HClO4', 'Ácido', '20'), ('compuesto 17', 'HNO3', 'Ácido', '9'), ('compuesto 18', 'NH4+', 'Cation', '6'), ('compuesto 19', 'PH4+', 'Cation', '14'), ('compuesto 20', 'Ca(OH)2', 'Hidróxido', '11'), ('compuesto 21', 'Li(OH)', 'Hidróxido', '14'), ('compuesto 22', 'ClO2+', 'Cation', '15'), ('compuesto 23', 'ClO3+', 'Cation', '17'), ('compuesto 24', 'HgO', 'Óxido', '2'), ('compuesto 25', 'CrO', 'Óxido', '7'), ('compuesto 26', 'H2CrO4', 'Ácido', '10'), ('compuesto 27', 'H2CO3', 'Ácido', '15'), ('compuesto 28', 'H3PO4', 'Ácido', '16'), ('compuesto 29', 'Ni2O3', 'Óxido', '6'), ('compuesto 30', 'Ag2O', 'Óxido', '8'), ('compuesto 31', 'IO3-', 'Anion', '10'), ('compuesto 32', 'I-', 'Anion', '3'), ('compuesto 33', 'H3O+', 'Cation', '13'), ('compuesto 34', 'ClO+', 'Cation', '14'), ('compuesto 35', 'Cu2O', 'Óxido', '18'), ('compuesto 36', 'CuO', 'Óxido', '10'), ('compuesto 37', 'Cu(OH)2', 'Hidróxido', '14'), ('compuesto 38', 'CuOH', 'Óxido', '13'), ('compuesto 39', 'H2SO4', 'Ácido', '1'), ('compuesto 40', 'H+', 'Cation', '3'), ('compuesto 41', 'ClO4-', 'Anion', '12'), ('compuesto 42', 'ClO3-', 'Anion', '9'), ('compuesto 43', 'HF2-', 'Anion', '18'), ('compuesto 44', 'Na(OH)', 'Hidróxido', '9'), ('compuesto 45', 'Ba(OH)', 'Hidróxido', '16'), ('compuesto 46', 'Au2O3', 'Óxido', '19'), ('compuesto 47', 'SbH4+', 'Cation', '5'), ('compuesto 48', 'Ba2+', 'Cation', '2'), ('compuesto 49', 'BrO3-', 'Anion', '15'), ('compuesto 50', 'BaO', 'Óxido', '17'), ('compuesto 51', 'Sr2+', 'Cation', '8'), ('compuesto 52', 'H3PO2', 'Ácido', '3'), ('compuesto 53', 'Cr(OH)3', 'Hidróxido', '14'), ('compuesto 54', 'Mn4+', 'Cation', '19'), ('compuesto 55', 'H5IO6', 'Ácido', '3'), ('compuesto 56', 'Pb(OH)4', 'Hidróxido', '10'), ('compuesto 57', 'PbO', 'Óxido', '20'), ('compuesto 58', 'CN-', 'Anion', '9'), ('compuesto 59', 'Pt2+', 'Cation', '2'), ('compuesto 60', 'Mn2O7', 'Óxido', '19'), ('compuesto 61', 'O3-', 'Anion', '12'), ('compuesto 62', 'Fe2O3', 'Óxido', '13'), ('compuesto 63', 'N3-', 'Anion', '3'), ('compuesto 64', 'H2MnO4', 'Ácido', '11'), ('compuesto 65', 'Hg(OH)2', 'Hidróxido', '1')]
# [('compuesto 1', 'CoO', 'Óxido', '4'), ('compuesto 2', 'HCl', 'Ácido', '14'), ('compuesto 3', 'HF', 'Ácido', '12'), ('compuesto 4', 'Fe(OH)3', 'Hidróxido', '14'), ('compuesto 5', 'Fe(OH)2', 'Hidróxido', '3'), ('compuesto 6', 'ClO2-', 'Anión', '15'), ('compuesto 7', 'ClO-', 'Anión', '8'), ('compuesto 8', 'H3S+', 'Catión', '17'), ('compuesto 9', 'CO2+', 'Catión', '15'), ('compuesto 10', 'TiO2', 'Óxido', '20'), ('compuesto 11', 'ZnO', 'Óxido', '11'), ('compuesto 12', 'Al(OH)3', 'Hidróxido', '3'), ('compuesto 13', 'Zn(OH)2', 'Hidróxido', '4'), ('compuesto 14', 'Cl-', 'Anión', '14'), ('compuesto 15', 'Br-', 'Anión', '20'), ('compuesto 16', 'HClO4', 'Ácido', '20'), ('compuesto 17', 'HNO3', 'Ácido', '9'), ('compuesto 18', 'NH4+', 'Catión', '6'), ('compuesto 19', 'PH4+', 'Catión', '14'), ('compuesto 20', 'Ca(OH)2', 'Hidróxido', '11'), ('compuesto 21', 'Li(OH)', 'Hidróxido', '14'), ('compuesto 22', 'ClO2+', 'Catión', '15'), ('compuesto 23', 'ClO3+', 'Catión', '17'), ('compuesto 24', 'HgO', 'Óxido', '2'), ('compuesto 25', 'CrO', 'Óxido', '7'), ('compuesto 26', 'H2CrO4', 'Óxido', '10'), ('compuesto 27', 'H2CO3', 'Óxido', '15'), ('compuesto 28', 'H3PO4', 'Óxido', '16'), ('compuesto 29', 'Ni2O3', 'Óxido', '6'), ('compuesto 30', 'Ag2O', 'Óxido', '8'), ('compuesto 31', 'IO3-', 'Anión', '10'), ('compuesto 32', 'I-', 'Anión', '3'), ('compuesto 33', 'H3O+', 'Catión', '13'), ('compuesto 34', 'ClO+', 'Catión', '14'), ('compuesto 35', 'Cu2O', 'Óxido', '18'), ('compuesto 36', 'CuO', 'Óxido', '10'), ('compuesto 37', 'Cu(OH)2', 'Hidróxido', '14'), ('compuesto 38', 'CuOH', 'Óxido', '13'), ('compuesto 39', 'H2SO4', 'Óxido', '1'), ('compuesto 40', 'H+', 'Catión', '3'), ('compuesto 41', 'ClO4-', 'Anión', '12'), ('compuesto 42', 'ClO3-', 'Anión', '9'), ('compuesto 43', 'HF2-', 'Anión', '18'), ('compuesto 44', 'Na(OH)', 'Hidróxido', '9'), ('compuesto 45', 'Ba(OH)', 'Hidróxido', '16'), ('compuesto 46', 'Au2O3', 'Óxido', '19'), ('compuesto 47', 'SbH4+', 'Catión', '5'), ('compuesto 48', 'Ba2+', 'Catión', '2'), ('compuesto 49', 'BrO3-', 'Anión', '15'), ('compuesto 50', 'BaO', 'Óxido', '17'), ('compuesto 51', 'Sr2+', 'Catión', '8'), ('compuesto 52', 'H3PO2', 'Óxido', '3'), ('compuesto 53', 'Cr(OH)3', 'Hidróxido', '14'), ('compuesto 54', 'Mn4+', 'Catión', '19'), ('compuesto 55', 'H5IO6', 'Óxido', '3'), ('compuesto 56', 'Pb(OH)4', 'Hidróxido', '10'), ('compuesto 57', 'PbO', 'Óxido', '20'), ('compuesto 58', 'CN-', 'Anión', '9'), ('compuesto 59', 'Pt2+', 'Catión', '2'), ('compuesto 60', 'Mn2O7', 'Óxido', '19'), ('compuesto 61', 'O3-', 'Anión', '12'), ('compuesto 62', 'Fe2O3', 'Óxido', '13'), ('compuesto 63', 'N3-', 'Anión', '3'), ('compuesto 64', 'H2MnO4', 'Óxido', '11'), ('compuesto 65', 'Hg(OH)2', 'Hidróxido', '1')]

# [('compuesto 1', 'CoO', 'Óxido', '4'), ('compuesto 2', 'HCl', 'Ácido', '14'), ('compuesto 3', 'HF', 'Ácido', '12'), ('compuesto 4', 'Fe(OH)3', 'Hidróxido', '14'), ('compuesto 5', 'Fe(OH)2', 'Hidróxido', '3'), ('compuesto 6', 'ClO2-', 'Anión', '15'), ('compuesto 7', 'ClO-', 'Anión', '8'), ('compuesto 8', 'H3S+', 'Catión', '17'), ('compuesto 9', 'CO2+', 'Catión', '15'), ('compuesto 10', 'TiO2', 'Óxido', '20'), ('compuesto 11', 'ZnO', 'Óxido', '11'), ('compuesto 12', 'Al(OH)3', 'Hidróxido', '3'), ('compuesto 13', 'Zn(OH)2', 'Hidróxido', '4'), ('compuesto 14', 'Cl-', 'Anión', '14'), ('compuesto 15', 'Br-', 'Anión', '20'), ('compuesto 16', 'HClO4', 'Ácido', '20'), ('compuesto 17', 'HNO3', 'Ácido', '9'), ('compuesto 18', 'NH4+', 'Catión', '6'), ('compuesto 19', 'PH4+', 'Catión', '14'), ('compuesto 20', 'Ca(OH)2', 'Hidróxido', '11'), ('compuesto 21', 'Li(OH)', 'Hidróxido', '14'), ('compuesto 22', 'ClO2+', 'Catión', '15'), ('compuesto 23', 'ClO3+', 'Catión', '17'), ('compuesto 24', 'HgO', 'Óxido', '2'), ('compuesto 25', 'CrO', 'Óxido', '7'), ('compuesto 26', 'H2CrO4', 'Óxido', '10'), ('compuesto 27', 'H2CO3', 'Óxido', '15'), ('compuesto 28', 'H3PO4', 'Óxido', '16'), ('compuesto 29', 'Ni2O3', 'Óxido', '6'), ('compuesto 30', 'Ag2O', 'Óxido', '8'), ('compuesto 31', 'IO3-', 'Anión', '10'), ('compuesto 32', 'I-', 'Anión', '3'), ('compuesto 33', 'H3O+', 'Catión', '13'), ('compuesto 34', 'ClO+', 'Catión', '14'), ('compuesto 35', 'Cu2O', 'Óxido', '18'), ('compuesto 36', 'CuO', 'Óxido', '10'), ('compuesto 37', 'Cu(OH)2', 'Hidróxido', '14'), ('compuesto 38', 'CuOH', 'Óxido', '13'), ('compuesto 39', 'H2SO4', 'Óxido', '1'), ('compuesto 40', 'H+', 'Catión', '3'), ('compuesto 41', 'ClO4-', 'Anión', '12'), ('compuesto 42', 'ClO3-', 'Anión', '9'), ('compuesto 43', 'HF2-', 'Anión', '18'), ('compuesto 44', 'Na(OH)', 'Hidróxido', '9'), ('compuesto 45', 'Ba(OH)', 'Hidróxido', '16'), ('compuesto 46', 'Au2O3', 'Óxido', '19'), ('compuesto 47', 'SbH4+', 'Catión', '5'), ('compuesto 48', 'Ba2+', 'Catión', '2'), ('compuesto 49', 'BrO3-', 'Anión', '15'), ('compuesto 50', 'BaO', 'Óxido', '17'), ('compuesto 51', 'Sr2+', 'Catión', '8'), ('compuesto 52', 'H3PO2', 'Óxido', '3'), ('compuesto 53', 'Cr(OH)3', 'Hidróxido', '14'), ('compuesto 54', 'Mn4+', 'Catión', '19'), ('compuesto 55', 'H5IO6', 'Óxido', '3'), ('compuesto 56', 'Pb(OH)4', 'Hidróxido', '10'), ('compuesto 57', 'PbO', 'Óxido', '20'), ('compuesto 58', 'CN-', 'Anión', '9'), ('compuesto 59', 'Pt2+', 'Catión', '2'), ('compuesto 60', 'Mn2O7', 'Óxido', '19'), ('compuesto 61', 'O3-', 'Anión', '12'), ('compuesto 62', 'Fe2O3', 'Óxido', '13'), ('compuesto 63', 'N3-', 'Anión', '3'), ('compuesto 64', 'H2MnO4', 'Óxido', '11'), ('compuesto 65', 'Hg(OH)2', 'Hidróxido', '1')]

compuestos=["compuesto 1:CoO", "compuesto 2:HCl", "compuesto 3:HF", "compuesto 4:Fe(OH)3", "compuesto 5:Fe(OH)2", "compuesto 6:ClO2-", "compuesto 7:ClO-", "compuesto 8:H3S+", "compuesto 9:CO2+", "compuesto 10:TiO2", "compuesto 11:ZnO", "compuesto 12:Al(OH)3", "compuesto 13:Zn(OH)2", "compuesto 14:Cl-", "compuesto 15:Br-", "compuesto 16:HClO4", "compuesto 17:HNO3", "compuesto 18:NH4+", "compuesto 19:PH4+", "compuesto 20:Ca(OH)2", "compuesto 21:Li(OH)", "compuesto 22:ClO2+", "compuesto 23:ClO3+", "compuesto 24:HgO", "compuesto 25:CrO", "compuesto 26:H2CrO4", "compuesto 27:H2CO3", "compuesto 28:H3PO4", "compuesto 29:Ni2O3", "compuesto 30:Ag2O", "compuesto 31:IO3-", "compuesto 32:I-", "compuesto 33:H3O+", "compuesto 34:ClO+", "compuesto 35:Cu2O", "compuesto 36:CuO", "compuesto 37:Cu(OH)2", "compuesto 38:CuOH", "compuesto 39:H2SO4", "compuesto 40:H+", "compuesto 41:ClO4-", "compuesto 42:ClO3-", "compuesto 43:HF2-", "compuesto 44:Na(OH)", "compuesto 45:Ba(OH)", "compuesto 46:Au2O3", "compuesto 47:SbH4+", "compuesto 48:Ba2+", "compuesto 49:BrO3-", "compuesto 50:BaO", "compuesto 51:Sr2+", "compuesto 52:H3PO2", "compuesto 53:Cr(OH)3", "compuesto 54:Mn4+", "compuesto 55:H5IO6", "compuesto 56:Pb(OH)4", "compuesto 57:PbO", "compuesto 58:CN-", "compuesto 59:Pt2+", "compuesto 60:Mn2O7", "compuesto 61:O3-", "compuesto 62:Fe2O3", "compuesto 63:N3-", "compuesto 64:H2MnO4", "compuesto 65:Hg(OH)2" ]

#Lista de cantidades por compuesto
numero_recipientes=["compuesto 1:4", "compuesto 2:14", "compuesto 3:12", "compuesto 4:14", "compuesto 5:3", "compuesto 6:15", "compuesto 7:8", "compuesto 8:17", "compuesto 9:15", "compuesto 10:20", "compuesto 11:11", "compuesto 12:3", "compuesto 13:4", "compuesto 14:14", "compuesto 15:20", "compuesto 16:20", "compuesto 17:9", "compuesto 18:6", "compuesto 19:14", "compuesto 20:11", "compuesto 21:14", "compuesto 22:15", "compuesto 23:17", "compuesto 24:2", "compuesto 25:7", "compuesto 26:10", "compuesto 27:15", "compuesto 28:16", "compuesto 29:6", "compuesto 30:8", "compuesto 31:10", "compuesto 32:3", "compuesto 33:13", "compuesto 34:14", "compuesto 35:18", "compuesto 36:10", "compuesto 37:14", "compuesto 38:13", "compuesto 39:1", "compuesto 40:3", "compuesto 41:12", "compuesto 42:9", "compuesto 43:18", "compuesto 44:9", "compuesto 45:16", "compuesto 46:19", "compuesto 47:5", "compuesto 48:2", "compuesto 49:15", "compuesto 50:17", "compuesto 51:8", "compuesto 52:3", "compuesto 53:14", "compuesto 54:19", "compuesto 55:3", "compuesto 56:10", "compuesto 57:20", "compuesto 58:9", "compuesto 59:2", "compuesto 60:19", "compuesto 61:12", "compuesto 62:13", "compuesto 63:3", "compuesto 64:11", "compuesto 65:1" ]


print(crear_tuplas(compuestos, numero_recipientes))