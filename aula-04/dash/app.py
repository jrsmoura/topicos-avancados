import dash
from dash import dcc, html
from dash import Input, Output
import joblib

app = dash.Dash(__name__)
model_clf = joblib.load('../models/model_clf.pkl')

app.layout = html.Div([
    html.H1("Classificador - Iris"),
    dcc.Input(id='input1', type='text', placeholder='', value=0.),
    dcc.Input(id='input2', type='text', placeholder='', value=0.),
    html.Div(id='output')
    ])

@app.callback(
        Output('output', 'children'),
        Input('input1', 'value'),
        Input('input2', 'value')
        )
def update_clf(input1, input2):
    clf = model_clf.predict([[input1, input2]])

    return f'{clf}'


if __name__ == '__main__':
    app.run_server(debug=True)
