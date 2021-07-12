from colorama import Fore
import collections as colle
print("---------------------------------------------------------------")
print("                   INICIO DE PROGRAMA")
print("---------------------------------------------------------------")

cadena = input("Ingrese la cadena de dispositivos IoT:")
#cadena = "sensor,humedad,ON@electricos,luces,OFF@alarma,movimiento,OFF"
lista_dispositivosIoT = cadena.split("@")
lista_IoTON = []
lista_IoTOFF = []
DispositivoIoT = colle.namedtuple('DispositivoIoT', 'tipo identificador estado')

for x in range (0, len(lista_dispositivosIoT)):
    lista_datosIoT = lista_dispositivosIoT[x].split(",")
    datos_IoT = DispositivoIoT(tipo=lista_datosIoT[0], identificador=lista_datosIoT[1], estado=lista_datosIoT[2])
    if datos_IoT.estado == "ON":
        lista_IoTON.insert(x, datos_IoT)
    else:
        lista_IoTOFF.insert(x, datos_IoT)

print("---------------------------------------------------------------")
print("                   REPORTES DE DISPOSITIVOS")
print("---------------------------------------------------------------")   
print(Fore.LIGHTCYAN_EX, "\n DISPOSITIVOS ENCENDIDOS:", len(lista_IoTON))
for x in lista_IoTON:
    print("Tipo dispositivo: {} // Dispositivo IoT: {}".format(*x))

print(Fore.LIGHTGREEN_EX, "\n DISPOSITIVOS APAGADOS:", len(lista_IoTOFF))
for x in lista_IoTOFF:
    print("Tipo dispositivo: {} // Dispositivo IoT: {}".format(*x))


print("---------------------------------------------------------------")