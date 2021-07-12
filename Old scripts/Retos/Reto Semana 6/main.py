""" Reto # 6 Clasificación y organización de sustancias químicas inorgánicas del anaquel del laboratorio de química
    Oscar Estrada Suazo
    Junio 11-21 """
    
# importar módulos diseñados por el alumno (Dividir)
#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================
import menu as mn
import extraer_archivos as exar
import extraer as ex
import crear_lista_compuesto as cl
import tipocompuesto as tc
import clasificar_compuesto as cc
import crear_tuplas as ct
from colorama import Fore

def crear_dic_compuestos(tupla_compuestos):
    dic_compuestos = {}
    
    for x in range(0, len(tupla_compuestos)):
        datosCompuesto =  tupla_compuestos[x] #('compuesto 46:', 'Au2O3', 'Óxido', 19)
        nombre, formula, tipoCompuesto = datosCompuesto[0], datosCompuesto[1], datosCompuesto[2]
        cantidad = datosCompuesto[3]
        dic_compuestos[formula] = {'Nombre': nombre, 'Tipo': tipoCompuesto, 'Cantidad': cantidad}

    return dic_compuestos

def pintar_tabla(tabla_compuestos):
            
    print ("\n{:<15} {:<20} {:<10}".format('Compuesto','Nombre','Cantidad'))
    print("----------------------------------------------")
    for x in range(0, len(tabla_compuestos)):
        datos_imprimir = tabla_compuestos[x].split(":") #['compuesto 36', 'CuO', 'Óxido', '10']
        print ("{:<15} {:<20} {:<10}".format(datos_imprimir[1], datos_imprimir[0], datos_imprimir[3]))


#Lista con compuestos químicos
#compuestos=["compuesto 1:CoO", "compuesto 2:HCl", "compuesto 3:HF", "compuesto 4:Fe(OH)3", "compuesto 5:Fe(OH)2", "compuesto 6:ClO2-", "compuesto 7:ClO-", "compuesto 8:H3S+", "compuesto 9:CO2+", "compuesto 10:TiO2", "compuesto 11:ZnO", "compuesto 12:Al(OH)3", "compuesto 13:Zn(OH)2", "compuesto 14:Cl-", "compuesto 15:Br-", "compuesto 16:HClO4", "compuesto 17:HNO3", "compuesto 18:NH4+", "compuesto 19:PH4+", "compuesto 20:Ca(OH)2", "compuesto 21:Li(OH)", "compuesto 22:ClO2+", "compuesto 23:ClO3+", "compuesto 24:HgO", "compuesto 25:CrO", "compuesto 26:H2CrO4", "compuesto 27:H2CO3", "compuesto 28:H3PO4", "compuesto 29:Ni2O3", "compuesto 30:Ag2O", "compuesto 31:IO3-", "compuesto 32:I-", "compuesto 33:H3O+", "compuesto 34:ClO+", "compuesto 35:Cu2O", "compuesto 36:CuO", "compuesto 37:Cu(OH)2", "compuesto 38:CuOH", "compuesto 39:H2SO4", "compuesto 40:H+", "compuesto 41:ClO4-", "compuesto 42:ClO3-", "compuesto 43:HF2-", "compuesto 44:Na(OH)", "compuesto 45:Ba(OH)", "compuesto 46:Au2O3", "compuesto 47:SbH4+", "compuesto 48:Ba2+", "compuesto 49:BrO3-", "compuesto 50:BaO", "compuesto 51:Sr2+", "compuesto 52:H3PO2", "compuesto 53:Cr(OH)3", "compuesto 54:Mn4+", "compuesto 55:H5IO6", "compuesto 56:Pb(OH)4", "compuesto 57:PbO", "compuesto 58:CN-", "compuesto 59:Pt2+", "compuesto 60:Mn2O7", "compuesto 61:O3-", "compuesto 62:Fe2O3", "compuesto 63:N3-", "compuesto 64:H2MnO4", "compuesto 65:Hg(OH)2" ]

#Lista de cantidades por compuesto
#numero_recipientes=["compuesto 1:4", "compuesto 2:14", "compuesto 3:12", "compuesto 4:14", "compuesto 5:3", "compuesto 6:15", "compuesto 7:8", "compuesto 8:17", "compuesto 9:15", "compuesto 10:20", "compuesto 11:11", "compuesto 12:3", "compuesto 13:4", "compuesto 14:14", "compuesto 15:20", "compuesto 16:20", "compuesto 17:9", "compuesto 18:6", "compuesto 19:14", "compuesto 20:11", "compuesto 21:14", "compuesto 22:15", "compuesto 23:17", "compuesto 24:2", "compuesto 25:7", "compuesto 26:10", "compuesto 27:15", "compuesto 28:16", "compuesto 29:6", "compuesto 30:8", "compuesto 31:10", "compuesto 32:3", "compuesto 33:13", "compuesto 34:14", "compuesto 35:18", "compuesto 36:10", "compuesto 37:14", "compuesto 38:13", "compuesto 39:1", "compuesto 40:3", "compuesto 41:12", "compuesto 42:9", "compuesto 43:18", "compuesto 44:9", "compuesto 45:16", "compuesto 46:19", "compuesto 47:5", "compuesto 48:2", "compuesto 49:15", "compuesto 50:17", "compuesto 51:8", "compuesto 52:3", "compuesto 53:14", "compuesto 54:19", "compuesto 55:3", "compuesto 56:10", "compuesto 57:20", "compuesto 58:9", "compuesto 59:2", "compuesto 60:19", "compuesto 61:12", "compuesto 62:13", "compuesto 63:3", "compuesto 64:11", "compuesto 65:1" ]

#======================================================================
#FUNCIONES DEL PROGRAMA PRINCIPAL
#TODO: 
print("===============================================================")
print("  ORGANIZADOR DE COMPUESTOS                   ")
print("===============================================================")
opcion = 1
#======================================================================
#Entra a menú de aplicación y no se detiene hasta que el usuario pulse la opcion 2:
while opcion == 1:
    opcion = mn.menu_opciones()
    compuestos = exar.extraer_archivos("data\compuesto.txt", "r")
    numero_recipientes = exar.extraer_archivos("data\cantidades.txt", "r")
    if opcion == 1:
        lista_indices = mn.capturarIndices()
        #======================================================================
        lista_nombres, lista_formulas = ex.extraer_compuesto(lista_indices, compuestos)
        lista_nombres, lista_cantidades = ex.extraer_compuesto(lista_indices, numero_recipientes)
        lista_tipoCompuestos = tc.validar_lista_Formulas(lista_formulas)
        lista_compuestos = cl.crear_lista_compuestos_usuario(lista_nombres, lista_formulas, lista_tipoCompuestos, lista_cantidades)
        #tupla_compuestos = crear_tupla_compuestos(lista_nombres, lista_formulas, lista_tipoCompuestos, lista_cantidades)
        tupla_compuestos = ct.crear_tupla_compuestos(lista_nombres, lista_formulas, lista_tipoCompuestos, lista_cantidades)
        dic_compuestos = crear_dic_compuestos(tupla_compuestos)
        #======================================================================
        #IMPRIMIR SALIDAS DEL PROGRAMA
        print(Fore.LIGHTGREEN_EX, "===============================================================")
        print(Fore.LIGHTGREEN_EX, "  RESULTADO DE LISTA DE COMPUESTOS")
        print(Fore.LIGHTGREEN_EX, "===============================================================")
        print(Fore.LIGHTGREEN_EX, "Lista de compuestos seleccionados =", lista_compuestos)
        print(Fore.LIGHTGREEN_EX, "\n Compuestos = ", tupla_compuestos)
        print(Fore.LIGHTWHITE_EX, "===============================================================")
        print(Fore.LIGHTWHITE_EX, "  RESULTADO DE DICCIONARIO DE COMPUESTOS")
        print(Fore.LIGHTWHITE_EX, "===============================================================")
        print(Fore.LIGHTWHITE_EX, "DICCIONARIO = ", dic_compuestos)
        print(Fore.LIGHTCYAN_EX, "===============================================================")
        print(Fore.LIGHTCYAN_EX, "  MENÚ DE IMPRESIÓN POR COMPUESTO")
        tabla_compuestos = cc.clasificar_compuesto(mn.mostrar_menu(), lista_tipoCompuestos, lista_compuestos, lista_cantidades)
        pintar_tabla(tabla_compuestos)
    elif opcion == 2:
        #======================================================================
        # Opcion de proceso para escribir en archivo de lista_compuestos.txt
        print(Fore.LIGHTMAGENTA_EX, "===============================================================")
        lista_nombres, lista_formulas = ex.extraer_compuesto_archivo(compuestos)
        lista_tipoCompuestos = tc.validar_lista_Formulas(lista_formulas)
        lista_nombres, lista_cantidades = ex.extraer_compuesto_archivo(numero_recipientes)
        cl.crear_lista_compuestos(compuestos, lista_tipoCompuestos, lista_cantidades)
        #======================================================================
        cc.clasificar_compuesto_archivo(lista_nombres, lista_formulas, lista_cantidades, lista_tipoCompuestos)
        #======================================================================
        #IMPRIMIR SALIDAS DEL PROGRAMA
        print(Fore.LIGHTGREEN_EX, "Proceso terminado por favor ingrese a la carpeta data para observar los archivos")
        opcion = 1
    else:
        break

print(Fore.LIGHTWHITE_EX, "===============================================================")
print(Fore.LIGHTWHITE_EX, "Fin de la simulacion, ¡Hasta una proxima ocasión!, ありがとうございました。")

