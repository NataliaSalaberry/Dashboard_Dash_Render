# EJEMPLO DE DASHBOARD
# NATALIA SALABERRY

#obtención de datos
from datetime import date, timedelta

#ajustar para obtener un mes
fecha_fin='2023-09-01' 
fecha_ini='2023-07-01' 

import yfinance as yf
import pandas as pd

Datos_GOOG = pd.DataFrame(yf.download('GOOGL', start=fecha_ini, end=fecha_fin)).reset_index()
Datos_GOOG.columns=Datos_GOOG.columns.droplevel(1)
Datos_GOOG

#formato a Date
Datos_GOOG['Date'] = Datos_GOOG['Date'].dt.strftime('%Y-%m-%d')

#creación de un gráfico
import plotly.graph_objects as go

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=Datos_GOOG['Date'],
               y=Datos_GOOG['Adj Close'],
               name="Adj Close",
               line=dict(color='#636EFA')
               ))

fig1.add_trace(
    go.Scatter(x=Datos_GOOG['Date'],
               y=Datos_GOOG['Open'],
               name="Open Price",
               visible=False,
               line=dict(color="#EF553B")))

fig1.add_trace(
    go.Scatter(x=Datos_GOOG['Date'],
               y=Datos_GOOG['High'],
               name="High Price",
               visible=False,
               line=dict(color="#00CC96", dash="dash")))

fig1.add_trace(
    go.Scatter(x=Datos_GOOG['Date'],
               y=Datos_GOOG['Low'],
               name="Low Price",
               visible=False,
               line=dict(color="#AB63FA", dash="dash")))

fig1.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, True, True]},
                           {"title": "Cotización Google Julio-Agosto 2023"}]),
                dict(label="Adj Close",
                     method="update",
                     args=[{"visible": [True, False, False, False]},
                           {"title": "Cotización de cierre ajustado Google Julio-Agosto 2023"}]),
                dict(label="Open",
                     method="update",
                     args=[{"visible": [False, True, False, False]},
                           {"title": "Cotización apertura Google Julio-Agosto 2023"}]),
                dict(label="High",
                     method="update",
                     args=[{"visible": [False, False, True, False]},
                           {"title": "Cotización máxima Google Julio-Agosto 2023"}]),
                dict(label="Low",
                     method="update",
                     args=[{"visible": [False, False, False, True]},
                           {"title": "Cotización mínima Google Julio-Agosto 2023"}]),
            ]),
        )
    ])

fig1.update_layout(title_text="Cotización Google Julio-Agosto 2023")
fig1.update_layout(dict(xaxis = dict( type='date', tickformat="%Y-%m-%d",range = ['2023-07-01','2023-09-1'],nticks=80,tickfont=dict(size=8),tickangle=45)))
fig1.update_layout(template='none')


#Creación de la App

import dash

from dash import Dash, dcc, html

app = dash.Dash(__name__)
server = app.server

app.layout =html.Div(children=[
    # Elementos en la parte superior de la página
    html.Div([
        html.H1(children='Tablero analítico', style={'textAlign': 'center'}),

        html.Div(children='''Análisis de la cotización de Google Julio-Agosto 2023''', style={'textAlign': 'center','color': 'black', "font-weight": "bold", 'fontSize': 20}),
       # primer gráfico
        dcc.Graph(
            id='graph1',
            figure=fig1
        ),
    ]),
    ])

if __name__ == '__main__':
    app.run_server(debug=False)


