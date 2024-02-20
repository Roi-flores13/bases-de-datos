import streamlit as st
import pandas as pd

st.title("Hola mundo")
st.header("Esto es un header")
st.markdown("### Hola")

path = r"C:\Users\Roi_f\apps\bases-de-datos\src\streamlit\train.csv"
df = pd.read_csv(path)

st.dataframe(df)
