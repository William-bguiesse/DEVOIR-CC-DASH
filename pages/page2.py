import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from app import df

# Enregistrement de la page
dash.register_page(__name__, path='/page2')

# Préparation des options
options_regions = [{'label': r, 'value': r} for r in sorted(df['region'].unique())]
options_types = [{'label': t, 'value': t} for t in sorted(df['type'].unique())]

layout = dbc.Container([
    html.H2("Exploration des données par Région et Type", className="my-4"),
    
    dbc.Row([
        # Colonne de gauche : Les Filtres
        dbc.Col([
            html.Div([
                html.Label("Sélectionner la région :", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='filter-region', 
                    options=options_regions, 
                    value='Albany',
                    clearable=False
                ),
                
                html.Br(),
                
                html.Label("Type d'avocat :", style={'fontWeight': 'bold'}),
                dcc.RadioItems(
                    id='filter-type', 
                    options=options_types, 
                    value='conventional', 
                    labelStyle={'display': 'block', 'margin-bottom': '5px'},
                    inputStyle={"margin-right": "10px"}
                ),
                
                html.Br(),
                
                # Le Badge pour le nombre de lignes
                html.Div([
                    dbc.Badge(id='row-count-badge', color="primary", className="p-2")
                ], className="d-grid gap-2")
            ], className="p-3 border rounded bg-light")
        ], width=3),
        
        # Colonne de droite : Le Tableau
        dbc.Col([
            dash_table.DataTable(
                id='data-table-avocado',
                # On définit les colonnes (sauf l'index inutile)
                columns=[{"name": i, "id": i} for i in df.columns if i != 'Unnamed: 0'],
                page_size=15,
                style_table={'overflowX': 'auto', 'border': '1px solid #dee2e6'},
                style_cell={'textAlign': 'left', 'padding': '10px', 'font-family': 'sans-serif'},
                style_header={'backgroundColor': '#f8f9fa', 'fontWeight': 'bold', 'borderBottom': '2px solid #dee2e6'}
            )
        ], width=9)
    ])
], fluid=True)

import pages.page2_cb