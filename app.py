import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Proyecto Sprint 7", layout="wide")

st.title("🚗 Análisis exploratorio de datos")
st.write("Aplicación web creada con Streamlit")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# Mostrar dataset
st.subheader("Vista previa del dataset")
st.dataframe(df.head())

# Información general
st.subheader("Información general del dataset")
st.write(df.describe(include="all"))

# Gráfico simple
st.subheader("Distribución de precios de vehículos")
fig = px.histogram(
    df,
    x="price",
    nbins=50,
    title="Distribución de precios"
)
st.plotly_chart(fig, use_container_width=True)

import pandas as pd
import streamlit as st

st.title("🚗 Análisis exploratorio de datos")
st.write("Aplicación web creada con Streamlit")

df = pd.read_csv("vehicles_us.csv")

st.subheader("Vista previa del dataset")
st.dataframe(df.head())

st.subheader("Información general del dataset")
st.write(df.describe(include="all"))
