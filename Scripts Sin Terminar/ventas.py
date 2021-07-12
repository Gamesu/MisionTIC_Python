""" Modulo Module ventas
    Funciones para el manejo de ventas mensuales
    con matrices
    Oscar Estrada Suazo
    Junio 10-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def leer_numero_empleados():
    codigosEmpleados = input("\n --- Ingrese los codigos de los empleados separadados por comas:")
    codigosEmpleados = codigosEmpleados.split(",")
    return codigosEmpleados

def leer_ventas_empleados_mes(plantilla, lista_empleados):
    for x in range(0, len(lista_empleados)):
      print("--- Ingrese las ventas del empleado", lista_empleados[x])
      ventasEmpleados = input("\n --- Ingrese las ventas de cada mes separadados por comas:")
      ventasEmpleados = ventasEmpleados.split(",")
      for y in range(0, 12):
          plantilla[x][y] = ventasEmpleados[y]
    return plantilla

def ordenar_vendedores_por_ventas(plantilla, lista_empleados):
    ventasVendedor = []

    for x in range(len(plantilla)):
        totalVentas = 0
        for y in range(len(plantilla[x])):
            totalVentas = totalVentas + int(plantilla[x][y])
        ventasVendedor.insert(x, totalVentas)
                
    return ventasVendedor

def calcular_cinco_vendedores():
    #TODO Comentar código
    #TODO Implementar la función
    return "No implementada aún"

def calcula_mes_mas_ventas():
    #TODO Comentar código
    #TODO Implementar la función
    return "No implementada aún"

def greficar_ventas_por_mes():
    #TODO Comentar código
    #TODO Implementar la función
    return "No implementada aún"