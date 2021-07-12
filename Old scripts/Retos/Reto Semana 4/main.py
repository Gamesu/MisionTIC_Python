""" Reto # 3 Clasificación y organización de sustancias químicas inorgánicas del anaquel del laboratorio de química
    Oscar Estrada Suazo
    Mayo 27-21 """
    
# importar módulos diseñados por el alumno (Dividir)
#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================
import extraer as ex
import tipocompuesto as tc
import clasificar_compuesto as cc
from colorama import Fore

def capturarIndices():
    lista_indices = []
    #Captura cantidad de compuestos a validar
    cantidad = int(input("Por favor ingrese la cantidad de compuestos a validar: "))
    
    #Valida si la cantidad es mayor a cero
    if cantidad == 2 or cantidad == 4:
        for x in range(cantidad):
            indice = int(input("Ingrese el indice del compuesto que desea validar: "))
            lista_indices.insert(x, indice - 1)
    else:
        print(Fore.LIGHTMAGENTA_EX, "Solo se permite extraer 2 o 4 elementos")        

    return lista_indices

def mostrar_menu():
    print("===========================================================")    
    print(Fore.LIGHTCYAN_EX, "1. Lista de Cationes")
    print(Fore.LIGHTCYAN_EX, "2. Lista de Aniones")
    print(Fore.LIGHTCYAN_EX, "3. Lista de Ácidos")
    print(Fore.LIGHTCYAN_EX, "4. Lista de Óxidos")
    print(Fore.LIGHTCYAN_EX, "5. Lista de Hidróxidos")
    print("===========================================================")
    opcion = int(input("Por favor digite al lista que desea imprimir del menu:"))
    #opcion = 1

    return opcion

#Lista con compuestos químicos
compuestos=["compuesto 1:CoO", "compuesto 2:HCl", "compuesto 3:HF", "compuesto 4:Fe(OH)3", "compuesto 5:Fe(OH)2", "compuesto 6:ClO2-", "compuesto 7:ClO-", "compuesto 8:H3S+", "compuesto 9:CO2+", "compuesto 10:TiO2", "compuesto 11:ZnO", "compuesto 12:Al(OH)3", "compuesto 13:Zn(OH)2", "compuesto 14:Cl-", "compuesto 15:Br-", "compuesto 16:HClO4", "compuesto 17:HNO3", "compuesto 18:NH4+", "compuesto 19:PH4+", "compuesto 20:Ca(OH)2", "compuesto 21:Li(OH)", "compuesto 22:ClO2+", "compuesto 23:ClO3+", "compuesto 24:HgO", "compuesto 25:CrO", "compuesto 26:H2CrO4", "compuesto 27:H2CO3", "compuesto 28:H3PO4", "compuesto 29:Ni2O3", "compuesto 30:Ag2O", "compuesto 31:IO3-", "compuesto 32:I-", "compuesto 33:H3O+", "compuesto 34:ClO+", "compuesto 35:Cu2O", "compuesto 36:CuO", "compuesto 37:Cu(OH)2", "compuesto 38:CuOH", "compuesto 39:H2SO4", "compuesto 40:H+", "compuesto 41:ClO4-", "compuesto 42:ClO3-", "compuesto 43:HF2-", "compuesto 44:Na(OH)", "compuesto 45:Ba(OH)", "compuesto 46:Au2O3", "compuesto 47:SbH4+", "compuesto 48:Ba2+", "compuesto 49:BrO3-", "compuesto 50:BaO", "compuesto 51:Sr2+", "compuesto 52:H3PO2", "compuesto 53:Cr(OH)3", "compuesto 54:Mn4+", "compuesto 55:H5IO6", "compuesto 56:Pb(OH)4", "compuesto 57:PbO", "compuesto 58:CN-", "compuesto 59:Pt2+", "compuesto 60:Mn2O7", "compuesto 61:O3-", "compuesto 62:Fe2O3", "compuesto 63:N3-", "compuesto 64:H2MnO4", "compuesto 65:Hg(OH)2" ]

#Lista de cantidades por compuesto
numero_recipientes=["compuesto 1:4", "compuesto 2:14", "compuesto 3:12", "compuesto 4:14", "compuesto 5:3", "compuesto 6:15", "compuesto 7:8", "compuesto 8:17", "compuesto 9:15", "compuesto 10:20", "compuesto 11:11", "compuesto 12:3", "compuesto 13:4", "compuesto 14:14", "compuesto 15:20", "compuesto 16:20", "compuesto 17:9", "compuesto 18:6", "compuesto 19:14", "compuesto 20:11", "compuesto 21:14", "compuesto 22:15", "compuesto 23:17", "compuesto 24:2", "compuesto 25:7", "compuesto 26:10", "compuesto 27:15", "compuesto 28:16", "compuesto 29:6", "compuesto 30:8", "compuesto 31:10", "compuesto 32:3", "compuesto 33:13", "compuesto 34:14", "compuesto 35:18", "compuesto 36:10", "compuesto 37:14", "compuesto 38:13", "compuesto 39:1", "compuesto 40:3", "compuesto 41:12", "compuesto 42:9", "compuesto 43:18", "compuesto 44:9", "compuesto 45:16", "compuesto 46:19", "compuesto 47:5", "compuesto 48:2", "compuesto 49:15", "compuesto 50:17", "compuesto 51:8", "compuesto 52:3", "compuesto 53:14", "compuesto 54:19", "compuesto 55:3", "compuesto 56:10", "compuesto 57:20", "compuesto 58:9", "compuesto 59:2", "compuesto 60:19", "compuesto 61:12", "compuesto 62:13", "compuesto 63:3", "compuesto 64:11", "compuesto 65:1" ]
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#======================================================================
#FUNCIONES DEL PROGRAMA PRINCIPAL
#TODO: 
print("===============================================================")
print("  ORGANIZADOR DE COMPUESTOS                   ")
print("===============================================================")
#======================================================================
#ENTRADAS DEL USUARIO
#TODO:
lista_indices = capturarIndices()
#======================================================================
#INICIACILIZACION DE VARIABLES Y LISTAS
#LLAMADO A FUCNIONES DEL PROGRAMA
#TODO:
lista_nombres, lista_formulas = ex.extraer_compuesto(lista_indices, compuestos)
lista_nombres, lista_cantidades = ex.extraer_compuesto(lista_indices, numero_recipientes)
lista_tipoCompuestos = tc.validar_lista_Formulas(lista_formulas)
lista_compuestos = []

for x in range(0, len(lista_nombres)):
    itemCompuesto = lista_nombres[x] + lista_formulas[x] + ":" + lista_tipoCompuestos[x] + ":" + lista_cantidades[x]
    lista_compuestos.insert(x, itemCompuesto)

#print(lista_nombres, "----", lista_formulas, "-------", lista_cantidades, "----", lista_tipoCompuestos)
#======================================================================
#IMPRIMIR SALIDAS DEL PROGRAMA
#TODO:
print(Fore.LIGHTGREEN_EX, "===============================================================")
print(Fore.LIGHTGREEN_EX, "  RESULTADO DE LISTA DE COMPUESTOS")
print(Fore.LIGHTGREEN_EX, "===============================================================")
print(Fore.LIGHTGREEN_EX, "Lista de compuestos seleccionados =", lista_compuestos)
print(Fore.LIGHTCYAN_EX, "===============================================================")
print(Fore.LIGHTCYAN_EX, "  MENÚ DE IMPRESIÓN POR COMPUESTO")
cc.clasificar_compuesto(mostrar_menu(), lista_tipoCompuestos, lista_compuestos, lista_cantidades)
print(Fore.LIGHTWHITE_EX, "===============================================================")
print(Fore.LIGHTWHITE_EX, "Fin de la simulacion, ¡Hasta una proxima ocasión!, ありがとうございました。")

