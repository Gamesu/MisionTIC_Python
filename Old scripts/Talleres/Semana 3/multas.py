""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Oscar Estrada Suazo
    Mayo 20-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(velocidad):
  #TODO: Documentar función 
    if velocidad >= 1 and velocidad <= 20:
        texto_multa =  "Llamado de atención por baja velocidad"
        pruebaAlcoholemia = False
    else:
        if velocidad >= 21 and velocidad <= 60:
            texto_multa =  "Normal, NO hacer multa"
            pruebaAlcoholemia = False
        else:
            if velocidad >= 61 and velocidad <= 80:
                texto_multa =  "Llamado de atención por alta velocidad"
                pruebaAlcoholemia = False
            else:
                if velocidad >= 81 and velocidad <= 120:
                    texto_multa =  "--> Multa tipo I"
                    pruebaAlcoholemia = True
                else:
                    texto_multa =  "Multa tipo II e inmovilización del vehículo"
                    pruebaAlcoholemia = True

    return texto_multa, pruebaAlcoholemia

def multar_alcoholemia(grado_alcohol):
#TODO: Documentar función 
    if grado_alcohol >= 20 and grado_alcohol <= 39:
        multa_alcoholemia = "--> suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
    else:
        if grado_alcohol >= 40 and grado_alcohol <= 99:
            multa_alcoholemia = "--> suspensión de la licencia de conducción entre uno (1) y tres (3) años."
        else:
            if grado_alcohol >= 100 and grado_alcohol <= 149:
                multa_alcoholemia = "* Suspensión de la licencia entre tres (3) y cinco (5) años y Curso de sensibilización por un mínimo de cuarenta (40) horas"
            else:
                multa_alcoholemia = "* Suspensión de la licencia entre cinco (5) y diez (10) años y Curso de sensibilización por un mínimo de ochenta (80) horas"

    return multa_alcoholemia


