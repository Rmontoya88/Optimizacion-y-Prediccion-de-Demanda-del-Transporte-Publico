# 🚆 Proyecto 1: Optimización y Predicción de Demanda del Transporte Público

Este proyecto busca analizar patrones de uso del transporte público en Costa Rica para **predecir la cantidad de pasajeros** y **optimizar la frecuencia del servicio**, contribuyendo a una gestión más eficiente y sostenible del sistema ferroviario.

---

## 📊 Descripción

Se realiza un análisis exploratorio de datos (EDA), visualización y desarrollo de modelos de *machine learning* para:

- 🔹 Predecir la demanda de pasajeros  
- 🔹 Clasificar el nivel de ocupación del servicio  
- 🔹 Optimizar horarios y rutas según los patrones detectados

---

## 🗂️ Fuentes de Datos

- 📁 CSV (Estadísticas de INCOFER):  
  [https://datos.incofer.go.cr/dataset/estadisticas-pasajeros](https://datos.incofer.go.cr/dataset/estadisticas-pasajeros)

- 📅 API de feriados en Costa Rica:  
  [https://api-feriados-cr.herokuapp.com/api/2025](https://api-feriados-cr.herokuapp.com/api/2025)

- 🛢️ Base de datos PostgreSQL:  
  Contiene datos históricos por estación y validaciones cruzadas de ocupación.

---

## 📈 Análisis Exploratorio (EDA) y Visualización

Incluye gráficos de tendencias, patrones estacionales, mapas de calor y análisis de correlación entre variables.

---

## 🤖 Modelos Supervisados

### 🔹 Regresión – Predicción de pasajeros

**Algoritmos utilizados:**

- Regresión Lineal  
- K-Nearest Neighbors (KNN)  
- Random Forest  
- XGBoost

**Variables de entrada:**

- Fecha y hora
- Estación
- Día de la semana
- Feriado (sí/no)
- Historial de demanda

**Variable objetivo:**

- Número de pasajeros

---

### 🔸 Clasificación – Nivel de ocupación del servicio

**Algoritmos utilizados:**

- Regresión Logística  
- Árbol de Decisión  
- Random Forest  

**Variables de entrada:**

- Fecha y hora
- Estación
- Día de la semana
- Feriado (sí/no)
- Historial de ocupación

**Variable objetivo:**

- Nivel de ocupación (Bajo, Medio, Alto)

---


