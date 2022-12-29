from abc import ABC, abstractclassmethod

class IAcoes(ABC):
   
    @abstractclassmethod
    def retornar_mapa_str(self, competencia):
        pass
    @abstractclassmethod
    def retornar_mapa_array(self, competencia):
        pass
    @abstractclassmethod
    def retornar_mapa(self, ano_de_referencia:str,nome:str):
        pass