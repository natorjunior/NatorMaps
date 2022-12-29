from .models.interface import IAcoes
import pandas as pd
class Micro(IAcoes):
    def __init__(self,db):
        self.db = db
    """ 
        funcao para retornar o mapa em formato de string
    """
    def retornar_mapa_str(self,tipo: str, dados: pd.DataFrame) -> str:
        pass
    def retornar_mapa_array(self):
        pass
    def retornar_mapa(self,ano_de_referencia,nome):
        pass