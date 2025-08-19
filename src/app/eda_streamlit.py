import streamlit as st
import os

def mostrar_eda():
    st.markdown("# Análisis Exploratorio de Datos (EDA)", unsafe_allow_html=True)

    st.markdown("## ¿Qué es el EDA?")
    st.markdown("""
    El análisis exploratorio de datos (EDA) permite comprender la estructura, calidad y patrones en los datos.  
    Aquí se presentan visualizaciones y estadísticas descriptivas para entender mejor el comportamiento del dataset.
    """)

    st.markdown("## Mes con mayores ingresos")
    st.markdown("""
    A continuación, se muestran las distribuciones de las principales variables numéricas del dataset:
    """)
    mostrar_imagen("mes_max_ingreso.png")
    st.markdown("""
        ### Gráfico:
        """)

    st.markdown("## Ruta con menos pasajeros en un mes")
    st.markdown("""
        A continuación, se muestran las distribuciones de las principales variables numéricas del dataset:
        """)
    mostrar_imagen("ruta_menos_pasajeros_x_mes.png")
    st.markdown("""
            ### Gráfico:
            """)
    st.markdown("## Ruta con mayor ingreso de adultos mayores")
    st.markdown("""
            A continuación, se muestran las distribuciones de las principales variables numéricas del dataset:
            """)
    mostrar_imagen("ruta_mayor_adultos_mayores.png")
    st.markdown("""
                ### Gráfico:
                """)

    st.markdown("## Día con mayor ingreso")
    st.markdown("""
            A continuación, se muestran las distribuciones de las principales variables numéricas del dataset:
            """)
    mostrar_imagen("dia_mayor_ingreso.png")
    st.markdown("""
                ### Gráfico:
                """)

    st.markdown("## Año con mayor ingreso")
    st.markdown("""
            A continuación, se muestran las distribuciones de las principales variables numéricas del dataset:
            """)
    mostrar_imagen("año_mayor_ingreso.png")
    st.markdown("""
                ### Gráfico:
                """)

    st.markdown("## Año con más adultos mayores transportados")
    st.markdown("""
            A continuación, se muestran las distribuciones de las principales variables numéricas del dataset:
            """)
    mostrar_imagen("año_mayor_adultos_mayores_transportados.png")
    st.markdown("""
                ### Gráfico:
                """)


def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Carga una imagen desde la carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")