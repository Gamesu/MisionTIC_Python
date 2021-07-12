""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Estrada Suazo
    Mayo 19-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  print("==================================================")
  print("| Menú")
  print("==================================================")
  print("| Ingresa un número para realizar la operación.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("| 4. Calcular división: (3)")
  print("==================================================")
  print("==================================================")
  opcion = int(input("Ingrese el número de la operación que desea realizar:"))
  
#Valida tipo de operación, sino esta en el menú arroja error
  if opcion > 0 and opcion < 5:
      return opcion
  else:
      opcion = 9999
      return opcion

  #return opcion
  
#Valida tipo de operación que desea realziar el usuario y envia datos
def operar_numeros(num_uno, num_dos, operacion):
    if operacion == 1:
        #suma
        resultado = calc.sumar_numeros(num_uno, num_dos)
    else:
        if operacion == 2:
            #resta
            resultado = calc.restar_numeros(num_uno, num_dos)
        else:
            if operacion == 3:
                #multiplicacion
                resultado = calc.multiplicar_numeros(num_uno, num_dos)
            else:
                #division
                resultado = calc.dividir_numeros(num_uno, num_dos)

    return resultado


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion = menu_operaciones()
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
#Valida que se halla seleccionado un opación valida
print("==================================================")
if operacion == 9999:
    print("No ha seleccionado una opción valida, por favor seleccione una opción valida")
else:
    #se valida si el segundo numero es cero
    num_uno = float(input("Ingrese el primer número a operar:"))
    num_dos = float(input("Ingrese el segundo número a operar:"))
    
    if num_dos <= 0 and operacion == 4:
        print("El valor del segundo operando es incorrecto por favor ingrese uno diferente")
    else:      
        resultado = operar_numeros(num_uno, num_dos, operacion)
        print("El resultado de la operación es:", resultado)

