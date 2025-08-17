import pandas as pd
import os


class ProcesadorEDA:
    def __init__(self, df):
        self.df = df

    def mostrar_head(self):
        """Devuelve las primeras 5 filas del DataFrame"""
        return self.df.head()

    def mostrar_tail(self):
        """Devuelve las últimas 5 filas del DataFrame"""
        return self.df.tail()

    def mostrar_info(self):
        """Devuelve la información general del DataFrame"""
        return self.df.info()

    def eliminar_columnas(self, columnas_a_eliminar):
        """Elimina las columnas especificadas y actualiza el DataFrame"""
        self.df = self.df.drop(columns=columnas_a_eliminar)
        print(f"Columnas eliminadas: {columnas_a_eliminar}")
        return self.df

    def mostrar_dimensiones(self):
        """Devuelve las dimensiones del DataFrame"""
        return self.df.shape


    def mostrar_resumen_descriptivo(self):
        """Devuelve el resumen descriptivo del DataFrame"""
        return self.df.describe()

    def rellenar_nulos(self):
        """Rellena los valores nulos con 0"""
        self.df = self.df.fillna(0)
        return self.df

    def mostrar_columnas(self):
        """Devuelve el resumen descriptivo del DataFrame"""
        return self.df.columns

    def analizar_nulos(self):

        print("\n" + "=" * 50)
        print("ANÁLISIS DE VALORES NULOS Y VACÍOS")
        print("=" * 50 + "\n")

        print("Valores nulos por columna:")
        print("-" * 50)
        print(self.df.isnull().sum())
        print("\n")

        print("Porcentaje de valores nulos por columna:")
        print("-" * 50)
        pct_nulos = (self.df.isnull().mean() * 100).round(2)
        print(pct_nulos)
        print("\n" + "=" * 50)

