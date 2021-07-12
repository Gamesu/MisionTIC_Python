""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada como entrada una cadena de caracteres 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Estrada Suazo
    Mayo 20-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc
from colorama import Fore

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def parser_cadena(cadena_entrada):
    #TODO: codigo que obtiene los numeros y el operando
    buscarEspacio = cadena_entrada.find(" ")
    numero_uno = cadena_entrada[0 : buscarEspacio]
    cadena_entrada = cadena_entrada[buscarEspacio + 1 : len(cadena_entrada)]
    buscarEspacio = cadena_entrada.find(" ")
    numero_dos = cadena_entrada[buscarEspacio + 1 : len(cadena_entrada)]
    operador = cadena_entrada[0]    
    
    return numero_uno, numero_dos, operador

#Valida tipo de operación que desea realziar el usuario y envia datos
def operar_numeros(num_uno, num_dos, operacion):
    num_uno = float(num_uno)
    print(num_uno, num_dos)
    if operacion == "+":
        #suma
        resultado = calc.sumar_numeros(num_uno, num_dos)
    else:
        if operacion == "-":
            #resta
            resultado = calc.restar_numeros(num_uno, num_dos)
        else:
            if operacion == "*":
                #multiplicacion
                resultado = calc.multiplicar_numeros(num_uno, num_dos)
            else:
                #division
                resultado = calc.dividir_numeros(num_uno, num_dos)

    return resultado

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
#TODO: Leer cadena de entrada
#cadena_entrada = input("Ingrese la operación que desea realziar: ")
cadena_entrada = "20 * 0"
num_1,num_2,op= parser_cadena(cadena_entrada)
#se valida si el segundo numero es cero
num_2 = float(num_2) 
if num_2 <= 0 and op == "/":
    print(Fore.LIGHTRED_EX + "El valor del segundo operando es incorrecto por favor ingrese uno diferente")
else:      
    resultado = operar_numeros(num_1, num_2, op)
    print(Fore.LIGHTCYAN_EX, "El resultado de la operación es:", resultado)

#TODO: terminar programa 

