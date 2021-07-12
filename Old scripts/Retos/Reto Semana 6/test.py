import collections

nombre = 'pepe'
edad = 28
genero = "M"
lista = []
#tuplaFInal = collections.namedtuple('datosPersona', 'nombre, edad, genero')
tuplaFInal = (nombre, edad, genero)
print(tuplaFInal)
#tupla = tuplaFInal(nombre=nombre, edad=edad, genero=genero)
lista.insert(0, tuplaFInal)
nombre = "JULIAN"
tuplaFInal = (nombre, edad, genero)
lista.insert(1, tuplaFInal)

print(lista)
print()
#print(tupla[0], tupla[1], tupla[2])