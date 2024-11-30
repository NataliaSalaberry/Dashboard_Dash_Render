# M71V MAESTRÍA EN GESTIÓN Y ANÁLISIS DE DATOS FIANCIEROS
# MÓDULO 10 INTERPRETACIÓN Y VISUALIZACIÓN DE DATOS FINANCIEROS
# PROFESORA NATALIA SALABERRY

#Recuerde instalar los módulos desde la temrinal antes de ejecutar las librerías 
# si no lo hizo antes

# pip intall datetime
# pip intall yfinance
# pip intall pandas
# pip intall matplotlib
# pip intall ploty
# pip intall dash
# pip intall yfinance



#obtención de datos
from datetime import date, timedelta

#ajustar para obtener un mes
fecha_fin='2023-09-01' #str(date.today()-timedelta(10))
fecha_ini='2023-07-01' #str(date.today()-timedelta(41))

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

app = Dash()

app.layout =html.Div(children=[
    # Elementos en la parte superior de la página
    html.Div([
        html.H1(children='Tablero analítico', style={'textAlign': 'center'}),

        html.Div(children='''Análisis de la cotización de Google Julio-Agosto 2024''', style={'textAlign': 'center','color': 'black', "font-weight": "bold", 'fontSize': 20}),
       # primer gráfico
        dcc.Graph(
            id='graph1',
            figure=fig1
        ),
    ]),
    # así va generando todos los div según los diferentes tipos, como en los ejemplos de clase
    ])

if __name__ == '__main__':
    app.run(debug=True)

#IMPORTANTE: UNA VEZ QUE CORRIÓ TODO EL CÓDIGO, GUARDE EL SCRIPT (app.py) EN LA 
# CARPETA QUE FIGURA EN LA TERMINAL (para eso, vaya al menu de arriba,
# en los tres puntitos-> New Temrinal): por ejemplo, en mi caso: C:\Users\LicNS
# 
# Una vez guardado, ejecutar la app en la terminal anteponiendo python app.py
# 
# en la ejecucción, observe que:
# 1 - Dash is running on http://127.0.0.1:8050/  Click + ctrl en el link y se le abre web la app
# lo que esta sucediendo es que ahora su PC (a través de su IP) esta haciendo de servidor
# Mientras no cierre VS Code (ni apague su PC) siempre estará online el tablero
# 2 - Serving Flask app 'app': Dash esta utilizando Flask para creación de la App. 
# Flask, es muy utilizado para crear App. Acerca de Flask: https://flask.palletsprojects.com/en/stable/

# 3- si modifica el código por ejemplo agregando otro gráfico, etc, luego recuerde Save As y reemplaza.
# al hacer eso observe en la terminal que se vuelve a ejecutar automáticamente
# porque en realidad esta corriendo continuamente (esta On la App)
# si luego va a la web se actualiza automáticamente el tablero.
