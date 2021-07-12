""" Modulo Listas
    Funciones para practicas con listas
    Oscar Estrada Suazo
    Mayo 25-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def suma_acumulativa(lista_numeros):
  valor = 0 
  for x in range(0,int(len(lista_numeros))):
    #print("Cantiad Lista:",len(lista))
    num1 = 0
    for x in range(0,len(lista_numeros)):
        suma = num1 + lista_numeros[x]
        lista_numeros[x] = suma
        num1 = lista_numeros[x]
        #print(lista[x])
    #print("Lista_acumuladas=", lista_numeros)
    return lista_numeros

def traductor_pig_latin(lista_palabras):
  #convierte texto a minusculas
  lista_palabras = lista_palabras.lower()
  #Valida si es vocal o consonante
  if lista_palabras[0] == "a" or lista_palabras[0] == "e" or lista_palabras[0] == "i" or lista_palabras[0] == "o" or lista_palabras[0] == "u":
    #Traduce la palabra cuadno es vocal
    lista_palabras =  lista_palabras + "yay"
    #print(lista_palabras)
  else:
    #Traduce la palabra cuadno es consonante
    letra = lista_palabras[0]
    lista = list(lista_palabras)
    lista.remove(lista[0])
    lista.insert(len(lista) ,letra)
    lista_palabras = "".join(lista)
    lista_palabras =  lista_palabras + "yay"
    #print(lista_palabras)
    
  return lista_palabras

def identificador_frutas(lista_frutas):
  frutas_vitaminaA = []
  for x in range (0, len(lista_frutas)):
      fruta = lista_frutas[x].lower()
      if fruta.find("a") >= 0:
          frutas_vitaminaA.insert(x, lista_frutas[x])
      else:
          print(fruta, "NO tiene vitamina A")

  return frutas_vitaminaA

def son_palindromos(frase_uno, frase_dos):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"
