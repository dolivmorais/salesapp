from pathlib import Path
from datetime import datetime

import streamlit as st
import pandas as pd
from utilidades.utilidades import leitura_de_dados

leitura_de_dados()

df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']
df_vendas = st.session_state['dados']['df_vendas']


df_filiais['cidade/estado'] = df_filiais['cidade'] + '/' + df_filiais['estado']
cidades_filiais = df_filiais['cidade/estado'].unique().tolist()


st.sidebar.markdown('### Adição de Vendas')
filial_selecionada = st.sidebar.selectbox('Selecionar Filial: ', cidades_filiais)

vendedores = df_filiais.loc[df_filiais['cidade/estado'] == cidades_filiais, 'vendedores'].iloc[0]
vendedores = vendedores.strip('][').replace("'", "").split(', ')
vendedores_selecionado = st.sidebar.selectbox('Selecionar Vendedores: ', vendedores)

produtos = df_produtos['nome'].unique().tolist()
produtos_selecionado = st.sidebar.selectbox('Selecionar Produtos: ', produtos)

nome_do_Cliente = st.sidebar.text_input('Nome do Cliente: ')
genero_seleconado = st.sidebar.selectbox('Genero: ', ['Masculino', 'Feminino'])

fromma_de_pagamento = st.sidebar.selectbox('Forma de Pagamento: ', ['Boleto', 'Cartão', 'Pix', 'Dinheiro'])

adicionar_venda = st.sidebar.button('Adicionar Venda')
if adicionar_venda:
    lista_adicionar = [df_vendas["id_venda"].max() + 1,
                    filial_selecionada.split('/')[0],
                    vendedores_selecionado,
                    produtos_selecionado,
                    nome_do_Cliente,
                    genero_seleconado,
                    fromma_de_pagamento,
                    ]
    hora_adicionada = datetime.now()
    df_vendas.loc[hora_adicionada] = lista_adicionar
    df_vendas.to_csv( st.session_state['caminho_dataset']/ 'vendas.csv', decimal=',', sep=';')
    st.dataframe(df_vendas)


st.sidebar.markdown('### Remoção de Vendas')
id_remocao = st.sidebar.number_input('ID da Venda a ser removida: ', 
                                     min_value=0,
                                     max_value=df_vendas['id_venda'].max())

remover_venda = st.sidebar.button('Remover Venda')
if remover_venda:
    df_vendas = df_vendas[df_vendas['id_venda'] != id_remocao]
    df_vendas.to_csv( st.session_state['caminho_dataset']/ 'vendas.csv', decimal=',', sep=';')
    st.session_state['dados']['df_vendas'] = df_vendas


st.dataframe(df_vendas,height=800)

