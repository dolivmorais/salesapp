from pathlib import Path

import streamlit as st
import pandas as pd

pasta_dataset = Path(__file__).parents[1] / "datasets"

pasta_dataset0 = Path(__file__).parents[0] / "datasets"
pasta_dataset1 = Path(__file__).parents[1] / "datasets"
pasta_dataset2 = Path(__file__).parents[2] / "datasets"
print(pasta_dataset0)
print(pasta_dataset1)
print(pasta_dataset2)


df_vendas = pd.read_csv(pasta_dataset / "vendas.csv",decimal=",", sep=";",index_col=0,parse_dates=True)
df_filiais = pd.read_csv(pasta_dataset / "filiais.csv",decimal=",", sep=";",index_col=0)
df_produtos = pd.read_csv(pasta_dataset / "produtos.csv",decimal=",", sep=";",index_col=0)
