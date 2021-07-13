
import streamlit as st
from PIL import Image
import pandas as pd
import os
import sys
dir = os.path.dirname
import requests
dir = os.path.dirname
src_path = dir(dir(os.path.abspath(__file__)))
sys.path.append(src_path)

#src_path = (dir(dir(__file__)))
#sys.path.append(src_path)
import utils.dashboard_tb as dash
path = os.path.dirname(__file__)
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
#import utils.visualization_tb as vis

st.set_option('deprecation.showPyplotGlobalUse', False)

dash.configuracion()

menu = st.sidebar.selectbox('Menu:',
                            options=["No selected", "Welcome", "Visualization", "Flask_API" , "Model Prediction", "“Models From SQL Database”" ])

st.title("CLASIFICACIÓN Y DETECCIÓN DE RESIDUOS SÓLIDOS")
# img = Image.open( dir(dir(path)) + os.sep + 'resources' + os.sep+ 'waste.jpg')
#st.image(img,use_column_width=True)

if menu == 'Welcome':
    dash.menu_inicio()
    
        
if menu == 'Visualization':
    ft.menu_data()
    
if menu == 'Flask_API':
    ft.menu_api()

if menu == 'Model Prediction':
    ft.menu_api()

if menu == 'Models From SQL Database':
    ft.menu_api()


    
 




