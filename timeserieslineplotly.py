import pandas as pd
import plotly.express as px

data = pd.read_csv("Merged_Data (1).csv")

data['Last Updated'] = pd.to_datetime(data['Last Updated'])
data = data[data['Installs'] > 10000] 
data = data[data['Content Rating'] == 'Teen'] 
data = data[data['App'].str.startswith('E')]  


data['Month'] = data['Last Updated'].dt.to_period('M')
monthly_installs = data.groupby(['Month', 'App Category'])['Installs'].sum().reset_index()
monthly_installs['Month'] = monthly_installs['Month'].dt.to_timestamp()

fig = px.line(
    monthly_installs,
    x="Month",
    y="Installs",
    color="App Category",
    title="Time Series: Total Installs Over Time by App Category",
    labels={"Installs": "Total Installs", "Month": "Time"},
    line_shape="spline",
)

monthly_installs['MoM Growth'] = monthly_installs.groupby('App Category')['Installs'].pct_change() * 100
significant_growth = monthly_installs[monthly_installs['MoM Growth'] > 20]

fig.add_scatter(
    x=significant_growth['Month'],
    y=significant_growth['Installs'],
    mode='markers',
    marker=dict(color='red', size=8),
    name="Significant Growth",
)

fig.show()