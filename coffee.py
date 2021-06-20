import pandas as pd
import plotly.express as px
import  statistics
import numpy as np

df_graph = pd.read_csv("cups of coffee vs hours of sleep.csv")

fig = px.scatter(x = 'Coffee in ml' , y = 'Sleep in hours')
fig.show()

def corr(list_x,list_y):
    c = np.corrcoef(x=[list_x],y = [list_y])
    return c[0][1]

c = corr(df_graph['Coffee in ml'].tolist(),df_graph['sleep in hours'].tolist())
print(c)
