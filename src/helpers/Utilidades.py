import folium
from pyproj import Transformer
import os


class GenerarMapa:
    def __init__(self, df):
        self.df = df

    def _convertir_coordenadas(self):
        """Convierte coordenadas de CRTM05 (EPSG:5367) a WGS84 (EPSG:4326)."""
        transformer = Transformer.from_crs("EPSG:5367", "EPSG:4326", always_xy=True)
        self.df["Longitud"], self.df["Latitud"] = transformer.transform(
            self.df["x"].values, self.df["y"].values
        )

    def crear_mapa(self, zoom_start=11):
        # Crea el mapa de paradas de tren.
        self._convertir_coordenadas()

        map_center = [self.df['Latitud'].mean(), self.df['Longitud'].mean()]
        m = folium.Map(location=map_center, zoom_start=zoom_start)

        for _, row in self.df.iterrows():
            popup = folium.Popup(
                f"<b>🚉 {row['nombre']}</b><br>"
                f"📍 Provincia: {row['provincia']}<br>"
                f"🏙️ Cantón: {row['canton']}<br>"
                f"🗺️ Distrito: {row['distrito']}",
                max_width=300
            )
            folium.Marker(
                location=[row['Latitud'], row['Longitud']],
                popup=popup,
                tooltip=row['nombre'],
                icon=folium.Icon(color="red", icon="train", prefix="fa")
            ).add_to(m)

        self.mapa = m
        return m

    def guardar_mapa(self, ruta_salida):
        #Guarda el mapa

        ruta_salida = os.path.abspath("ruta_salida")
        self.mapa.save(ruta_salida)
        print(f"✅ Mapa guardado en: {ruta_salida}")