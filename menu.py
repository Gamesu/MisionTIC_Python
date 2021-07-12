from colorama import Fore

def menu_opciones():
  print("===========================================================")
  print("Bienvenido al programa de organizador de compuestos.")
  print("\nIngrese la opción que desea usar:    ")
  print(Fore.LIGHTWHITE_EX, "1. Mostrar Dataframe de compuestos")
  print(Fore.LIGHTWHITE_EX, "2. Mostrar PieChart de tipos de compuestos")
  print(Fore.LIGHTWHITE_EX, "3. Mostrar Barras de cantidad compuestos ")
  print(Fore.LIGHTWHITE_EX, "4. Salir del programa ")
  print("===========================================================")
  #opcionMenu = int(input("Por favor digite la opción del menú que desea usar:"))
  opcionMenu = 2

  while opcionMenu > 4 or opcionMenu < 1:
    print(Fore.LIGHTRED_EX, "¡Opción escogida no esta en la lista indicada!")
    print(Fore.LIGHTWHITE_EX, "")
    opcionMenu = int(input("Por favor digite la opción del menú que desea usar:"))

  return opcionMenu