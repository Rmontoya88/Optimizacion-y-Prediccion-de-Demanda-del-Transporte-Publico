from sqlalchemy import create_engine, Column, Integer,DECIMAL, String, Date, ForeignKey, SmallInteger, column
from sqlalchemy.orm import relationship, sessionmaker,declarative_base
import pandas as pd
from unidecode import unidecode
from urllib.parse import quote_plus
import psycopg2


Base = declarative_base()

class Pasajeros_TrenUrbano(Base):
    __tablename__ = 'pasajeros_trenurbano'
    id = Column(Integer, primary_key=True,autoincrement=True)
    codigoruta = Column(String)
    descripcionruta = Column(String)
    codigorecorrido = Column(String)
    descripcionrecorrido = Column(String)
    sentido = Column(String)
    dia = Column(SmallInteger)
    mes = Column(SmallInteger)
    annio = Column(SmallInteger)
    cantidadpasajerosreg = Column(SmallInteger)
    cantidadadultosmay = Column(SmallInteger)
    ingresos = Column(DECIMAL(10,2))

passw = quote_plus("LMtco26.08")
engine = create_engine(f"postgresql+psycopg2://postgres:{passw}@localhost:5432/Incofer", echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
df_pasajeros = pd.read_csv( r"C:\Users\Fabiola\Documents\CUC\BigData\Programacion II\Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico\data\raw\Tren_urbano_pasajeros.csv",encoding="utf-8-sig")

df_pasajeros.columns =(
    df_pasajeros.columns
    .str.strip()
    .map(lambda x: unidecode(x))
    .str.replace(" ","",regex=True)
    .str.lower()
)
#Renombrar columnas
df_pasajeros = df_pasajeros.rename(columns ={
    "codigoderuta":"codigoruta",
    "descripciondelaruta":"descripcionruta",
    "codigorecorrido":"codigorecorrido",
    "descripciondelrecorrido":"descripcionrecorrido",
    "sentido":"sentido",
    "dia":"dia",
    "mes":"mes",
    "ano":"annio",
    "cantidaddepasajerosregulares":"cantidadpasajerosreg",
    "cantidaddeadultosmayores":"cantidadadultosmay",
    "ingresos":"ingresos"
})
df_pasajeros.columns =df_pasajeros.columns.str.lower()

df_pasajeros['cantidadadultosmay'] = df_pasajeros['cantidadadultosmay'].fillna(0)
#print(df_pasajeros.columns)
df_pasajeros.to_sql("pasajeros_trenurbano", engine, if_exists='append',index=False)
#Verificar que se insertaran los datos
df_test = pd.read_sql("Select * from pasajeros_trenurbano",engine)
print(df_test)
