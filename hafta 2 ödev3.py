import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

veri = pd.DataFrame({
    "Departman": ["Pazarlama", "Satış", "IT", "IK", "Finans"],
    "Bütçe_Milyon_TL": [12.5, 18.2, 25.0, 5.4, 10.1]
})

grafik = px.bar(veri, x="Departman", y="Bütçe_Milyon_TL",
                title="Departmanlara Göre Bütçe Dağılımı",
                color="Departman", template="plotly_white")

uygulama = dash.Dash(__name__)

uygulama.layout = html.Div(children=[
    html.H1(children='Kurumsal İş Zekası (BI) Paneli', style={'textAlign': 'center'}),
    html.Div(children='Stratejik karar alma süreçlerini destekleyen veriye dayalı içgörüler.',
             style={'textAlign': 'center', 'color': '#7FDBFF'}),
    dcc.Graph(id='butce-grafigi', figure=grafik)
])

if __name__ == '__main__':
    uygulama.run(debug=False, port=8050)