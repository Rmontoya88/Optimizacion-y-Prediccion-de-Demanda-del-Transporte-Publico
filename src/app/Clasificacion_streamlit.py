import streamlit as st
import os


def mostrar_modelo_clasificacion():
    st.markdown("# Modelo de Clasificación", unsafe_allow_html=True)

    st.markdown("##  ¿Qué es el modelo de clasificación?")
    st.markdown("""
    El modelo de clasificación es un tipo de algoritmo de Machine Learning utilizado para asignar etiquetas o categorías a los datos de entrada.  
    En este caso, hemos entrenado un modelo que predice los **rangos de ingresos** según la **ruta** de un servicio de transporte público.

    La **limpieza de datos** que se realizó para este modelo es la misma que se llevó a cabo durante el **Análisis Exploratorio de Datos (EDA)**. A partir de este punto, el dataset fue modificado para prepararlo para la clasificación.
    """)

    st.markdown("##  Preparación de Datos para el Modelo de Clasificación")
    st.markdown("""
    Los siguientes pasos fueron realizados en el dataset para prepararlo para el modelo de clasificación:
    """)

    st.markdown("1. **Filtramos el dataset** para seleccionar solo las columnas de interés.")
    mostrar_imagen("data_filtrado_modeloC.png")

    st.markdown("2. **Revisamos el head del dataset** para verificar las primeras filas.")
    mostrar_imagen("head_dataset_modeloC.png")

    st.markdown("3. **Revisamos la distribución de ingresos por mes** para entender cómo varían a lo largo del tiempo.")
    mostrar_imagen("distribucion de ingresos por mes.png")
    st.markdown("### Gráfico")
    mostrar_imagen("distribucion de ingresos por mes_grafico.png")

    st.markdown("4. **Analizamos la tendencia de adultos mayores con el tiempo** para ver si hay patrones.")
    mostrar_imagen("tendencia_adultos_modeloC.png")
    st.markdown("### Gráfico")
    mostrar_imagen("tendencia_adultos_modeloC_grafico.png")

    st.markdown("5. **Se calcularon las estadísticas básicas de la columna 'Ingresos'** para tener una visión general de la distribución.")
    mostrar_imagen("ingresos_columna_modeloC.png")

    st.markdown(
        "6. **Creamos una nueva columna de 'Ingresos'** basada en los rangos de ingresos definidos a partir de las estadísticas básicas.")
    mostrar_imagen("ingresos_transfor_modeloC.png")

    st.markdown(
        "7. **Realizamos la transformación de las variables categóricas**, como las rutas y otras variables relacionadas.")
    mostrar_imagen("ingresos_transfor_modeloC_grafico.png")

    st.markdown(
        "8. **Verificamos la distribución de la variable objetivo**, es decir, los rangos de ingresos predichos.")
    mostrar_imagen("distribucion_modeloC.png")

    st.markdown("## ️ Creación del Modelo de Clasificación")
    st.markdown("""
       Una vez preparados los datos, procedimos con los siguientes pasos para crear nuestro modelo de clasificación:
       """)
    st.markdown("1. **Creación de las variables X y Y (variable objetivo)**.")
    mostrar_imagen("xy_modeloC.png")

    st.markdown("2. **Escalado de los datos de X** para mejorar el rendimiento del modelo.")
    mostrar_imagen("x_escalado_modeloC.png")

    st.markdown(
        "3. **Benchmarking**: Comparamos el rendimiento de diferentes modelos de clasificación para seleccionar el mejor.")
    mostrar_imagen("benchmarking_modeloC.png")

    st.markdown("##  La Mejor Opción Fue el Random Forest")
    st.markdown("""
       Después de realizar el benchmarking, encontramos que el **Random Forest** fue el mejor modelo para predecir los rangos de ingresos.
       Los pasos para entrenar y evaluar el modelo fueron los siguientes:
       """)
    st.markdown("1. **Entrenamos el modelo Random Forest** con el dataset procesado.")
    mostrar_imagen("entreno_modeloC.png")

    st.markdown("2. **Evaluamos el modelo** utilizando métricas como la precisión, matriz de confusión, y curva ROC.")
    mostrar_imagen("evaluar_modeloC.png")

    st.markdown("##  Probar el Modelo")
    st.markdown("""
       A continuación, cargamos el **dataset de prueba** y probamos el modelo entrenado. Los pasos fueron los siguientes:
       """)
    st.markdown("1. **Cargamos el dataset de prueba**.")
    mostrar_imagen("probar_modeloC.png")

    st.markdown("2. **Verificamos la predicción** comparando las etiquetas predichas con las etiquetas reales.")
    mostrar_imagen("prediccion_modeloC.png")

    st.markdown("1. **Resultados**.")
    mostrar_imagen("ejemplo_prediccion_modeloC.png")

    st.markdown("3. **Exportamos el modelo** en formato `.pkl` para usarlo en futuras predicciones.")
    mostrar_imagen("exportar_modeloC.png")

    st.markdown("##  Conclusiones")
    st.markdown("""
    - El **modelo Random Forest** demostró ser el más adecuado para la predicción de los rangos de ingresos.
    - El modelo tiene una **precisión del 98%**, lo cual es una indicación de su buen desempeño.
    - Se realizaron ajustes adicionales para mejorar la **precisión**.
    """)

def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Carga una imagen desde la carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
