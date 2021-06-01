import streamlit as st
from PIL import Image
import pandas as pd
import os 
import requests
path = os.path.dirname(__file__)
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import utils.visualization_tb as vis
st.set_option('deprecation.showPyplotGlobalUse', False)

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
    url= "http://localhost:6060/token_id?token_id=Y4290783D"
    json_api = requests.get(url).json()
    st.write(json_api)

def menu_graphs():
    
    csv_path = dir(dir(path)) + os.sep + 'reports' + os.sep+'waste_management_cleaned.csv'
    df = pd.read_csv(csv_path)
    st.pyplot(vis.graph_analysis_disposal(df))
   

#def menu_project():
    #st.title("Hypothesis")
    #st.write("The development of societies and population growth, among other things, influence the increase in municipal solid waste generation.  The world's population is growing by leaps and bounds, projected to reach 8.5 billion by 2030, 9.7 billion by 2050 and 11.2 billion by 2100 (United Nations, 2019).Similarly, global environmental indicators show that more waste is being generated over time, creating environmental problems in urban ecosystems, especially because of the challenge faced by governments in the management and disposal of such waste. According to a report presented by the World Bank in 2017 (2018), 2010 million tonnes of MSW are generated annually in the world, and an important fact to highlight is that at least 33% of this waste is managed at risk to the environment. Therefore, the hypothesis of this project is: Population growth and economic development generate an increase in the production of solid waste.")
    #img = Image.open( dir(dir(path)) + os.sep + 'resources' + os.sep+ 'correlation_variables.png')
    #st.image(img,use_column_width=True)




