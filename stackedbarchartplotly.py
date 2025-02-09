import dash
from dash import dcc, html
import plotly.graph_objs as go

# Initialize Dash app
app = dash.Dash(__name__)

# Data from your example (replace with actual values when integrating)
sentiment_data = {
    'categories': ['Category1', 'Category2', 'Category3', 'Category4', 'Category5'],
    'positive': [120, 150, 200, 180, 220],
    'neutral': [50, 70, 100, 90, 80],
    'negative': [30, 40, 60, 50, 40]
}

# Create the traces for the bar chart
trace_positive = go.Bar(
    x=sentiment_data['categories'],
    y=sentiment_data['positive'],
    name='Positive',
    marker=dict(color='green')
)

trace_neutral = go.Bar(
    x=sentiment_data['categories'],
    y=sentiment_data['neutral'],
    name='Neutral',
    marker=dict(color='blue')
)

trace_negative = go.Bar(
    x=sentiment_data['categories'],
    y=sentiment_data['negative'],
    name='Negative',
    marker=dict(color='red')
)

# Layout configuration for the dashboard
layout = go.Layout(
    barmode='stack',
    title='Sentiment Distribution by Rating Groups (Top 5 Categories)',
    xaxis={'title': 'Categories'},
    yaxis={'title': 'Number of Reviews'}
)

# Create the figure
fig = go.Figure(data=[trace_positive, trace_neutral, trace_negative], layout=layout)

# Define the layout of the Dash app
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1("Sentiment Distribution by Rating Groups", style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#4CAF50', 'color': 'white'})
            ]
        ),
        html.Div(
            children=[
                dcc.Graph(figure=fig)
            ],
            style={'width': '80%', 'margin': '40px auto', 'background': 'white', 'padding': '20px', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
