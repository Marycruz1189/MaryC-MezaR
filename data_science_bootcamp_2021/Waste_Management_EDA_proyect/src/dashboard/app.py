
import streamlit as st
from PIL import Image
import pandas as pd
import os
import sys
dir = os.path.dirname
src_path = (dir(dir(__file__)))
sys.path.append(src_path)
import utils.dashboard_tb as ft
path = os.path.dirname(__file__)

ft.configuracion()

menu = st.sidebar.selectbox('Menu:',
                            options=["No selected", "Welcome", "Data", "Flask_API"])

st.title("WASTE MANAGEMENT SPAIN")
img = Image.open( dir(dir(path)) + os.sep + 'resources' + os.sep+ 'waste.jpg')
st.image(img,use_column_width=True)

if menu == 'Welcome':
    ft.menu_home()
    #st.title('¡Welcome to the EDA project Waste Management in Spain')
    #st.write('WHAT A WASTE: A national review of solid waste management')
    
if menu == 'Data':
    ft.menu_data()
    #st.dataframe(df)
   
    #dir = os.path.dirname
    #path = os.path.dirname(__file__)
    #csv_path = dir(dir(path)) + os.sep + 'data' + os.sep+'waste_management_cleaned.csv'
if menu == 'Flask_API':
    #ft.menu_api()
    st.write("http://localhost:6060/token_id?token_id=Y4290783D") 


    
    #df = pd.read_csv(csv_path)
    #st.dataframe(df)
    #SEP = os.sep
    #dir = os.path.dirname
    #csv_path = dir(dir(dir(os.getcwd()))) + SEP + "data" + SEP + "waste_management_cleaned.csv"
    #df = ft.menu_data(csv_path)

    
   # ft.menu_data(df)
    #SEP = os.sep
    #dir = os.path.dirname
    #csv_path = dir(os.getcwd()) + SEP + "data" + SEP + "waste_management_cleaned.csv"
    #df = ft.cargar_datos(csv_path)
    #df = pd.read_csv(df)





