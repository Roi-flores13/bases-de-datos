import streamlit as st
import pandas as pd

st.title("Hola mundo")
st.header("Esto es un header")
st.markdown("### Hola")

path = r"train.csv"
df = pd.read_csv(path)

st.dataframe(df)

