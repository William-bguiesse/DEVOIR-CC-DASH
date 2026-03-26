import pandas as pd
import dash
import dash_bootstrap_components as dbc

# partie chargement des données
df = pd.read_csv('data/avocado.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date') # N'oublie pas le tri pour éviter les graphiques en zigzag !

# partie initialisation de l'application Dash
app = dash.Dash(
    __name__, 
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Volumes", href="/")),
            dbc.NavItem(dbc.NavLink("Tableau", href="/page2")),
            dbc.NavItem(dbc.NavLink("Documentation", href="/page3")),
        ],
        brand="Avocado Dashboard",
        color="dark",
        dark=True,
        className="mb-4",
    ), # <--- LA VIRGULE ÉTAIT MANQUANTE ICI
    
    # Conteneur où les pages (page1.py / page2.py / page3.py) vont s'afficher
    dash.page_container 
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)