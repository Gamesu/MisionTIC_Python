frase_uno = "Anula la luz azul a la luna"
frase_dos = ""


"""
lista_frutas = ["Pera", "Mango", "lUlo", "KiWi", "PapaYa"]
frutas_vitaminaA = []
for x in range (0, len(lista_frutas)):
    fruta = lista_frutas[x].lower()
    if fruta.find("a") >= 0:
        #print(fruta, "tiene vitamina A")
        frutas_vitaminaA.insert(x, lista_frutas[x])
    else:
        #frutas_vitaminaA.remove(x)
        print(fruta, "NO tiene vitamina A")

print(frutas_vitaminaA)
"""
"""
palabra = "Maaaab"
palabra = palabra.lower()
#print(palabra)
if palabra[0] == "a" or palabra[0] == "e" or palabra[0] == "i" or palabra[0] == "o" or palabra[0] == "u":
    palabra =  palabra + "yay"
    print(palabra)
else:
    letra = palabra[0]
    lista = list(palabra)
    lista.remove(lista[0])
    lista.insert(len(lista) ,letra)
    palabra = "".join(lista)
    palabra =  palabra + "yay"
    print(palabra)
"""


"""
lista=[4, 3, 6, 10]
lista_acumulada = []
#print("Cantiad Lista:",len(lista))
num1 = 0
for x in range(0,len(lista)):
    suma = num1 + lista[x]
    lista[x] = suma
    num1 = lista[x]
    #print(lista[x])
print("Lista_acumuladas=", lista)

"""


#for x in range(101):
#    print(x)

#longitud = int(5)
#print(longitud%2)