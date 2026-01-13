import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Proyecto Sprint 7", layout="wide")

st.header("🚗 Análisis exploratorio de anuncios de coches")

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# Checkbox: histograma
build_histogram = st.checkbox("Construir histograma del odómetro")

if build_histogram:
    st.write("Distribución del kilometraje de los vehículos")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox: dispersión
build_scatter = st.checkbox("Construir gráfico de dispersión precio vs odómetro")

if build_scatter:
    st.write("Relación entre precio y kilometraje")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.4
    )
    st.plotly_chart(fig, use_container_width=True)
