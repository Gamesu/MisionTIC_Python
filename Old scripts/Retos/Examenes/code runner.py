def extraer_compuesto(indice,compuestos):
  #TODO: instrucciones, debe recibir un elemento de la lista, separar la formula y retornarla
  indiceCompuesto = compuestos[indice - 1]
  posicionCaracter = indiceCompuesto.find(":") + 1
  compuestoImprimir = indiceCompuesto[posicionCaracter:len(indiceCompuesto)]
  return compuestoImprimir

compuestos=[
"compuesto 1:CoO",
"compuesto 2:HCl",
"compuesto 3:HF",
"compuesto 4:Fe(OH)3",
"compuesto 5:Fe(OH)2",
"compuesto 6:ClO2–",
"compuesto 7:ClO–",
"compuesto 8:H3S+",
"compuesto 9:CO2+",
"compuesto 10:TiO2",
"compuesto 11:ZnO",
"compuesto 12:Al(OH)3",
"compuesto 13:Zn(OH)2",
"compuesto 14:Cl–",
"compuesto 15:Br–",
"compuesto 16:HClO4",
"compuesto 17:HNO3",
"compuesto 18:NH4+",
"compuesto 19:PH4+",
"compuesto 20:Ca(OH)2",
"compuesto 21:Li(OH)",
"compuesto 22:ClO2+",
"compuesto 23:ClO3+",
"compuesto 24:HgO",
"compuesto 25:CrO",
"compuesto 26:H2CrO4",
"compuesto 27:H2CO3",
"compuesto 28:H3PO4",
"compuesto 29:Ni2O3",
"compuesto 30:Ag2O",
"compuesto 31:IO3–",
"compuesto 32:I–",
"compuesto 33:H3O+",
"compuesto 34:ClO+",
"compuesto 35:Cu2O",
"compuesto 36:CuO",
"compuesto 37:Cu(OH)2",
"compuesto 38:CuOH",
"compuesto 39:H2SO4",
"compuesto 40:H+",
"compuesto 41:ClO4-",
"compuesto 42:ClO3-",
"compuesto 43:HF2-",
"compuesto 44:Na(OH)",
"compuesto 45:Ba(OH)",
"compuesto 46:Au2O3",
"compuesto 47:SbH4+",
"compuesto 48:Ba2+",
"compuesto 49:BrO3–"
]
print(extraer_compuesto(7,compuestos))
#print(extraer_compuesto(10,"compuesto 10:TiO2"))
#formula = extraer_compuesto(16,"compuesto 16:HClO4")
#print(formula)

