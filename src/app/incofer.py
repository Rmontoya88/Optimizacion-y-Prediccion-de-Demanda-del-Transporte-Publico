import streamlit as st
import base64
import os

def get_base64_image(image_name):
    dir_path = os.path.dirname(__file__)
    image_path = os.path.join(dir_path, "imagenes", image_name)
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def mostrar_historia():
    img_base64 = get_base64_image("fondo.jpg")

    st.markdown(
        f"""
<style>
.stApp {{
    background-image:
        linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)),
        url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
}}

/* Texto general blanco */
.stApp, .stMarkdown {{
    color: white !important;
}}

/* Títulos */
h1 {{
    color: #ff0000 !important;  /* rojo intenso */
    font-weight: 700;
}}

h2 {{
    color: #FFD700 !important;  /* amarillo intenso */
    font-weight: 700;
}}

h3 {{
    color: #FFFFFF !important;  /* blanco */
    font-weight: 700;
}}
</style>
""",
unsafe_allow_html=True
)

    st.markdown("# Nuestra Historia")

    st.markdown("""
**El Instituto Costarricense de Ferrocarriles**, creado por la **Ley Nº 7001**, del 19 de setiembre de 1985, es una institución de derecho público, con autonomía administrativa, personalidad jurídica y patrimonio propio, y se rige por las disposiciones establecidas en dicha ley y sus reglamentos, así como en las leyes que la complementen.

---

**Crisis y cierre técnico (1990 - 1995)**  
Entre 1990 y 1995, la actividad ferroviaria se vio sumida en una profunda crisis económica, por las altas deudas que no se podían cubrir. Se decide realizar un “cierre técnico”, suspendiendo los servicios del ferrocarril en todo el territorio nacional. A los trabajadores se les paga la cesantía y solo quedan algunos para salvaguarda de los activos ferroviarios. Este cierre se efectúa mediante el Acuerdo **SCD-106-95** del 28 de junio de 1995, dictado por el Consejo de Gobierno del entonces Presidente de la República, **José María Figueres Olsen**.

---

**Reactivación en 1998**  
El Gobierno del **Lic. Miguel Ángel Rodríguez Echeverría** emite el **Decreto Nº 035 del 9 de setiembre de 1998**, acordando la reanudación del servicio ferroviario para personas y carga, comenzando por la región Atlántica.

---

**Fortalecimiento legal (2016)**  
El 7 de junio de 2016, se aprueba en la Asamblea Legislativa la nueva ley para el:  
**FORTALECIMIENTO DEL INSTITUTO COSTARRICENSE DE FERROCARRILES (INCOFER)**  
y promoción del **Tren Eléctrico Interurbano de la Gran Área Metropolitana**.

Se reforma el artículo 3º de la Ley 7001, estableciendo como objetivo del INCOFER:

> “...Fortalecer la economía del país mediante la administración de un moderno sistema de transporte ferroviario para el servicio de pasajeros y de carga...”.

---

**Actualidad**  
Los esfuerzos de reactivación gradual han dado frutos, lo cual se evidencia en las estadísticas de evolución de los servicios de transporte de pasajeros, carga y turistas.

---

## **Transporte de Pasajeros en el Gran Área Metropolitana:**
- San José - Heredia - San José  
- Metrópoli III: Pavas - Curridabat - Pavas  
- San José - San Antonio de Belén - San José  
- San José - Cartago - San José  
- Alajuela - Heredia - Alajuela  

### **Servicio Turístico:**
- Transporte turístico en Limón
    """, unsafe_allow_html=True)
