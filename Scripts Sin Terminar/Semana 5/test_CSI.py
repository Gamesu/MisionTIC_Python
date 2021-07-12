#mensaje = "Llamar después de las 12:15 al teléfono 1-800-329-8044"
mensaje = "A"

mensajeSplit = mensaje.strip()
#print(mensajeSplit)
for x in range(0, len(mensaje)):
    print(mensaje[x])
    print(str.isdigit(mensaje[x]))

#Llamar después de las 12:15 al teléfono 1-800-329-8044
#Llamar después de las 98:90 al teléfono 9-255-781-2566
"""
def imprimir(paises):
    for clave in paises:
        #print(clave, paises[clave])
        print(clave)


# bloque principal

paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)
"""

dic_Codificado = {"1": 9, "2":8, "3":7, "4":6, "5":0, "6":4, "9":1, "8":2, "7":3, "0":5}
men = "9"

print(dic_Codificado[men])