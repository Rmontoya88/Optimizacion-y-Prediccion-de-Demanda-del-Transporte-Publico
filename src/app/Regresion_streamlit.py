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
    mostrar_imagen("data_filtrado_modeloR.png")

    st.markdown("2. **Revisamos el head del dataset** para verificar las primeras filas.")
    mostrar_imagen("head_dataset_modeloR.png")

    st.markdown("## Creación del Modelo de Regresión")
    st.markdown("""
       Una vez preparados los datos, procedimos con los siguientes pasos para crear nuestro modelo de regresión:
       """)
    st.markdown("1. **Creación de las variables X y Y (variable objetivo)**.")
    mostrar_imagen("data_filtrado_modeloR.png")

    st.markdown("2. Se realiza limpieza de posibles valores Nan y se representa a las variables categoricas como disyuntivas")
    mostrar_imagen("disy.png")

    st.markdown("3. Se realiza la verificación.")
    mostrar_imagen("verif.png")

    st.markdown("4. Se realiza imputacion usando el promedio.")
    mostrar_imagen("imputacion.png")

    st.markdown("5. Se realiza la division de los datos de entrenamiento y prueba.")
    mostrar_imagen("entrenamiento.png")

    st.markdown("6. Se indican la cantidad de arboles.")
    mostrar_imagen("forest.png")

    st.markdown("7. Se realiza el entrenamiento.")
    mostrar_imagen("regresion.png")

    st.markdown("8. Se obtiene el cross validation de los datos entrenados.")
    mostrar_imagen("validacionr.png")

    st.markdown("9. Se obtiene el score de; desempeño del modelo.")
    mostrar_imagen("desempeno.png")

    st.markdown("10. Se realiza una predicción.")
    mostrar_imagen("prediccionR.png")

    st.markdown("11. Coeficiente de determinación.")
    mostrar_imagen("coedeter.png")

    st.markdown("12. Coeficiente de determinación.")
    mostrar_imagen("coedeter.png")

    st.markdown("13. Datos separados para la prueba.")
    mostrar_imagen("x_prueba.png")

    st.markdown("14. Subconjuntos de variable objetivo, se verifica que tan bueno fue el modelo.")
    mostrar_imagen("y_test.png")

    st.markdown("15. Datos separados para la prueba.")
    mostrar_imagen("x_prueba.png")

    st.markdown("## 🔍 Conclusiones")
    st.markdown("""
    Utilizando el modelo RandomForest realizamos un entrenamiento a nuestro modelo y optuvimos un gran resultado para la predicción,
    un 0.88, siendo un modelo con capacidad de predicción.
    """)

def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Carga una imagen desde la carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
