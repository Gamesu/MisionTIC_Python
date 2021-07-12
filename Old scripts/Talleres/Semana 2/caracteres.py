nombre = "Fe(OH)3"
nombre = nombre.partition("(OH)")
print(nombre) #['Fe', '(OH)', '3']
print(len(nombre))
#print(nombre[9])
x = 0
while x <= len(nombre):
    if nombre[x] == "(OH)":
        print(nombre[x])
        x = x + 1
    else:
        print("NO es")
        x = x + 1

"""
x = 0
while x <= len(nombre):
    print(nombre[x])
    x = x + 1
"""