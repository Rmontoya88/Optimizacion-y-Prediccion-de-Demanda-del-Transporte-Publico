from numpy import integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus
import pyodbc


print(pyodbc.drivers())
Base = declarative_base()

class GestorDatos:
    def __init__(self):
        self.passw = quote_plus("LMtco26.08")
        self.engine = create_engine(f"postgresql+psycopg2://postgres:{self.passw}@localhost:5432/Incofer", echo=True)
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def ObtencionPasajerosTrenUrbano(self):
        df = pd.read_sql("Select * from pasajeros_trenurbano", self.engine)
        return df

    def ObtencionPasajerosAdultosMayores(self):
        df = pd.read_sql("Select * from pasajeros_adultos_mayores",self.engine)
        return df

    def ObtencionTarifas(self):
        df = pd.read_sql("Select * from tarifas_historicas",self.engine)
        return df

    def ObtencionParadas(self):
        df = pd.read_sql("Select * from paradas_tren", self.engine)
        return df

    def ObtencionEstadisticaARESEP(self):
        df = pd.read_sql("Select * from datos_aresep", self.engine)
        return df

    def cerrar_sesion(self):
        self.session.close()