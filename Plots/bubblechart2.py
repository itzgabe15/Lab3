import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Creating max, min, and mean cases group by Month Column
new_df = df.groupby(['month']).agg(
    {'average_max_temp': 'max', 'average_min_temp': 'min', 'actual_mean_temp': 'mean'}).reset_index()

# Preparing data
data = [
    go.Scatter(x=new_df['average_max_temp'],
               y=new_df['average_min_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['actual_mean_temp'] / 1,color=new_df['actual_mean_temp'] / 1, showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Max/Min Temperatures Throughout The Months', xaxis_title="Average Max Temp",
                   yaxis_title="Average Min Temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart2.html')