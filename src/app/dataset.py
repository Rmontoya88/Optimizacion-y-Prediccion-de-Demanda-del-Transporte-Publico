import streamlit as st
import os

def mostrar_dataset():
    st.markdown("# Dataset", unsafe_allow_html=True)

    st.markdown("## ¿Dónde se obtuvo el dataset?")
    st.markdown("""
    El dataset fue obtenido de la fuente oficial de INCOFER a través del portal de datos abiertos del gobierno.  
    Contiene información relacionada con los viajes diarios, horarios, estaciones, y otros datos relevantes.
    """)
    mostrar_imagen("dataset.jpg")
    st.markdown("""[Ir a la web](https://aresep.go.cr/datos-abiertos/#info_datos_estadisticatren)
        """)

    st.markdown("##  ¿Qué tipo de datos contiene el dataset?")
    st.markdown("""
    El dataset contiene datos estructurados en formato CSV, incluyendo variables categóricas y numéricas como:
    - Descripción de la Ruta
    - Código Recorrido
    - Descripción del Recorrido
    - Sentido
    - Día
    - Mes
    - Año
    - Cantidad de Pasajeros Regulares
    - Cantidad de Adultos Mayores
    - Ingresos
    """)
    mostrar_imagen("info.png")

    st.markdown("## Información Básica del Dataset")
    st.markdown("""
        El dataset contiene:""")
    mostrar_imagen("info_basica.png")

    st.markdown("""
            Cantidad de valores nulos:""")
    mostrar_imagen("nulos.png")

    st.markdown("""
                Se tratan los valores nulos:""")
    mostrar_imagen("nulos_tratar.png")

    st.markdown("## Información Básica del Dataset")
    st.markdown("""
                ### Código de Ruta :""")
    mostrar_imagen("codigo_ruta.png")

    st.markdown("""
                ### Descripción de Ruta :""")
    mostrar_imagen("Descripcion_ruta.png")

    st.markdown("""
                    ### Código de Recorrido:""")
    mostrar_imagen("recorrido.png")

    st.markdown("""
                   ### Descripcion de Recorrido:""")
    mostrar_imagen("descripcion_recorrido.png")

    st.markdown("""
                       ### Sentido:""")
    mostrar_imagen("sentido.png")

    st.markdown("""
                       ### Día:""")
    mostrar_imagen("dia.png")

    st.markdown("""
                       ### Mes:""")
    mostrar_imagen("mes.png")

    st.markdown("""
                       ### Año:""")
    mostrar_imagen("Año.png")

    st.markdown("""
                   Las otras columnas tienen valores númericos a gran escala""")

    st.markdown("## Proceso de limpieza")
    st.markdown("""
    Se realizaron las siguientes transformaciones para preparar los datos:
    - Transformación de valores nulos a valores numerico cero
    """)
    mostrar_imagen("dataset_final.png")

    st.markdown("## Dataset listo para análisis")
    mostrar_imagen("dataset_final.png")

def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Función para cargar imágenes desde carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
