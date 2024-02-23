import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st
import altair as alt

path_gender = "gender_submission.csv"
path_test = "test.csv"
path_train = "train.csv"
df_survived = pd.read_csv(path_gender)
df_test = pd.read_csv(path_test)
df_train = pd.read_csv(path_train)

def grouped_bar_chart(dataframe, column):
    st.subheader(f'Gráfica para la columna: {column}')

    grouped_data = dataframe[column].value_counts().reset_index()
    grouped_data.columns = [column, 'Count']

    chart = alt.Chart(grouped_data).mark_bar().encode(
        x=alt.X(f'{column}:N', title=f'{column}'),
        y=alt.Y('Count:Q', title='Frecuencia'),
        color=alt.Color(f'{column}:N', legend=None)
    ).properties(width=600)

    st.altair_chart(chart, use_container_width=True)

def graph_looper(df, nombre_var):
    st.title(f"Gráficas para el dataframe {nombre_var}")
    for column in df.columns:

        datatype = df[column].dtype
        
        if pd.api.types.is_numeric_dtype(datatype):
            grouped_bar_chart(df,column)


graph_looper(df_survived, "df_survived")
graph_looper(df_test, "df_test")
graph_looper(df_train, "df_train")
