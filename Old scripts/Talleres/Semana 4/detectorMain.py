# Oscar Estrada
# 26/05/2021
from colorama import Fore
import detector_virus as virus
#===========================================================
# Ejercicio Menú
#===========================================================
def capturar_muestra():  
    print("===========================================================")    
    print(Fore.LIGHTGREEN_EX, "--> Simulador de virus")
    print("Ingrese las secuencias genéticas a validar, sino va ingresar mas ingrese el valor cero")
    print("NOTA: Si no va ingresar mas ingrese el valor cero")
    print("===========================================================")
    #opcion = input("Por favor digite al opción del menu:")
    lista_muestra = ["vucS"]
    #lista_muestra = ["ravuS", "Peravus"]
    resultado = virus.validar_virus(lista_muestra)
    return resultado

#===========================================================
# Inicio del programa
#===========================================================
positivas, negativas =  capturar_muestra()
print("negativas:", negativas)
print("positivas:", positivas)

