import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Proyecto Sprint 7",
    layout="wide"
)

# Encabezado principal
st.header("🚗 Análisis exploratorio de anuncios de coches")
st.write("Aplicación web interactiva creada con Streamlit para explorar anuncios de vehículos en EE. UU.")

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# --- Vista previa del dataset ---
st.subheader("Vista previa del dataset")
st.dataframe(car_data.head())

# --- Información general ---
st.subheader("Información general del dataset")
st.write(car_data.describe(include="all"))

st.divider()

# --- Checkbox: histograma del odómetro ---
build_odometer_hist = st.checkbox("Construir histograma del odómetro")

if build_odometer_hist:
    st.write("Distribución del kilometraje de los vehículos")
    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=100,
        title="Distribución del kilometraje"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Checkbox: histograma de precios ---
build_price_hist = st.checkbox("Construir histograma de precios")

if build_price_hist:
    st.write("Distribución de precios de los vehículos")
    fig = px.histogram(
        car_data,
        x="price",
        nbins=50,
        title="Distribución de precios"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Checkbox: scatter precio vs odómetro ---
build_scatter = st.checkbox("Construir gráfico de dispersión precio vs odómetro")

if build_scatter:
    st.write("Relación entre precio y kilometraje")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.4,
        title="Precio vs kilometraje"
    )
    st.plotly_chart(fig, use_container_width=True)
