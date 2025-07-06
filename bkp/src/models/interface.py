"""docstring"""
from abc import ABC, abstractclassmethod

class IAcoes(ABC):
    """docstring"""
    @classmethod
    @abstractclassmethod
    def retornar_mapa_str(cls, competencia):
        """docstring"""
    @classmethod
    @abstractclassmethod
    def retornar_mapa_array(cls, competencia):
        """docstring"""
    @classmethod
    @abstractclassmethod
    def retornar_mapa(cls, ano_de_referencia:str,nome:str):
        """docstring"""
