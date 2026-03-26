from dash import Input, Output, callback
import plotly.express as px
from app import df 

@callback(
    Output('graph-region-unique', 'figure'),
    Input('dropdown-region', 'value') 
)
def update_graph(selected_region):
    filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, 
        x='Date', 
        y='Total Volume', 
        title=f"Détail des ventes : {selected_region}",
        markers=True 
    )
    return fig