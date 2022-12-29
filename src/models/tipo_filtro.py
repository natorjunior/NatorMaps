from .interface import IAcoes
from ..micro import Micro
from ..macro import Macro
from ..estado import Estado

class TipoFiltro():
    def __init__(self,db):
        self.estado = "ESTADO"
        self.micro = "MICRO"
        self.macro = "MACRO"
        self.estado_object = Estado(db)
        self.micro_object = Micro(db)
        self.macro_object = Macro(db)

    def retornar_tipo_filtro(self, tipo: str):
        map = {
            self.estado: self.estado_object,
            self.micro: self.micro_object,
            self.macro: self.macro_object
        }
        return map[tipo]