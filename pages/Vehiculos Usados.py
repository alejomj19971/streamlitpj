import streamlit as st
import pandas as pd
import numpy as np



#Title sirve para mostrar un titulo con un texto como parámetro
st.title("Automoviles Usados -Los más vendidos")

# se lee el archivo en data,queda en un formato de texto compatible para crear un dataframe
data = pd.read_csv('carros.csv')
df = pd.DataFrame(data)


modelo = st.selectbox('MODEL',(df["Model"].sort_values(ascending=True).unique()))  
precio = st.selectbox('PRECIO',(df["Price;"].sort_values(ascending=True).unique()))   
marca = st.selectbox('MARCA',(df["Make"].sort_values(ascending=True).unique()))  
kilometros= st.selectbox('KILOMETROS',(df["Kilometres"].sort_values(ascending=True).unique())) 

#Filtro de barras
filtroBarras = (df['MODEL'] == modelo) & (df['PRECIO'] ==precio)   
df_filtradoBarras = df.loc[filtroBarras]

chart_data = pd.DataFrame(df_filtradoBarras)

st.bar_chart(chart_data)



st.write(df)
