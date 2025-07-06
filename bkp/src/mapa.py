from .models.tipo_filtro import TipoFiltro
class Mapa:
    def __init__(self, db, ano_de_referencia="2021"):
        self.tipo = TipoFiltro(db)
        self.ano_de_referencia = ano_de_referencia
    def retornar_mapa(self,tipo: str, sigla_nome:str) -> str:
        return self.tipo.retornar_tipo_filtro(tipo).retornar_mapa(self.ano_de_referencia, sigla_nome) 