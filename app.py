import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor':'#0d1117', 'color':'#c9d1d9'}, children=[
    html.H1("Real-Time Sales Dashboard", style={'textAlign':'center', 'color':'#58a6ff'}),
    dcc.Graph(id='sales-trend'),
    dcc.Interval(
        id='interval-component',
        interval=5*1000,  # update every 5 seconds
        n_intervals=0
    )
])

@app.callback(
    Output('sales-trend', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    df = pd.read_csv('data/sales_data.csv')  # reload latest data
    fig = px.line(df, x='Date', y='Revenue', title='Revenue Over Time')
    fig.update_layout(plot_bgcolor='#161b22', paper_bgcolor='#0d1117', font_color='#c9d1d9')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
