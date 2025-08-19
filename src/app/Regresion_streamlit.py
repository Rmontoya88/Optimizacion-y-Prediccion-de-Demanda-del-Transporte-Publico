import streamlit as st
import os

def mostrar_modelo_regresion():
    st.markdown("# Modelo de Regresión", unsafe_allow_html=True)

    st.markdown("## ¿Qué es el modelo de regresión?")
    st.markdown("""
    El modelo de regresión es un tipo de algoritmo de Machine Learning utilizado para predecir un valor continuo basado en los datos de entrada.  
    En este caso, hemos entrenado un modelo que predice los **??** según la **??** de un servicio de transporte público.

    La **limpieza de datos** que se realizó para este modelo es la misma que se llevó a cabo durante el **Análisis Exploratorio de Datos (EDA)**. A partir de este punto, el dataset fue modificado para prepararlo para la regresión.
    """)

    st.markdown("##  Preparación de Datos para el Modelo de Regresión")
    st.markdown(""" 
    Los siguientes pasos fueron realizados en el dataset para prepararlo para el modelo de regresión:
    """)

    st.markdown("1. **Filtramos el dataset** para seleccionar solo las columnas de interés.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("2. **Revisamos el head del dataset** para verificar las primeras filas.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("3. **Revisamos la distribución de ingresos por mes** para entender cómo varían a lo largo del tiempo.")
    mostrar_imagen("distribucion_ingresos_por_mes_regresion.png")
    st.markdown("### Gráfico")
    mostrar_imagen("poner_nombre_imagen.png")


    st.markdown("## Creación del Modelo de Regresión")
    st.markdown("""
       Una vez preparados los datos, procedimos con los siguientes pasos para crear nuestro modelo de regresión:
       """)
    st.markdown("1. **Creación de las variables X y Y (variable objetivo)**.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("2. **Escalado de los datos de X** para mejorar el rendimiento del modelo.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("3. **Benchmarking**: Comparamos el rendimiento de diferentes modelos de regresión para seleccionar el mejor.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("##  La Mejor Opción Fue ")
    st.markdown("""
       Después de realizar el benchmarking, encontramos que el **algoritmo** fue el mejor modelo para predecir los XXXX.
       Los pasos para entrenar y evaluar el modelo fueron los siguientes:
       """)
    st.markdown("1. **Entrenamos el modelo XXXX** con el dataset procesado.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("2. **Evaluamos el modelo** utilizando métricas como XXXX etc.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("## Probar el Modelo")
    st.markdown("""
       A continuación, cargamos el **dataset de prueba** y probamos el modelo entrenado. Los pasos fueron los siguientes:
       """)
    st.markdown("1. **Cargamos el dataset de prueba**.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("2. **Verificamos la predicción** comparando las etiquetas predichas con las etiquetas reales.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("3. **Resultados**.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("4. **Exportamos el modelo** en formato `XXXX` para usarlo en futuras predicciones.")
    mostrar_imagen("poner_nombre_imagen.png")

    st.markdown("## 🔍 Conclusiones")
    st.markdown("""
    - XXXX
    - XXXX
    - XXXX.
    """)

def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Carga una imagen desde la carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
