# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("despesas subfuncao.csv")

# criando gráfico
fig = px.bar(df, x="Mês Ano", y="Valor Empenhado", color="Área de atuação (Função)", barmode="group")
fig1 = px.line(df, x="Mês Ano", y="Valor Pago", color="Subfunção")


opcoes = list(df["Área de atuação (Função)"].unique())
opcoes.append("Todas as funções")

opcoes1 = list(df["Subfunção"].unique())
opcoes1.append("Todos os valores pago")


# no layout pode criar itens html ou itens grafico (textos, link e imagens)
app.layout = html.Div(children=[
    html.H1(
        children='VALOR EMPENHADO DE DESPESAS POR MÊS ANO',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(children='Dash: Consulta da Despesa Pública.',
             style={
                'textAlign': 'center',
    }),

#grafico 0
    # Gráficos e botoes que vao interagir diretamente com o gráfico é do dash
    dcc.Dropdown(opcoes, value='Todas as funções', id='lista_funções'),
    dcc.Graph(
        id='grafico_valor_empenhado',
        figure=fig
    ),

    #figura 1
    dcc.Dropdown(opcoes1, value='Todos os valores pago', id='lista_subfunção'),
    dcc.Graph(
        id='grafico_valor_pago',
        figure=fig1
    )
])

#grafico 0
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

    #grafico 1
@app.callback(
    Output('grafico_valor_pago', 'figure'),       # saida
    Input('lista_subfunção', 'value')            # Componente de entrada
)
def update_output(value):
    if value == 'Todos os valores pago':
        fig1 = px.line(df, x="Mês Ano", y="Valor Pago", color="Subfunção")

    else:
        tabela1 = df.loc[df['Valor Pago']==value, :]
        fig1 = px.line(tabela1, x="Mês Ano", y="Valor Pago", color="Subfunção")

    return fig1

if __name__ == '__main__':
    app.run_server(debug=True)