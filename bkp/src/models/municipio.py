"""docstring"""
import pandas as pd
import sqlalchemy
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base

engine = sqlalchemy.create_engine('sqlite:///natorMaps.db', echo=False)
Base = declarative_base()
class Municipio(Base):
    """docstring"""
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
    def retornar_municipios(self):
        """Funcao para calcular e retornar os municipios"""
    def load_malhas(self):
        """Funcao para ler as malhas de acordo com o ano de referencia"""

    def retornar_mapa_str(self,tipo: str, dados: pd.DataFrame) -> str:
        """funcao para retornar o mapa em formato de string"""
