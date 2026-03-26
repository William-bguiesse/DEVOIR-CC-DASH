from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# 1. Chargement des données
df = pd.read_csv('data/avocado.csv')

# 2. Initialisation avec un thème Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# --- STYLES POUR LA SIDEBAR ---
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# --- COMPOSANT SIDEBAR ---
sidebar = html.Div(
    [
        html.H2("Avocado", className="display-6"),
        html.Hr(),
        html.P("Table des matières", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("🏠 Accueil", href="/", active="exact"),
                dbc.NavLink("📈 Prix par Région", href="/prix", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# --- LAYOUT PRINCIPAL ---
app.layout = html.Div([
    dcc.Location(id="url"), # Surveille l'URL
    sidebar,                # Affiche le menu
    html.Div(id="page-content", style=CONTENT_STYLE) # Zone où le contenu change
])

# --- CALLBACK POUR LA NAVIGATION ---
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
            html.H1("Bienvenue sur l'Analyse Avocat"),
            html.P("Utilisez le menu à gauche pour naviguer dans les données.")
        ])
    
    elif pathname == "/prix":
        # On retourne le layout que tu avais créé
        return html.Div([
            dbc.Row([
                dbc.Col([html.H1("Évolution des prix", className="mb-4")], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    html.Label("Choisissez une région :"),
                    dcc.Dropdown(
                        id='region-filter', 
                        options=[{'label': r, 'value': r} for r in sorted(df['region'].unique())], 
                        value='Albany',
                        clearable=False
                    )
                ], width=4),
                dbc.Col([
                    dcc.Graph(id='price-graph')
                ], width=8)
            ])
        ])
    
    # Si la page n'est pas trouvée
    return html.Div([
        html.H1("404: Not Found", className="text-danger"),
        html.P(f"Le chemin {pathname} n'existe pas.")
    ])

# --- CALLBACK POUR LE GRAPHIQUE (Uniquement sur la page /prix) ---
@app.callback(
    Output('price-graph', 'figure'),
    Input('region-filter', 'value'),
    prevent_initial_call=True # Évite de chercher l'ID avant que la page soit chargée
)
def update_graph(selected_region):
    if not selected_region:
        return px.line()
    
    filtered_df = df[df['region'] == selected_region]
    fig = px.line(
        filtered_df.sort_values(by="Date"), 
        x='Date', 
        y='AveragePrice',
        title=f"Prix à {selected_region}",
        color='type',
        template="plotly_white"
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)