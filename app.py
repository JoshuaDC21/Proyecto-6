#Importa librerias
import pandas as pd
import plotly_express as px
import streamlit as st

#Lee los datos
car_data = pd.read_csv('C:\\Users\\joshu\\Documents\\DS\\Proyecto 6\\vehicles_us.csv')

#Crea un encabezado
st.header('Información sobre venta de coches')

#Crea un checkbox para cada gráfico
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

#Genera el histograma
if build_histogram: # si la casilla de verificación está seleccionada
            
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig_1 = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig_1, use_container_width=True)

#Genera un gráfico de dispersión
if build_histogram: # si la casilla de verificación está seleccionada
            
            st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            fig_2 = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig_2, use_container_width=True)
