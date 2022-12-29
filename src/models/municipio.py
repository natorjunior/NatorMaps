import pandas as pd
import sqlalchemy
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import numpy as np
import requests
from tqdm.auto import tqdm
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///natorMaps.db', echo=False)
Base = declarative_base()
class Municipio(Base):
    __tablename__ = 'municipio' # campo obrigatório
    id = Column(Integer, primary_key=True) # campo obrigatório
    malha = Column(String(100000))
    malha_g = Column(String(100000))
    nome_municipio = Column(String(100))
    codigo_ibge = Column(String(100))
    cor_do_municipio = Column(String(100))
    name_funcao_click = Column(String(100))
    caixa_de_texto = Column(String(400))
    ano_de_referencia = Column(String(20))
    uf = Column(String(20))
    codigo_uf = Column(Integer)
    populacao_estimada = Column(Integer)
    onclick=False 
    hover=False
    """
        Funcao para calcular e retornar os municipios
    """
    def retornar_municipios(self):
        pass
    """
        Funcao para ler as malhas de acordo com o ano de referencia
    """
    def load_malhas():
        pass
    """ 
        funcao para retornar o mapa em formato de string
    """
    def retornar_mapa_str(self,tipo: str, dados: pd.DataFrame) -> str:
        pass