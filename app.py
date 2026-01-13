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
st.write("Aplicación web creada con Streamlit para explorar anuncios de venta de vehículos.")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

car_data = load_data()

# Vista previa del dataset
st.subheader("Vista previa del dataset")
st.dataframe(car_data.head())

# Información general
st.subheader("Información general del dataset")
st.write(car_data.describe(include="all"))

st.divider()
st.subheader("📊 Visualizaciones interactivas")

# =========================
# Histograma del odómetro
# =========================
build_histogram = st.checkbox("Construir histograma del odómetro")

if build_histogram:
    st.write("Distribución del kilometraje de los vehículos")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del odómetro"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# =========================
# Histograma de precios
# =========================
build_price_hist = st.checkbox("Construir histograma de precios")

if build_price_hist:
    st.write("Distribución de precios de los vehículos")
    fig_price = px.histogram(
        car_data,
        x="price",
        nbins=50,
        title="Distribución de precios"
    )
    st.plotly_chart(fig_price, use_container_width=True)

# =========================
# Gráfico de dispersión
# =========================
build_scatter = st.checkbox("Construir gráfico de dispersión precio vs odómetro")

if build_scatter:
    st.write("Relación entre precio y kilometraje")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.4,
        title="Precio vs odómetro"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
