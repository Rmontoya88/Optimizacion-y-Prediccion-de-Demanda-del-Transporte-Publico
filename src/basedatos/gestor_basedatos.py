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

class Tarifas_Historicas(Base):
    __tablename__ = 'tarifas_historicas'
    id = Column(Integer, primary_key=True,autoincrement=True)
    servicio = Column(String)
    recorrido = Column(String)
    tarifaregular = Column(SmallInteger)
    resolucion = Column(String)
    fechapublicacionlagaceta = Column(Date)
    expediente = Column(String)

class Paradas_Servicio_Tren(Base):
    __tablename__ = 'paradas_tren'
    idparada = Column(Integer, primary_key=True)
    nombre = Column(String)
    provincia = Column(String)
    canton = Column(String)
    distrito = Column(String)
    codigodta = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)

class Pasajeros_Adultos_Mayores(Base):
    __tablename__ = 'pasajeros_adultos_mayores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    annio = Column(SmallInteger)
    mes = Column(String)
    totalpasajeros = Column(Integer)
    heredia_sj = Column(Integer)
    pavas_sanpedro = Column(Integer)
    sj_belen = Column(Integer)
    cartago_sj = Column(Integer)
    alaj_her = Column(Integer)

class Datos_ARESEP(Base):
    __tablename__ = 'datos_aresep'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigoderuta = Column(String)
    descripcionderuta = Column(String)
    mes = Column(Integer)
    annio = Column(Integer)
    tipodeequipo = Column(String)
    cantidadviajes = Column(DECIMAL(10,2))
    cantidadlocomotoras = Column(DECIMAL(10,2))
    cantidadvagones = Column(DECIMAL(10,2))
    usomensual = Column(DECIMAL(10,2))
    distanciarecorrida_km = Column(DECIMAL(10,2))
    consumo_combustible = Column(DECIMAL(10,2))
    cantidad_zapata_freno = Column(DECIMAL(10,2))
    tipo_zapata_freno = Column(String)
    lubricante_carter = Column(DECIMAL(10,2))
    tipo_lubricante_carter = Column(String)
    lubricante_compresor = Column(DECIMAL(10,2))
    tipo_lubricante_compresor = Column(String)
    lubricante_motor_diesel = Column(DECIMAL(10,2))
    tipo_lubricante_motor_diesel = Column(String)
    filtro_aire = Column(DECIMAL(10,2))
    tipo_filtro_aire = Column(String)
    filtro_primario = Column(DECIMAL(10,2))
    tipo_filtro_primario = Column(String)
    aceite_sist_hidraulico = Column(DECIMAL(10,2))
    tipo_aceite_sist_hidraulico = Column(String)

passw = quote_plus("LMtco26.08")
engine = create_engine(f"postgresql+psycopg2://postgres:{passw}@localhost:5432/Incofer", echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#Pasajeros
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

#Tarifas
df_tarifas = pd.read_csv(r"C:\Users\Fabiola\Documents\CUC\BigData\Programacion II\Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico\data\raw\Tarifas_históricas_de_tren.csv",encoding="utf-8-sig")
df_tarifas.columns =(
    df_tarifas.columns
    .str.strip()
    .map(lambda x: unidecode(x))
    .str.replace(" ","",regex=True)
    .str.lower()
)

df_tarifas = df_tarifas.rename(columns ={
    "servicio":"servicio",
    "recorrido":"recorrido",
    "tarifaregular(c/)":"tarifaregular",
    "resolucion":"resolucion",
    "fechapublicacionlagaceta":"fechapublicacionlagaceta",
    "expediente":"expediente"
})
df_tarifas.to_sql("tarifas_historicas", engine, if_exists='append',index=False)
df_test1 = pd.read_sql("Select * from tarifas_historicas",engine)

#Paradas
df_paradas = pd.read_csv(r"C:\Users\Fabiola\Documents\CUC\BigData\Programacion II\Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico\data\raw\Paradas_del_servicio_del_tren.csv",encoding="utf-8-sig")
df_paradas.columns =(
    df_paradas.columns
    .str.strip()
    .map(lambda x: unidecode(x))
    .str.replace(" ","",regex=True)
    .str.lower()
)

df_paradas = df_paradas.rename(columns ={
    "idparada":"idparada",
    "nombre":"nombre",
    "provincia":"provincia",
    "canton":"canton",
    "distrito":"distrito",
    "codigodta":"codigodta",
    "x":"x",
    "y":"y"
})
df_paradas.to_sql("paradas_tren", engine, if_exists='append',index=False)
df_test2 = pd.read_sql("Select * from paradas_tren",engine)

#Adultos Mayores
df_adult_may = pd.read_csv(r"C:\Users\Fabiola\Documents\CUC\BigData\Programacion II\Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico\data\raw\Pasajeros_adultos_mayores_movilizados.csv",encoding="utf-8-sig")
df_adult_may.columns =(
    df_adult_may.columns
    .str.strip()
    .map(lambda x: unidecode(x))
    .str.replace(" ","",regex=True)
    .str.lower()
)
df_adult_may = df_adult_may.rename(columns ={
    "ano":"annio",
    "mes":"mes",
    "totalpasajeros":"totalpasajeros",
    "heredia-sanjose":"heredia_sj",
    "pavas-sanpedro":"pavas_sanpedro",
    "sanjose-belen":"sj_belen",
    "cartago-sanjose":"cartago_sj",
    "alajuela-heredia":"alaj_her"
})

df_adult_may.to_sql("pasajeros_adultos_mayores", engine, if_exists='append',index=False)
df_test3 = pd.read_sql("Select * from pasajeros_adultos_mayores",engine)

#Datos de ARESEP
df_aresep = pd.read_csv(r"C:\Users\Fabiola\Documents\CUC\BigData\Programacion II\Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico\data\raw\Datos_Abiertos_ARESEP_Estadísticas_rendimiento.csv",encoding="utf-8-sig")
df_aresep.columns =(
    df_aresep.columns
    .str.strip()
    .map(lambda x: unidecode(x))
    .str.replace(" ","",regex=True)
    .str.lower()
)

df_aresep = df_aresep.rename(columns ={
    "codigoderuta":"codigoderuta",
    "descripcionderuta":"descripcionderuta",
    "mes":"mes",
    "ano":"annio",
    "tipodeequipo":"tipodeequipo",
    "cantidaddeviajes":"cantidadviajes",
    "cantidaddelocomotoras":"cantidadlocomotoras",
    "cantidaddevagones":"cantidadvagones",
    "usomensual(h)":"usomensual",
    "distanciarecorrida(km)": "distanciarecorrida_km",
    "consumodecombustible(l)": "consumo_combustible",
    "cantidaddezapatafreno": "cantidad_zapata_freno",
    "tipodezapatafreno": "tipo_zapata_freno",
    "lubricantecarter(l)": "lubricante_carter",
    "tipodelubricantecarter": "tipo_lubricante_carter",
    "lubricantecompresor(l)": "lubricante_compresor",
    "tipodelubricantecompresor": "tipo_lubricante_compresor",
    "lubricantemotordiesel(l)": "lubricante_motor_diesel",
    "tipodelubricantemotordiesel": "tipo_lubricante_motor_diesel",
    "filtroaire": "filtro_aire",
    "tipodefiltroaire": "tipo_filtro_aire",
    "filtroprimario": "filtro_primario",
    "tipodefiltroprimario": "tipo_filtro_primario",
    "aceitesistemahidraulico": "aceite_sist_hidraulico",
    "tipodeaceitesistemahidraulico": "tipo_aceite_sist_hidraulico"
})
df_aresep['aceite_sist_hidraulico'] = df_aresep['aceite_sist_hidraulico'].fillna(0)
df_aresep.to_sql("datos_aresep", engine, if_exists='append',index=False)
df_test4 = pd.read_sql("Select * from datos_aresep",engine)
print(df_test4)