# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv("despesas subfuncao.csv")

# criando gráfico
fig = px.bar(df, x="Mês Ano", y="Valor Empenhado", color="Área de atuação (Função)", barmode="group")

opcoes = list(df["Área de atuação (Função)"].unique())
opcoes.append("todas as funções")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# no layout pode criar itens html ou itens grafico (textos, link e imagens)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='VALOR EMPENHADO DE DESPESAS POR MÊS ANO',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: Consulta da Despesa Pública.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    # Gráficos e botoes que vao interagir diretamente com o gráfico é do dash
    dcc.Dropdown(opcoes, value='Todas as funções', id='lista_funções'),
    dcc.Graph(
        id='grafico_valor_empenhado',
        figure=fig
    )
])

@app.callback(
    Output('grafico_valor_empenhado', 'figure'),       # saida
    Input('lista_funções', 'value')            # Componente de entrada
)
def update_output(value):
    if value == 'Todas as funções':
        fig = px.bar(df, x="Mês Ano", y="Valor Empenhado", color="Área de atuação (Função)", barmode="group")
    else:
        tabela_filtrada = df.loc[df['Área de atuação (Função)']==value, :]
        fig = px.bar(tabela_filtrada, x="Mês Ano", y="Valor Empenhado", color="Área de atuação (Função)", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
