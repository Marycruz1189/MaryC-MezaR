# This file represents your module.
# Write the code...
import pandas as pd
import numpy as np

def mean_visualization():
    """Draw the mean in a plot"""
    return None

def show_list_of_elements(lista):
    # TODO 
    pass


if __name__ == '__main__':
    x = mean_visualization()
    print(x)

##23 /05 / 2021

# Función para acceder a URLS que estan dentro de una API

def get_info(url):
    lista_vacia = []
    peticion_api_url = requests.get(url).json()
    lista_keys = ["height","id","order","weight","types"]
    for key in lista_keys:
        lista_vacia.append(peticion_api_url[key])
    return pd.Series(lista_vacia)
        

df[["height","id","order","weight","types"]] = df['url'].apply(lambda x:get_info(x))

# Para conocer los elementos (elements_by_tag) en un web scraping
for i in range(0, len(elements_by_tag)):
    print(elements_by_tag[i].text)


#funcion para eliminar argumentos

def ejercicio_3(arg1):
    valor_borrar = (" ")
    
    for elem in arg1:
        if '' in elem:
            lista = list(arg1)
            lista.remove((''))
            print(tuple(arg1))


# Funcion reverse numbers
def reverse_numbers(cadena, n):
    cont = -1
    cadena_al_reves = ""
    for i in range(len(cadena)):  
        cadena_al_reves = cadena_al_reves + cadena[cont] + str(n)
        cont -= 1  
    return cadena_al_reves

x = reverse_numbers(cadena="cadena", n=4)
x