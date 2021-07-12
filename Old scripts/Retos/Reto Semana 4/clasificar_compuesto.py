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

  #return lista_compuesto_seleccionado, total_cantidad
