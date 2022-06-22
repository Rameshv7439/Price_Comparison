import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('data/smartphone.csv')
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

fig = px.bar(x, x='Brand', y='Model', color = 'Brand', title = 'Number of Models by Brands')
fig.show()

y = df.groupby('Brand')[['Rating']].mean().sort_values(ascending=False,by='Rating')
y.reset_index(inplace=True)
fig = px.bar(y, x='Brand', y='Rating', color = 'Brand', title = 'Average Rating of Models of Brands')
fig.show()

df2 = df.groupby('Brand')[['Selling Price']].mean().sort_values(ascending=False,by='Selling Price')
df2 = df2.reset_index()
fig = px.bar(df2, x='Brand', y='Selling Price', color = 'Brand', title = 'Average Selling Price of Phones by Brands')
fig.show()