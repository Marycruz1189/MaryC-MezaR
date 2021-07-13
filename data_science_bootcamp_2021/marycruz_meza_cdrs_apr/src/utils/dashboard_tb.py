import streamlit as st
from PIL import Image
import pandas as pd
import os 
import requests
import sys 
dir = os.path.dirname
path = os.path.abspath(__file__)
#src_path = dir(dir(os.path.abspath(__file__)))
#sys.path.append(src_path)



import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#import utils.visualization_tb as vis
st.set_option('deprecation.showPyplotGlobalUse', False)

def configuracion():
    st.set_page_config(page_title='Waste Management', page_icon=':electric_plug:', layout="wide")

def menu_inicio():
    
    st.write('Bienvenidos al sistema de clasificación y detección por tipos de residuos sólidos')
    st.write("""
        OBJETIVO:
        Implementar un sistema de reconocimiento 
        automatizado que utiliza un algoritmo de aprendizaje 
        profundo para clasificar los desechos por tipo de residuo. 
        La segregación eficiente de los desechos sólidos ayuda a
        reducir la cantidad de dispuestos incorrectamente, lo que 
        mejora la tasa de reciclaje y protege el suelo de la 
        contaminación

        PERFIL DEL AUTOR:
        Investigador de residuos sólidos
        """)


def menu_visualization():    
    fullpath = "C:\\Users\\Mary\\Desktop\\BootCamp\\Python\\MaryC-MezaR\\data_science_bootcamp_2021\\Machine_Learning_project\\resources\\"
    image = Image.open(fullpath)
    st.image (image,use_column_width=True)
    #fullpath = dir(dir(dir(os.path.abspath(__file__)))) + os.sep + 'reports' + os.sep + "data_cleaned.json"

 def menu_api(): 
    url= "http://localhost:6060/token_id?token_id=Y4290783D"
    json_api = requests.get(url).json()
    st.write(json_api)


   
   






