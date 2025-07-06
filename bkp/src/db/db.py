"""docstring"""
import pandas as pd
import numpy as np
import sqlalchemy
from tqdm.auto import tqdm
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
engine = sqlalchemy.create_engine('sqlite:///natorMaps.db', echo=False)
Base = declarative_base()
class Municipio(Base):
    """docstring"""
    __tablename__ = 'municipio' # campo obrigatório
    id = Column(Integer, primary_key=True) # campo obrigatório
    id = Column(Integer, primary_key=True) # campo obrigatório
    malha = Column(String(100000))
    malha_g = Column(String(100000))
    view_box_malha = Column(String(100))
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
class DB:
    """docstring"""
    def __init__(self) -> None:
        self.engine = engine
        self.base = Base
        self.malhas = np.load('src/data/malhas_brazil.npy', allow_pickle='TRUE').all()
        self.df_pop_br = {2021:pd.read_excel(
            "src/data/popBR.xls",
            sheet_name='Municípios',
            header=1,
            nrows=5570,
            dtype = {'UF': str, 'COD. UF': str, 'COD. MUNIC': str}
        )}

    def criando_db_municipios(self)->None:
        """Criando a base de dados e tabela para municipiosdos municipios"""
        self.base.metadata.create_all(engine)
        print('Base de dados criada')
    def salvando_dados_na_base(self,ano_referencia=2021):
        """Funcao para popular a tabela de municipios"""
        df = self.df_pop_br[ano_referencia]
        malhas = self.malhas
        #criando uma coluna que unifica o código da UF com o código do municipio
        df['cod_ibge'] = df[["COD. UF","COD. MUNIC"]].T.apply(lambda x: x[0]+x[1])

        session_object = sessionmaker(bind=engine)
        session = session_object()
        #percorrendo todos os municipios e salvando os dados
        for i,row in tqdm(df.iterrows()):
            try:
                uf,cod_uf,cod_mun,nome_municipio,populacao_estimada,codigo_ibge = row.values
                malha = malhas[codigo_ibge]
                start,end = malha.find('<g'),malha.find('</g>')
                viewbox = malha.split('viewBox="')[1].split('" stroke-linecap=')[0]
                #cria o objeto para que em seguida seja salvo no banco.
                municipio = Municipio(
                    id = codigo_ibge,
                    malha = malha,
                    malha_g = malha[start:end+4],
                    view_box_malha = viewbox,
                    nome_municipio = nome_municipio,
                    codigo_ibge = codigo_ibge,
                    cor_do_municipio = '',
                    name_funcao_click = '',
                    caixa_de_texto = '',
                    ano_de_referencia = ano_referencia,
                    uf = uf,
                    codigo_uf = cod_uf,
                    populacao_estimada = populacao_estimada,
                )
                #verifica a existencia do dado na base
                verify = session.query(Municipio).filter_by(
                    id = codigo_ibge,
                    codigo_ibge = codigo_ibge,
                    ano_de_referencia = ano_referencia,
                    uf = uf,
                    codigo_uf = cod_uf
                ).first()
                if not verify:
                    session.add(municipio)
            except NameError:
                pass
        session.commit() #Salvando o dado no banco de dados
        session.close()
