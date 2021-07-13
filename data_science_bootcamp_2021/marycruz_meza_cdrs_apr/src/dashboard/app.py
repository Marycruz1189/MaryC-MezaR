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
from utils import dashboard_tb as dash
#import utils.dashboard_tb as dash
path = os.path.abspath(__file__)

st.set_option('deprecation.showPyplotGlobalUse', False)

dash.configuracion()

menu = st.sidebar.selectbox('Menu:',
                            options=["No selected", "Welcome", "Visualization", "Flask_API" , "Model Prediction", "“Models From SQL Database”" ])

st.title("CLASIFICACIÓN Y DETECCIÓN DE RESIDUOS SÓLIDOS")

if menu == 'Welcome':
    dash.menu_inicio()

if menu == 'Visualization':

    fullpath1 = (dir(src_path) + os.sep+ "resources" + os.sep + "imagenes.png")
    image = Image.open(fullpath1)
    st.image (image,use_column_width=True)

if menu == 'Flask_API':
    dash.menu_api()

#if menu == 'Model Prediction':

