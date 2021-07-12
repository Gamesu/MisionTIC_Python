from colorama import Fore

def menu_opciones():
  print("===========================================================")
  print("Bienvenido al programa de organizador de compuestos.")
  print("\nIngrese la opción que desea usar:    ")
  print(Fore.LIGHTWHITE_EX, "1. Organizar compuestos seleccionados")
  print(Fore.LIGHTWHITE_EX, "2. Organizar compuestos - Archivos ")
  print(Fore.LIGHTWHITE_EX, "3. Salir del programa ")
  print("===========================================================")
  opcionMenu = int(input("Por favor digite la opción del menú que desea usar:"))
  #opcionMenu = 2

  while opcionMenu > 3 or opcionMenu < 1:
    print(Fore.LIGHTRED_EX, "¡Opción escogida no esta en la lista indicada!")
    print(Fore.LIGHTWHITE_EX, "")
    opcionMenu = int(input("Por favor digite la opción del menú que desea usar:"))

  return opcionMenu

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