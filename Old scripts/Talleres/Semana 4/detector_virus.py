# Oscar Estrada
# 26/05/2021
def validar_virus(lista_muestra):
    muestras_positivas = []
    muestras_negativas = []
    lista_resultado = []

    #cuenta cantidad de muestras que esta en la lista
    for x in range(0, len(lista_muestra)):
        #virus = "coronavirus"
        #lista_muestra = ["vuS"]
        virus = "co"
        muestraPersona = lista_muestra[x].lower()
        muestraPersona = list(muestraPersona)
        lista_virus = list(virus)
        #sepera la muestra con el virus
        for y in range(0, len(lista_virus)):
            for z in range(0, len(muestraPersona)):
                virus = lista_virus[y]
                persona = muestraPersona[z]
                #valida si cumple con la prueba e inserta en lista
                if virus == persona:
                    lista_resultado.insert(z, True)
                    #break
                else:
                    lista_resultado.insert(z, False)

                print(virus, persona, lista_resultado)
    
    return muestras_positivas, muestras_negativas