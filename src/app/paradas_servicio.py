import streamlit as st
import folium
import pandas as pd
from pyproj import Transformer
from streamlit_folium import st_folium

def mostrar_paradas_servicio(df_mapa_locomotoras):

    st.markdown(""" 
    Aquí se visualizan las ubicaciones geográficas de las paradas de servicio.
    """)

    def crear_mapa(df, zoom_start=11):
        # Convertir coordenadas de CRTM05 a WGS84
        transformer = Transformer.from_crs("EPSG:5367", "EPSG:4326", always_xy=True)
        df["Longitud"], df["Latitud"] = transformer.transform(df["X"].values, df["Y"].values)

        # Centrar el mapa en las coordenadas promedio
        map_center = [df['Latitud'].mean(), df['Longitud'].mean()]
        m = folium.Map(location=map_center, zoom_start=zoom_start)

        # Agregar marcadores al mapa
        for _, row in df.iterrows():
            popup = folium.Popup(
                f"<b>🚉 {row['Nombre']}</b><br>"
                f"📍 Provincia: {row['Provincia']}<br>"
                f"🏙️ Cantón: {row['Cantón']}<br>"
                f"🗺️ Distrito: {row['Distrito']}",
                max_width=300
            )
            folium.Marker(
                location=[row['Latitud'], row['Longitud']],
                popup=popup,
                tooltip=row['Nombre'],
                icon=folium.Icon(color="red", icon="train", prefix="fa")
            ).add_to(m)

        return m

    # mostrar el mapa
    def mostrar_mapa(df):
        mapa = crear_mapa(df)
        st_folium(mapa, width=700)

    # Cargar el dataset
    try:
        df = pd.read_csv('D:/cuc/programacion 2/Proyecto Final/Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico/data/raw/Paradas_del_servicio_del_tren.csv')
        mostrar_mapa(df)
    except Exception as e:
        st.error(f"Error al cargar el archivo CSV: {e}")

