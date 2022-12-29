import pandas as pd
import numpy as np
import sqlalchemy
from tqdm.auto import tqdm
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import sessionmaker
engine = sqlalchemy.create_engine('sqlite:///natorMaps.db', echo=False)
Base = declarative_base()
class Municipio(Base):
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
class DB:
    def __init__(self) -> None:
        self.engine = engine
        self.Base = Base
        self.malhas = np.load('src/data/malhas_brazil.npy', allow_pickle='TRUE').all()
        self.df_popBR = {2021:pd.read_excel(
            "src/data/popBR.xls",
            sheet_name='Municípios',
            header=1,
            nrows=5570, 
            dtype = {'UF': str, 'COD. UF': str, 'COD. MUNIC': str}
        )}

    """
        Criando a base de dados e tabela para municipiosdos municipios 
    """
    def criando_db_municipios(self):
        Base.metadata.create_all(engine)
        print('Base de dados criada')
    """
        Funcao para popular a tabela de municipios
    """
    def salvando_dados_na_base(self,ano_referencia=2021):
        df = self.df_popBR[ano_referencia]
        malhas = self.malhas
        #criando uma coluna que unifica o código da UF com o código do municipio
        df['cod_ibge'] = df[["COD. UF","COD. MUNIC"]].T.apply(lambda x: x[0]+x[1])

        Session = sessionmaker(bind=engine)
        session = Session()
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
                    #print('***************************')
                    session.add(municipio)
            except:
                pass
                #print('',end='.')
            #print(municipio.__dict__)
            #break
        session.commit() #Salvando o dado no banco de dados
        session.close() 