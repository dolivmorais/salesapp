from pathlib import Path
import streamlit as st
import pandas as pd


COMISSAO = 0.08

def leitura_de_dados():
    if not 'dados' in st.session_state:
        pasta_dataset = Path(__file__).parents[1] / "datasets"
        df_vendas = pd.read_csv(pasta_dataset / "vendas.csv",decimal=",", sep=";",index_col=0,parse_dates=True)
        df_filiais = pd.read_csv(pasta_dataset / "filiais.csv",decimal=",", sep=";",index_col=0)
        df_produtos = pd.read_csv(pasta_dataset / "produtos.csv",decimal=",", sep=";",index_col=0)
        dados = {
            'df_vendas': df_vendas,
            'df_filiais': df_filiais,
            'df_produtos': df_produtos
        }
        st.session_state['caminho_dataset'] = pasta_dataset
        st.session_state['dados'] = dados


