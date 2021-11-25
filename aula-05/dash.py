import sqlite3
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Output, Input, Event
# import dash_core_components as dcc
# import dash_html_components as html
import plotly
import plotly.graph_objs as go
import random

app = dash.Dash()

app.layout = html.Div([html.H2('Análise de Sentimentos em Tempo Real'),
                       dcc.Input(id='sentiment-term', value='twitter', type='text'),
                       dcc.Graph(id='live-graph', animate=False),
                       dcc.Interval(
                            id='graph-update',
                            interval=1*1000
                       )

])

@app.callback(Output('live-graph', 'figure'),
              [Input(component_id='sentiment-term', component_property='value')],
             events=[Event('graph-update', 'interval')])
def update_graph_scatter(sentiment_term):
    try:
        conn = sqlite3.connect('twitter.db')
        c = conn.cursor()
        query = "SELECT * FROM sentiment WHERE tweet LIKE ? ORDER BY unix DESC LIMIT 1000"
        df = pd.read_sql(query, conn, params=('%' + sentiment_term + '%',))

        df.sort_values('unix', inplace=True)
        df['date'] = pd.to_datetime(df.unix, unit='ms')
        df.set_index('date', inplace=True)
        df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
        df.dropna(inplace=True)
        df = df.resample('1s').mean()

        X = df.index[-100:]
        Y = df.sentiment_smoothed[-100:]

        data = go.Scatter(x=X,
                          y=Y,
                          name='Scatter',
                          mode='lines+markers'
                          )

        return {'data': [data],
                'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                    yaxis=dict(range=[min(Y), max(Y)]),
                                    title='Termo: {}'.format(sentiment_term)
                                    )
                }

    except Exception as e:
        with open('error.txt', 'a') as f:
            f.write(str(e))
            f.write('\n')


if __name__ == '__main__':
    app.run_server(port=8050, debug=False)

