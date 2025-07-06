""" docstring import"""
from .src.mapa import Mapa
from .src.db.db import DB
db = DB()
#cria a tabela e a base de dados
db.criando_db_municipios()
#popula a tabela municipios
db.salvando_dados_na_base()
mapa = Mapa(db)
m = mapa.retornar_mapa('ESTADO',"CE")
with open('CE.svg', 'w', encoding="utf-8") as f:
    f.write(m)
    f.close()
