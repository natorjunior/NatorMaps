from .interface import IAcoes
from .Municipio import Municipio

class Estado(IAcoes):
    def __init__(self):
        self.nome_estado   = ''
        self.codigo_estado = ''
        self.view_box = ''
        self.municipios =  Municipio