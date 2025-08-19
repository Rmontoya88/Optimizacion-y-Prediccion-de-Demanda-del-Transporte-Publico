import streamlit as st
import sys
import os
from PIL import Image
from incofer import mostrar_historia
from dataset import mostrar_dataset
from eda_streamlit import  mostrar_eda
from paradas_servicio import mostrar_paradas_servicio
from Clasificacion_streamlit import mostrar_modelo_clasificacion
from Regresion_streamlit import  mostrar_modelo_regresion
from bd_streamlit import mostrar_base_datos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import pandas as pd

st.set_page_config(
    page_title="Optimización y Predicción de Demanda del Transporte Público",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ruta para la imagen
logo_path = "D:/cuc/programacion 2/Proyecto Final/Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico/src/app/imagenes/icon.png"

# Mostrar la imagen del logo en el slider
def display_logo(logo_path):
    image = Image.open(logo_path)
    return image

st.markdown("""
    <style>
        .header {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1rem;
            border-bottom: 1px solid #ccc;
        }
        .header h1 {
            font-size: 1.5rem;
            color: #2c3e50;
            margin: 0;
            font-weight: 600;
        }
        .stRadio label {
            font-weight: 500;
            color: #2c3e50;
        }
        /* Estilo para las imágenes */
        .stImage {
            width: 100%;
            max-width: 800px;  /* Limitar el ancho máximo */
            margin: 0 auto;  /* Centrar la imagen */
        }
        /* Estilo para los contenedores de las imágenes */
        .stImage > div {
            text-align: center;

    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    logo = display_logo(logo_path)
    if logo:
        st.image(logo, use_container_width=True)

    st.markdown("### **Opciones del Proyecto**")
    selected_option = st.radio(
        "Selecciona una opción:",
        ["Incofer", "Base de Datos", "Dataset", "EDA", "Paradas de Servicio", "Modelo Clasificación",
         "Modelo Regresión", "Api","Repositorio GIT"]
    )

# Mostrar el título
st.markdown(f"## {selected_option}")

if selected_option == "Incofer":
     mostrar_historia()

elif selected_option == "Dataset":
    mostrar_dataset()

elif selected_option == "Base de Datos":
    mostrar_base_datos()

elif selected_option == "EDA":
    mostrar_eda()

elif selected_option == "Paradas de Servicio":

    ruta_mapa_locomotoras = "D:/cuc/programacion 2/Proyecto Final/Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico/data/raw/Paradas_del_servicio_del_tren.csv"
    df_mapa_locomotoras = pd.read_csv(ruta_mapa_locomotoras, encoding='utf-8')
    mostrar_paradas_servicio(df_mapa_locomotoras)

elif selected_option == "Modelo Clasificación":
    mostrar_modelo_clasificacion()

elif selected_option == "Modelo Regresión":
    mostrar_modelo_regresion()

elif selected_option == "Repositorio GIT":
    st.markdown("""
        [Ir al Repositorio en GitHub](https://github.com/Rmontoya88/Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico/tree/main)
    """)
else:
    st.markdown("Contenido relacionado con la **Api**")



