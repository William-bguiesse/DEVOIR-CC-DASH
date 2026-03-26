import dash
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
from app import df 


dash.register_page(__name__, path='/')

regions = ["MidSouth", "Northeast", "South Central", "Southeast", "TotalUS", "West"]
df_fixes = df[df['region'].isin(regions)]

fig_principale = px.line(
    df_fixes, 
    x='Date', 
    y='Total Volume', 
    color='region',
    title="Quantités vendues - Régions principales"
)

# creation de la variable qui sert de menu deroulant pour les regions
options_regions = [{'label': r, 'value': r} for r in sorted(df['region'].unique())]

# creation du layout de la page d'accueil. il contient le graph des regions avec le menu deroulant.
layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(html.H2("Quantités vendues (Total Volume)")),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='graph-regions-principales', figure=fig_principale)
                ], width=7),
                dbc.Col([
                    dbc.Badge("Sélectionnez une région:", color="purple", className="mb-2"),
                    dcc.Dropdown(
                        id='dropdown-region', 
                        options=options_regions,
                        value='Albany', 
                        clearable=False
                    ),
                    dcc.Graph(id='graph-region-unique') # Ce graphique restera vide ou fixe pour l'instant
                ], width=5)
            ])
        ])
    ], className="mt-4")
], fluid=True)