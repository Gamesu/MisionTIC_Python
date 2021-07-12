def extraer_archivos(archivo,control):
  # archivo: string con ruta de archivo
  # control: r,w,a 
  archivo = open(archivo, control)
  #contenido = archivo.read()
  lista = list()

  #for x in range(0, len(archivo)):
  for registro in archivo:
    registro = registro.split(" ") # ['compuesto', '2', 'HCl', '14\n']
    if registro[0] == 'compuesto':
      datoCantidad = registro[3].splitlines()
      registro[3] = datoCantidad[0]
      registroArch = registro[0] + " " + registro[1] + "\t" + registro[2] + "\t" + registro[3]
      lista.append(registroArch)
      #cantidad = registro[3].splitlines()
    else:
      registroArch = registro[0] + " " + registro[1] + " " + registro[2] + " " + registro[3] + " " + registro[4]
      lista.append(registroArch)
    
  for dato in lista:
    print(dato)

  archivo.close()
  #print(lista)
  #return resultado

#compuesto 2\tHCl\t14
#compuesto 2\tHCl\t14\n
compuestos = extraer_archivos("acidos.txt","r")
#cantidades = extraer_archivos("cantidades.txt", "r")
