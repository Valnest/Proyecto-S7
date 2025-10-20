import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Anuncios de Vehículos en Estados Unidos')

st.write("""
Esta aplicación interactiva permite explorar el conjunto de datos **vehicles_us.csv**.
Puedes visualizar la distribución del kilómetro (odometer) y la relación entre precio y kilómetro.
""")

hist_button = st.button('Construir histograma del kilometraje')

if hist_button:
    st.write('Creando un histograma del kilometraje de los vehículos...')
    fig = px.histogram(
        car_data,
        x='odometer',
        nbins=30,
        title='Distribución del kilometraje (odómetro)',
        labels={'odometer': 'Kilometraje (millas)'}
    )
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión Precio vs Kilometraje')

if scatter_button:
    st.write('Creando un gráfico de dispersión: Precio vs. Kilometraje...')
    color_col = 'condition' if 'condition' in car_data.columns else None
    fig2 = px.scatter(
        car_data,
        x='odometer',
        y='price',
        color=color_col,
        title='Relación entre Precio y Kilometraje',
        labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio (USD)', 'condition': 'Condición'}
    )
    st.plotly_chart(fig2, use_container_width=True)

