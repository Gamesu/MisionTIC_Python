def crear_tupla_compuestos(lista_nombres, lista_formulas, lista_tipoCompuestos, lista_cantidades):
    tupla_compuestos = []

    for x in range(0, len(lista_nombres)):
        nombre, formula, tipoComponente = lista_nombres[x], lista_formulas[x], lista_tipoCompuestos[x]
        cantidad = int(lista_cantidades[x])
        #itemCompuesto = (lista_nombres[x], lista_formulas[x], lista_tipoCompuestos[x], lista_cantidades[x])
        itemCompuesto = (nombre, formula, tipoComponente, cantidad)
        tupla_compuestos.insert(x, itemCompuesto)

    return tupla_compuestos