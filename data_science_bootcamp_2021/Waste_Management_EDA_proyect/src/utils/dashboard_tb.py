import streamlit as st
from PIL import Image
import pandas as pd
import os 
path = os.path.dirname(__file__)

def configuracion():
    st.set_page_config(page_title='Waste Management', page_icon=':electric_plug:', layout="wide")

def menu_home():
    st.title('¡Welcome to the EDA project Waste Management in Spain')
    st.write('WHAT A WASTE: A national review of solid waste management')
   

def menu_data():    
    dir = os.path.dirname
    path = os.path.dirname(__file__)
    csv_path = dir(dir(path)) + os.sep + 'reports' + os.sep+'waste_management_cleaned.csv'
    df = pd.read_csv(csv_path)
    st.dataframe(df)
    
def menu_api(): 
    st.write("http://localhost:6060/token_id?token_id=Y4290783D")
     
    #dir = os.path.dirname
    #path = os.path.dirname(__file__)
    #csv_path = dir(dir(path)) + os.sep + 'reports' + os.sep+'waste_management_cleaned.json'
    #df = pd.read_json(csv_path)
    #st.dataframe(df)



