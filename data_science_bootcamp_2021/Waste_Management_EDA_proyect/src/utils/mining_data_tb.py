#that contains the generic 
# functionality related to open, create, read and 
# write ﬁles.



def read_databases():
    
    """ Function to read the 5 databases """
    import os
    SEP = os.sep
    dir = os.path.dirname
    #global csv_fullpath_gdp
    csv_fullpath_gdp = dir(os.getcwd()) + SEP + "data" + SEP + "PIBcorriente_milesdeeuros.xlsx"
    #global csv_fullpath_d
    csv_fullpath_d = dir(os.getcwd()) + SEP + "data" + SEP + "residuos_gestionados_nuevo.xlsx"
    #global csv_fullpath_popu
    csv_fullpath_popu = dir(os.getcwd()) + SEP + "data" + SEP + "poblacion.xls"
    #global csv_fullpath_c
    csv_fullpath_c = dir(os.getcwd()) + SEP + "data" + SEP + "recogida_residuos.xls"
    #global csv_fullpath_e
    csv_fullpath_e = dir(os.getcwd()) + SEP + "data" + SEP + "total contaminantes nacional.xlsx"
    return csv_fullpath_gdp, csv_fullpath_d, csv_fullpath_popu, csv_fullpath_c, csv_fullpath_e
    
if __name__ == '__main__':
    read_databases()



    #return gdp, population, waste_disposal, waste_collection, waste_emissions

#VER EN ESTA FUNCION CLEAN SI AL HACER REFERENCIA A READ DATABASE
#DEBO ESPECIFICAR ALGUNO DE LOS ELEMENTOS QUE USO DEL RETORNAR LA FUNCION

def clean_years(gdp, population):
    to_drop = gdp.iloc[:, 1:11]
    gdp.drop(to_drop, inplace = True , axis= 1 )

    to_drop_1  = ['2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997', '1996']
    population.drop(to_drop_1, inplace = True , axis= 1 )
    return gdp, population


#def melt_gdp(clean_years= gdp):
#     clean_gdp = pd.melt(clean_years, id_vars=['Comunidad Autónoma'], 
#     value_vars=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
#     var_name='Año', value_name='PIB').sort_values('Comunidad Autónoma')
#     return clean_gdp

# def melt_population(clean_years=population):
#     clean_population = pd.melt(clean_years, id_vars=['Comunidad Autónoma'], value_vars=['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', 2018],var_name='Año', value_name='Poblacion').sort_values('Comunidad Autónoma')
#     return clean_population

# def save_clean_files():
#     """Function that returns all clean files """


# def capitalize_ac():
# #CHANGE TO CAPITALIZE ALL the column CCAA esto se aplica para todas 
#     melt_pib['Comunidad Autónoma'] = melt_pib['Comunidad Autónoma'].str.upper()

# def re_index():
# #reiniciar el index esa se puede aplicar para todas 
#     pib_clean = melt_pib.reset_index(drop=True)