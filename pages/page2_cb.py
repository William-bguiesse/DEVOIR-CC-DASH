from dash import Input, Output, callback
from app import df  # On importe les données chargées dans app.py

@callback(
    [Output('data-table-avocado', 'data'),      # On met à jour les lignes du tableau
     Output('row-count-badge', 'children')],   # On met à jour le texte du badge
    [Input('filter-region', 'value'),          # On écoute le menu région
     Input('filter-type', 'value')]            # On écoute les boutons radio (type)
)
def update_table_and_badge(region_val, type_val):
    # 1. Filtrage des données selon les deux critères
    dff = df[(df['region'] == region_val) & (df['type'] == type_val)]
    
    # 2. Conversion des données filtrées pour le tableau
    table_data = dff.to_dict('records')
    
    # 3. Préparation du texte pour le badge
    badge_label = f"Lignes affichées : {len(dff)}"
    
    return table_data, badge_label