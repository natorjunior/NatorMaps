from abc import ABC, abstractclassmethod

class IAcoes(ABC):
   
    @abstractclassmethod
    def retornar_municipios(self,competencia):
        pass