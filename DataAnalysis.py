#Data Analysis imports
import pandas as pd
import pandas_profiling as pp
from pandas_profiling.config import Report

# Visualization Imports
import seaborn as sns
color = sns.color_palette()
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.express as px
#Import the CSV dataset file
fn='ExampleDataSet.csv'
df = pd.read_csv(fn)
varL={ 
    'x':[],
    'y':[],
    'z':[],
}
#Data analysis report creation
def report():
    #With pandas profilling creete the Data report
    global df
    df= pd.read_csv(fn)
    profile = pp.ProfileReport(df, title="Pandas Profiling Report", minimal=True, explorative=True) 
    profile.to_file("Report.html") #Save the date report in a HTML file
    #Creation of the correlation matrix graphic with pandas that display all the variables
    dfNew = df.corr() 
    fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew))) 
    global varL
    varL=df_to_plotly(dfNew)
    with open('CorrelationMatrix.html', 'w') as f1: #Exporting the graphic to a HTML
        print(fig.to_html(), file=f1)

#From the analysis report, creation of the variables
def df_to_plotly(df):
    #Take the dataset information and assign it to the Plotly axes
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist()}

#Dot graphic creation xi vs yi
def dotGraphic(xi,yi):
    fig = px.scatter(df, x=xi, y=yi)
    fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5)
    fig.update_layout(title_text=f'{xi} vs {yi} dot graphic')
    with open(f'dotGraphic[{xi}]vs[{yi}].html', 'w') as f2:
        print(fig.to_html(), file=f2)

