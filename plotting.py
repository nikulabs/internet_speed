import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('/home/brn/speedtest.csv')

#fig = make_subplots(specs=[[{"secondary_y": True}]])
#fig.add_trace(go.Scatter(x = df['Timestamp'], y = df['Download'],
#                  name='Download speed over time'))

#fig.update_layout(title='Apple Share Prices over time (2014)',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)

#fig.show()
fig = px.line(df, x = 'Timestamp', y = 'Download', title='Download speed over time(Dec 2019)')
fig.show()
