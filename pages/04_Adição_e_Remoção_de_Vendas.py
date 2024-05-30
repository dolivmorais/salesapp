from pathlib import Path

import streamlit as st
import pandas as pd
from utilidades.utilidades import leitura_de_dados

leitura_de_dados()


df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']
df_vendas = st.session_state['dados']['df_vendas']

st.session_state['df_filiais'] = df_filiais
st.session_state['df_produtos'] = df_produtos
st.session_state['df_vendas'] = df_vendas

st.dataframe(df_vendas)
st.dataframe(df_filiais)
st.dataframe(df_produtos)