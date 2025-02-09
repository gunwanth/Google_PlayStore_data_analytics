import dash
from dash import dcc, html
import plotly.graph_objs as go

app = dash.Dash(__name__)

grouped_data = {
    'categories': ['Category1', 'Category2', 'Category3', 'Category4', 'Category5'],
    'avg_rating': [4.5, 4.2, 4.8, 4.1, 4.6],
    'total_reviews': [1500, 2000, 1200, 1800, 1600]
}

trace_avg_rating = go.Bar(
    x=grouped_data['categories'],
    y=grouped_data['avg_rating'],
    name='Average Rating',
    marker=dict(color='orange')
)

trace_total_reviews = go.Bar(
    x=grouped_data['categories'],
    y=grouped_data['total_reviews'],
    name='Total Reviews',
    marker=dict(color='purple')
)

layout = go.Layout(
    barmode='group',
    title='Average Rating and Total Reviews (Top Categories)',
    xaxis={'title': 'Categories'},
    yaxis={'title': 'Values'}
)

fig = go.Figure(data=[trace_avg_rating, trace_total_reviews], layout=layout)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    "Average Rating and Total Reviews",
                    style={
                        'textAlign': 'center',
                        'padding': '20px',
                        'backgroundColor': '#007BFF',
                        'color': 'white'
                    }
                )
            ]
        ),
        html.Div(
            children=[
                dcc.Graph(figure=fig)
            ],
            style={
                'width': '80%',
                'margin': '40px auto',
                'background': 'white',
                'padding': '20px',
                'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
