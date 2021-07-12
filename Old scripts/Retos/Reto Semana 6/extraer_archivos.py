def extraer_archivos(archivo,control):
  # archivo: string con ruta de archivo
  # control: r,w,a 
  archivo = open(archivo, control)
  resultado = list()

  for registro in archivo:
    registro = registro.splitlines()
    resultado.append(registro[0])

  archivo.close()
  return resultado

