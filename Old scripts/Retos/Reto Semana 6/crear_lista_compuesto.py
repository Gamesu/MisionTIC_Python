import extraer as ex
import tipocompuesto as tc

def crear_lista_compuestos(compuestos, lista_tipoCompuestos, lista_cantidades):
  archivo = open("data\lista_compuestos.txt", "w", encoding="utf-8")

  for x in range(0, len(compuestos)):
    archivo.write(compuestos[x] + ":" + lista_tipoCompuestos[x] + ":" + lista_cantidades[x] + "\n")
  archivo.close()

def crear_lista_compuestos_usuario(lista_nombres, lista_formulas, lista_tipoCompuestos, lista_cantidades):
  lista_compuestos = []

  for x in range(0, len(lista_nombres)):
        itemCompuesto = lista_nombres[x] + lista_formulas[x] + ":" + lista_tipoCompuestos[x] + ":" + lista_cantidades[x]
        lista_compuestos.insert(x, itemCompuesto)
    
  return lista_compuestos

"""
compuestos = ["compuesto 1:CoO", "compuesto 2:HCl", "compuesto 3:HF"]
lista_tipoCompuestos =['Óxido', 'Ácido', 'Ácido']
lista_cantidades = ['4', '14', '12']

crear_lista_compuestos(compuestos, lista_tipoCompuestos, lista_cantidades)
"""