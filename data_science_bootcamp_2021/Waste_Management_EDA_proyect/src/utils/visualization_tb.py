import seaborn as sns
import matplotlib.pyplot as plt 
import os, sys
dir = os.path.dirname
src_path = dir(__file__)
sys.path.append(src_path)
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mining_data_tb import *

def Outliers(waste_management):
    import seaborn as sns
    outliers = sns.boxplot(x=waste_management['Total Waste-C'])
    return outliers


def econo_distribution(waste_management):
    econodis= waste_management.hist(column=["Population", "GDP", 'Total(tons/day)'], color = 'lightblue', edgecolor = 'black', bins=5)
    plt.xticks(rotation=-45)
    plt.title("Distribution of economical variables")
    plt.show()
    return econodis

def collection_distribution(waste_management):
    collectiondis = waste_management.hist(column=['Domestic Waste and Wheelie Bins -C', 'Metallics waste-C', 'Waste Glass-C', 'Waste Paper and Cardboard-C', 'Plastics-C'], color = 'blue', edgecolor = 'black', bins=5)
    plt.title("Distribution of collection variables")
    #plt.show()
    return collectiondis

def disposal_distribution(waste_management):
    disposaldis = waste_management.hist(column=['Recycling collection-D', 'Mixed Recovered Mater-D',
       'Composting/anaerobic digestion FORS-D',
       'Composting/anaerobic digestion-D', 'Incinerated-D',
       'Landfill of rejects', 'Landfill without pre-treatment-D'], color = 'lightgreen', edgecolor = 'black', bins=5)
    plt.title("Distribution of disposal variables")
    return disposaldis

def distribution_totalwaste(waste_management):
    distotalwaste = sns.distplot(waste_management['Total Waste-C'], color='g', bins=100, hist_kws={'alpha': 0.4});
    plt.title("Distribution of total waste")
    return distotalwaste


def processed_waste(waste_management):
    processed = sns.kdeplot(waste_management['Processed_waste'])
    return processed
            
def not_processed_waste(waste_management):
    notprocessed = plt.boxplot(waste_management['Processed_waste'])
    plt.title("Distribution of not processed waste")
    return notprocessed


def comparative_scatter(waste_management):
    import seaborn as sns                       
    import matplotlib.pyplot as plt 
    fig, ax = plt.subplots(figsize=(10,6))
    fig = ax.scatter(waste_management['Total(tons/day)'], waste_management['Population'])
    ax.set_xlabel('Total(tons/day)')
    ax.set_ylabel('Population')
    #plt.show()
    return fig

def most_generation_graph(waste_management):
    import seaborn as sns 
    import matplotlib.pyplot as plt
    ccaa = waste_management.groupby('Autonomous communities').sum()
    ccaa_sorted = ccaa.sort_values('Total(tons/day)', ascending = False)[1:11]
    ccaa_sorted['Total(tons/day)']
    mostgenration= plt.bar(ccaa_sorted['Total(tons/day)'].index, ccaa_sorted['Total(tons/day)'].values,\
            width = 0.5, color = ['b', 'orange', 'r', 'c', 'm', 'y', 'pink', 'lightblue', 'grey', 'g'])
    plt.xticks(rotation = 90) 
    plt.xlabel('CCAA')
    plt.ylabel('Total(tons/day)')
    plt.title('10 CCAA with more waste generation')
    #plt.show()
    #return mostgenration

def most_disposal_graph(waste_management):
    import seaborn as sns 
    import matplotlib.pyplot as plt
    ccaadis = waste_management.groupby('Autonomous communities').sum()
    ccaa_sorted_dis = ccaadis.sort_values('Recycling collection-D', ascending = False)[1:11]
    ccaa_sorted_dis['Recycling collection-D']
    mostdisposal = plt.bar(ccaa_sorted_dis['Recycling collection-D'].index, ccaa_sorted_dis['Recycling collection-D'].values,\
            width = 0.5, color = ['lightcoral', 'green', 'silver', 'palegreen', 'navy', 'wheat', 'pink', 'lightblue', 'grey', 'peru'])
    plt.xticks(rotation = 90) 
    plt.xlabel('CCAA')
    plt.ylabel('Recycling collection-D')
    plt.title('10 CCAA with more waste-recovered')
    #plt.show()
    #return mostdisposal

# set the histogram, mean and median
def distribution_kgpercapita(waste_management):
    dispercapita = sns.distplot(waste_management['Per Capita(kg/capita/day)'], kde=False)
    plt.axvline(x=waste_management['Per Capita(kg/capita/day)'].mean(), linewidth=3, color='g', label="mean", alpha=0.5)
    plt.axvline(x=waste_management['Per Capita(kg/capita/day)'].median(), linewidth=3, color='y', label="median", alpha=0.5)
    # set title, legends and labels
    plt.xlabel("Per Capita(kg/capita/day)")
    plt.ylabel("Count")
    plt.title("Distribution of Per Capita(kg/capita/day)", size=14)
    plt.legend(["mean", "median"])
    #plt.show()
    #return dispercapita

def correlation_variables(waste_management):
    plt.figure(figsize=(10,5))
    features1=list(['GDP','Population','GDP per capita',  'Total mixed waste-C', 'Total separately waste-C (tn)',
        'Total Waste-C',
        'Total Waste disposal (tn)-D', 'Total(tons/day)',
        'Per Capita(kg/capita/day)'  ])
    c = waste_management[features1].corr()
    correlation = sns.heatmap(c,cmap="BrBG",annot=True)
    #return c, correlation

def graph_analysis_disposal(waste_management):
    mean = waste_management[['Processed_waste', 'Not Processed_waste']]
    graphanalysis = sns.boxplot(data = mean)
    plt.title('Distribution of type disposal')
    plt.xticks(rotation=-45);
    #return graphanalysis
# regression models
def correlation_gdp_kg(waste_management):
    gdpcorr = sns.regplot(x="GDP per capita", y="Per Capita(kg/capita/day)", data=waste_management).set(title='gdp percapita /kg dia')
    #return gdpcorr

def correlation_pop_tn(waste_management):
    correpoputn = sns.regplot(x="Population", y="Total(tons/day)", data=waste_management, scatter_kws={"color": "green"}, line_kws={"color": "gray"}).set(title='population /Total(tons/day)')
    #return correpoputn

def correlation_disposal(waste_management):
    corrdispo = sns.regplot(x="GDP", y="Processed_waste", data=waste_management, scatter_kws={"color": "black"}, line_kws={"color": "red"}).set(title='GDP /Processed_waste')
    #return corrdispo

def time_kgperday(waste_management):
    timeserie = waste_management.groupby('Year')['Per Capita(kg/capita/day)'].sum()
    plt.figure();
    kgtime = timeserie.plot();
    plt.title("Evolution by year kg/percapita/day")
    #return kgtime 


def time_disposal(waste_management):
    timeserie_dispo = waste_management.groupby('Year')['Processed_waste', 'Not Processed_waste'].mean()
    plt.figure();
    timedis = timeserie_dispo.plot();
    plt.title("Type of waste processing per year (tn)")
    #return timedis

def time_collected(waste_management):
    timeserie_collec = waste_management.groupby('Year')['Metallics waste-C', 'Waste Glass-C', 'Waste Paper and Cardboard-C', 'Plastics-C',
       'Waste Wood-C', 'Textile waste-C', 'Electrical waste-C', 'Battery-C'].mean()
    plt.figure();
    timecollec = timeserie_collec.plot();
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.title("Type of waste collected")
    #return timecollec

def time_typedisposal(waste_management):
    timeserie_disposaltype = waste_management.groupby('Year')['Recycling collection-D', 'Mixed Recovered Mater-D',
        'Composting/anaerobic digestion FORS-D',
        'Composting/anaerobic digestion-D', 'Incinerated-D',
        'Landfill of rejects', 'Landfill without pre-treatment-D'].mean()
    plt.figure();
    timeseriedis = timeserie_disposaltype.plot();
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.title("Type of disposal")
    #return timeseriedis


def spent_time():
    time = pd.DataFrame({'Time': [0.05, 0.40 , 0.15, 0.15, 0.15, 0.10 ],
                   'Task': ['Data Sourcing', 'Data wrangling', 'Exploratory Data Analysis', 'Flask', 'Streamlit','Presentation']})
    plot = time.plot.pie(y='Time', autopct='%1.2f%%',shadow=True, figsize=(5, 5))
    labels = 'Data Sourcing', 'Data wranling', 'Exploratory Data Analysis', 'Flask', 'Streamlit','Presentation'
    plt.legend(labels, bbox_to_anchor=(1,0), loc="lower right", 
                          bbox_transform=plt.gcf().transFigure)
    #return plot
