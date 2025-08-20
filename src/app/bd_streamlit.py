import streamlit as st
import os

def mostrar_base_datos():
    st.markdown("# Creación de la Base de Datos", unsafe_allow_html=True)

    st.markdown("## ¿Cómo se creó la base de datos?")
    st.markdown("""
    La base de datos fue creada para almacenar toda la información relacionada con los viajes de transporte público.  
    Esta base de datos se construyó a partir de diferentes fuentes de datos, que fueron procesadas y transformadas para adaptarlas a las necesidades.

    El proceso de creación de la base de datos consistió en los siguientes pasos:
    1. **Recolección de los datos** 
    2. **Creación de la Base de Datos** 
    3. **Creación de tablas** 
    4. **Carga de la base de datos** en un sistema de gestión de bases de datos PostgreSQL
    """)

    st.markdown(" **Limpieza y transformación de los datos** para asegurarse de que estuvieran en un formato adecuado.")
    mostrar_imagen("transformacion_datos.png")
    mostrar_imagen("transformaciondatos2.png")
    mostrar_imagen("transformaciondatos3.png")
    st.markdown("## Conclusiones")
    st.markdown(""" La limpieza y transformacion de los datos es de suma importancia mas cuando el objetivo principal es realizar anaslisis.
    Mas cuando son datos tan relevnates como del INCOFER, donde se requiere de la cosistencia de los datos para obtener los resultados
    deseados
    """)

def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Carga una imagen desde la carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
