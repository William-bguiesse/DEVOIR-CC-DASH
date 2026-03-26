import pandas as pd
import dash
import dash_bootstrap_components as dbc

# partie chargement des données
df = pd.read_csv('data/avocado.csv')
df['Date'] = pd.to_datetime(df['Date'])

# partie initialisation de l'application Dash
app = dash.Dash(
    __name__, 
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    # Barre de navigation fixe en haut
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Volume des Ventes (P1)", href="/", active="exact")),
            dbc.NavItem(dbc.NavLink("Détails & Tableau (P2)", href="/page2", active="exact")),
        ],
        brand="Avocado Analytics Dashboard",
        brand_href="/",
        color="dark",
        dark=True,
        className="mb-4",
    ),
    
    # Conteneur où les pages (page1.py / page2.py) vont s'afficher
    dash.page_container 
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)