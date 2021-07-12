def clasificar_compuesto(opcion,compuestos_tipo):
  lista_opciones = ["Cation", "Anion", "Hidróxido", "Ácido", "Óxido"]
  lista_compuesto_seleccionado = []
  total_cantidad = 0
  total_componentes = 0

  for x in range(0, len(compuestos_tipo)): #compuesto 1:CoO:Óxido:4
    valores = compuestos_tipo[x].split(":")
    #print(valores[2])
    opcion_sel = lista_opciones[int(opcion) -1]
    if valores[2] == opcion_sel:
      lista_compuesto_seleccionado.insert(x, compuestos_tipo[x])
      total_cantidad = total_cantidad + int(valores[3])
      total_componentes = total_componentes + 1

  return opcion_sel,  lista_compuesto_seleccionado, total_cantidad, total_componentes

compuestos_tipo =['compuesto 1:CoO:Óxido:4', 'compuesto 2:HCl:Ácido:14', 'compuesto 3:HF:Ácido:12', 'compuesto 4:Fe(OH)3:Hidróxido:14', 'compuesto 5:Fe(OH)2:Hidróxido:3', 'compuesto 6:ClO2-:Anion:15', 'compuesto 7:ClO-:Anion:8', 'compuesto 8:H3S+:Cation:17', 'compuesto 9:CO2+:Cation:15', 'compuesto 10:TiO2:Óxido:20', 'compuesto 11:ZnO:Óxido:11', 'compuesto 12:Al(OH)3:Hidróxido:3', 'compuesto 13:Zn(OH)2:Hidróxido:4', 'compuesto 14:Cl-:Anion:14', 'compuesto 15:Br-:Anion:20', 'compuesto 16:HClO4:Ácido:20', 'compuesto 17:HNO3:Ácido:9', 'compuesto 18:NH4+:Cation:6', 'compuesto 19:PH4+:Cation:14', 'compuesto 20:Ca(OH)2:Hidróxido:11', 'compuesto 21:Li(OH):Hidróxido:14', 'compuesto 22:ClO2+:Cation:15', 'compuesto 23:ClO3+:Cation:17', 'compuesto 24:HgO:Óxido:2', 'compuesto 25:CrO:Óxido:7', 'compuesto 26:H2CrO4:Ácido:10', 'compuesto 27:H2CO3:Ácido:15', 'compuesto 28:H3PO4:Ácido:16', 'compuesto 29:Ni2O3:Óxido:6', 'compuesto 30:Ag2O:Óxido:8', 'compuesto 31:IO3-:Anion:10', 'compuesto 32:I-:Anion:3', 'compuesto 33:H3O+:Cation:13', 'compuesto 34:ClO+:Cation:14', 'compuesto 35:Cu2O:Óxido:18', 'compuesto 36:CuO:Óxido:10', 'compuesto 37:Cu(OH)2:Hidróxido:14', 'compuesto 38:CuOH:Óxido:13', 'compuesto 39:H2SO4:Ácido:1', 'compuesto 40:H+:Cation:3', 'compuesto 41:ClO4-:Anion:12', 'compuesto 42:ClO3-:Anion:9', 'compuesto 43:HF2-:Anion:18', 'compuesto 44:Na(OH):Hidróxido:9', 'compuesto 45:Ba(OH):Hidróxido:16', 'compuesto 46:Au2O3:Óxido:19', 'compuesto 47:SbH4+:Cation:5', 'compuesto 48:Ba2+:Cation:2', 'compuesto 49:BrO3-:Anion:15', 'compuesto 50:BaO:Óxido:17', 'compuesto 51:Sr2+:Cation:8', 'compuesto 52:H3PO2:Ácido:3', 'compuesto 53:Cr(OH)3:Hidróxido:14', 'compuesto 54:Mn4+:Cation:19', 'compuesto 55:H5IO6:Ácido:3', 'compuesto 56:Pb(OH)4:Hidróxido:10', 'compuesto 57:PbO:Óxido:20', 'compuesto 58:CN-:Anion:9', 'compuesto 59:Pt2+:Cation:2', 'compuesto 60:Mn2O7:Óxido:19', 'compuesto 61:O3-:Anion:12', 'compuesto 62:Fe2O3:Óxido:13', 'compuesto 63:N3-:Anion:3', 'compuesto 64:H2MnO4:Ácido:11', 'compuesto 65:Hg(OH)2:Hidróxido:1']

#print(clasificar_compuesto('1',compuestos_tipo))
#print(clasificar_compuesto('2',compuestos_tipo))
print(clasificar_compuesto('3',compuestos_tipo))
print(clasificar_compuesto('4',compuestos_tipo))
print(clasificar_compuesto('5',compuestos_tipo))