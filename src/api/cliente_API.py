import requests
import pandas as pd
import streamlit as st

class ClienteAPI:
    base_url ="https://datos.aresep.go.cr/ws.datosabiertos/Services/IT/Ferrocarril.svc/ObtenerInformacionLineaPorDistritoMapa"

    def obtenerInformacionLineaPorDistritoMapa(self):
        response = requests.get(self.base_url)

        if response.status_code == 200:
            print("Datos obtenidos exitosamente.")
            data = response.json()
            columns = [col['field'] for col in data['metadata']['gridColumns']]
            #df = pd.json_normalize(data)
            rows = data['value']
            df = pd.DataFrame(rows, columns=columns)

            st.write(df.head())
            return df
        else:
            print(f"Error al obtener datos: {response.status_code}")
