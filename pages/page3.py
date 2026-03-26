import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dash.register_page(__name__, path='/page3')
def read_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

content1 = read_md('expli1.md')
content2 = read_md('expli2.md')
content3 = read_md('expli3.md')

layout = dbc.Container([
    html.H2("Documentation et Explications", className="my-4 text-primary"),
    
    dbc.Tabs([
        dbc.Tab(
            dcc.Markdown(content1, className="p-4 border rounded bg-light"),
            label="Explication 1",
            tab_id="tab-1"
        ),
        dbc.Tab(
            dcc.Markdown(content2, className="p-4 border rounded bg-light"),
            label="Explication 2",
            tab_id="tab-2"
        ),
        dbc.Tab(
            dcc.Markdown(content3, className="p-4 border rounded bg-light"),
            label="Explication 3",
            tab_id="tab-3"
        ),
    ], active_tab="tab-1")
], fluid=True)