import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
     page_title="Análise da Previsão de Renda:",
     page_icon="https://cdn-icons-png.flaticon.com/512/3594/3594449.png",
     layout="wide",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

path = r"E:\backup\Python\2024\Python\Estudo\EBAC\Mod_4\projeto 2\input\previsao_de_renda.csv"
renda = pd.read_csv(path)


# gráfico de barras:
def graf_bar(var: str):
    """ Recebe a string de uma variável categórica e retorna
    um barplot da renda média em função da variável
    """
    gi = renda.groupby(var)['renda'].mean().sort_values()
    plt.figure(figsize=(15,8))
    sns.barplot(x=gi.index, y=gi, palette='viridis', errorbar=('ci', 90))
    plt.title(f'Renda média em função de {var}')
    plt.ylabel('Renda média')

# Grafico de point:
def graf_point(var: str):
    """ Recebe a string de uma variável categórica e retorna
    um pointplot da renda média em função da variável
    """
    plt.figure(figsize=(10,6))
    sns.pointplot(data=renda, x=var, y='renda')
    plt.title(f'Renda média em função de {var}')
    plt.ylabel('Renda média')

st.title('Análise exploratória da previsão de renda')
st.markdown('Nesta página será exposto as visualizações utilizadas no projeto.')
st.markdown('----')
st.markdown('### Renda em função do tempo de emprego:')

fig, ax = plt.subplots()
sns.scatterplot(data=renda.dropna(), x='tempo_emprego', y='renda', hue='sexo', ax=ax)
st.pyplot(fig)
st.markdown('Podemos notar a pequena correlação entre __renda__ e __tempo empregado__. Esta correlação apresenta diferentes valores para clientes de sexo masculino e feminino.')

st.markdown('----')
st.markdown('### Relação de variáveis booleanas com a renda média:')

st.pyplot(graf_point('sexo'))
st.pyplot(graf_point('posse_de_imovel'))
st.pyplot(graf_point('posse_de_veiculo'))
st.subheader('Considerações:')
st.markdown('__sexo__ e __posse_de_veiculo__ apresentam uma distinção estatisticamente relevante em relação a renda média')
st.markdown('Renda média não apresenta variação significativa, considerando intervalo de confiança, para a variável __posse_de_imovel__')

st.markdown('----')
st.markdown('### Relação da renda média com variáveis categóricas:')
st.pyplot(graf_bar('tipo_residencia'))
st.pyplot(graf_bar('estado_civil'))
st.pyplot(graf_bar('educacao'))
st.pyplot(graf_bar('tipo_renda'))
st.subheader('Considerações:')
st.markdown('Podemos notar uma tendência de valores distíntos de renda média para diferentes classes das variáveis analisadas')