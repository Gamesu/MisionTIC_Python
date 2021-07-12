from colorama import Fore

def mostrar_menu():
    print("===========================================================")    
    print(Fore.LIGHTYELLOW_EX, "1. Lista total de compuestos con cantidades")
    print(Fore.LIGHTYELLOW_EX, "2. Lista clasificada de compuestos con cantidades")
    print("===========================================================")
    opcion = int(input("Por favor digite al opción del menu:"))
    #opcion = 1

    return opcion

def validar_cantidad(cantidad):
    lista_indices = []

    #Valida si la cantidad es mayor a cero
    if cantidad == 2 or cantidad == 4:
        for x in range(cantidad):
            indice = int(input("Ingrese el indice del compuesto que desea validar: "))
            lista_indices.insert(x, indice - 1)
    else:
        print(Fore.LIGHTMAGENTA_EX, "Solo se permite extraer 2 o 4 elementos")        

    return lista_indices

def extraer_compuesto(indice,compuestos):
    #Se obtiene a continuación la formula del compuesto seleccionado
    lista_Formulas = []

    for x in range(0, len(indice)):
        indiceCompuesto = compuestos[indice[x]]
        posicionCaracter = indiceCompuesto.find(":") + 1
        compuesto = indiceCompuesto[posicionCaracter:len(indiceCompuesto)]
        lista_Formulas.insert(x, compuesto)
    
    return lista_Formulas

def validar_lista_Formulas(lista_Formulas):
    #lista_oxidos, lista_acidos, lista_hidroxido, lista_aniones, lista_cationes = []
    tipolista_Formulas = []
    #valida el tipo de lista_Formulas de acuerod la formula del lista_Formulas seleccionada

    for x in range(0, len(lista_Formulas)):
        compuesto = lista_Formulas[x]
        ultimaPosicionFormula = compuesto[len(compuesto) - 1]
        # Cationes
        if ultimaPosicionFormula == "+":
            tipocompuesto = compuesto + " : Catión"
            #lista_Formulas.insert(x, compuesto)
            #tipocompuesto = "Catión"
            tipolista_Formulas.insert(x, tipocompuesto)
        else:
            # Aniones
            if ultimaPosicionFormula == "–":
                tipocompuesto = compuesto + " : Anión"
                #tipocompuesto = "Anión"
                tipolista_Formulas.insert(x, tipocompuesto)
            else:
                if compuesto[0] == "H" and compuesto[1].isupper() == True:
                        tipocompuesto = compuesto + " : Ácido"
                        #tipocompuesto = "Ácido"
                        tipolista_Formulas.insert(x, tipocompuesto)
                else:
                    if ultimaPosicionFormula == "O" or compuesto[len(compuesto) - 2] == "O":
                        tipocompuesto = compuesto + " : Óxido"
                        #tipocompuesto = "Óxido"
                        tipolista_Formulas.insert(x, tipocompuesto)
                    else:
                        if validar_hidroxilo(compuesto) == True:
                            tipocompuesto = compuesto + " : Hidróxido"
                            #tipocompuesto = "Hidróxido"
                            tipolista_Formulas.insert(x, tipocompuesto)
                        else:
                            tipocompuesto = compuesto + " compuesto Desconocido"
 
    return tipolista_Formulas

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

def clasificar_compuesto(opcion,compuestos_tipo):

    return "OK"

compuestos = [
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
"compuesto 15:Br–"
]
#Lista de cantidades por compuesto
numero_recipientes = ["compuesto 1:4",
"compuesto 2:14",
"compuesto 3:12",
"compuesto 4:14",
"compuesto 5:3",
"compuesto 6:15",
"compuesto 7:8",
"compuesto 8:17",
"compuesto 9:15",
"compuesto 10:20",
"compuesto 11:11",
"compuesto 12:3",
"compuesto 13:4",
"compuesto 14:14",
"compuesto 15:20"
]

print("--------------------------------------------------")
print("--------------------------------------------------")
#=====================================================
# INICIO DEL PROGRAMA
#=====================================================

#Carga menu de inicio
opcion = mostrar_menu()
if opcion == 1:
    #Captura cantidad de compuestos a validar
    cantidad = int(input("Por favor ingrese la cantidad de compuestos a validar: "))
    print("")
    lista_indices = validar_cantidad(cantidad)
    lista_componentes = []
    lista_recipientes = []
    lista_cantidadRec = []

    #=========================================================
    # IMPRIME EL PUNTO DOS DEL RETO // LISTA DE COMPONENTES
    #=========================================================
    for x in range(0, len(lista_indices)):
        lista_componentes.insert(x, numero_recipientes[lista_indices[x]])
        ################
        indiceRecipiente = lista_componentes[x]
        posicionCaracter = indiceRecipiente.find(":") + 1
        nombreCompuesto = indiceRecipiente[0 : posicionCaracter]
        lista_recipientes.insert(x, nombreCompuesto)
        ################
        compuestoFormula = indiceRecipiente[posicionCaracter:len(indiceRecipiente)]
        lista_cantidadRec.insert(x + 1, compuestoFormula)

    tipoCompuesto = validar_lista_Formulas(extraer_compuesto(lista_indices, compuestos))
    print("--------------------------------------------------")
    print(Fore.LIGHTCYAN_EX, "lista_compuestos = [", end=" ")
    for x in range(0, cantidad):
        print(lista_recipientes[x], tipoCompuesto[x], ":", lista_cantidadRec[x], ",", end=" ")
    print("]")
    print("--------------------------------------------------")
else:
    #=========================================================
    # IMPRIME EL PUNTO TRES DEL RETO // LISTA DE COMPONENTES
    #=========================================================
    print("opcion 2")