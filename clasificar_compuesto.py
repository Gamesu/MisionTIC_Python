import pandas as pd
import menu 
import matplotlib.pyplot as plt 

def clasificar_compuesto(compuestos):
  lista = list()
  pieLabels = ["Catión", "Anión", "Ácido", "Óxido", "Hidróxido"]
  
  #formula = compuestos.loc["compuesto 1", "Fï¿½rmula"]
  #formula = compuestos["Fï¿½rmula"]
  #formula = compuestos["Cantidad"]
  formula = compuestos.Cantidad
  print(formula)
  #cant = compuestos.value_counts()
  #print(cant)

  #plt.pie(lista, labels= pieLabels)
  #plt.show()