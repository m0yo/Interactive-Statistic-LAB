import streamlit as st
import pandas as pd

st.set_page_config(page_title="Jogos", layout="wide")
st.title("Dados sobre jogos")

DATA = "data/dataset.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df['User_Score'] = pd.to_numeric(df['User_Score'], errors='coerce') # esta linha converte os dados da coluna User_Score para números e se não houver nenhum dado na coluna, ele retorna 'None'

    return df

df = load_data(DATA) # carrega a tabela

# aqui divide as colunas categoricas e as numericas
num_col = df.select_dtypes(include="number").columns.tolist()
num_cat = df.select_dtypes(exclude="number").columns.tolist()

st.write(f"Formato do dataset: {df.shape[0]} linhas, {df.shape[1]} colunas")
st.write("Colunas numéricas:", num_col)
st.write("Colunas Categóricas:", num_cat)

st.write(df)