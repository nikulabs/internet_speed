import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('/home/brn/speedtest.csv')

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x = df['Timestamp'], y = df['Download'],
                  name='Download (bps)'), secondary_y=False)
fig.add_trace(go.Scatter(x = df['Timestamp'], y = df['Ping'],
                  name='Ping (msec)'), secondary_y=True)

fig.update_layout(title='Vodafone home internet connection',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="Speed", secondary_y=False)
fig.update_yaxes(title_text="Ping", secondary_y=True)

fig.show()
