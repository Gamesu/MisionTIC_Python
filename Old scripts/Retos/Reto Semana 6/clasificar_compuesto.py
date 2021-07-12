def clasificar_compuesto(opcion, lista_tipoCompuestos, lista_compuestos, lista_cantidades):
  lista_opciones = ["Catión", "Anión", "Ácido", "Óxido", "Hidróxido"]
  lista_compuesto_seleccionado = []
  total_cantidad = 0

  for x in range(0, len(lista_tipoCompuestos)):
    if lista_tipoCompuestos[x] == lista_opciones[opcion -1]:
      lista_compuesto_seleccionado.insert(x, lista_compuestos[x])
      total_cantidad = total_cantidad + int(lista_cantidades[x])
  
  print("")
  print("Cantidad de compuestos para", lista_opciones[opcion -1], ":", len(lista_compuesto_seleccionado))
  print("Cantidad de recipientes para", lista_opciones[opcion -1], ":", total_cantidad)

  return lista_compuesto_seleccionado

def clasificar_compuesto_archivo(lista_nombres, lista_formulas, lista_cantidades, lista_tipoCompuestos):
  lista_compuestos = ["Catión", "Anión", "Ácido", "Óxido", "Hidróxido"]
  lista_archivos = ["cationes.txt", "aniones.txt", "acidos.txt", "oxidos.txt", "hidroxidos.txt"]

  for x in range(0, len(lista_compuestos)):
    total_cantidad = 0
    archivo = open("data/" + lista_archivos[x], "w", encoding="utf-8")
    for y in range(0, len(lista_tipoCompuestos)):
      if lista_tipoCompuestos[y] == lista_compuestos[x]:
        registro = lista_nombres[y] + " " + lista_formulas[y] + " " + lista_cantidades[y] + "\n"
        archivo.write(registro)
        total_cantidad = total_cantidad + int(lista_cantidades[y])
    #print("\nCantidad de recipientes para", lista_compuestos[x], ":", total_cantidad)
    archivo.write("\nCantidad de recipientes para " + lista_compuestos[x] + " : " + str(total_cantidad))
    archivo.close()
    

  
  
