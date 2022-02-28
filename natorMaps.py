import requests
import pandas as pd
from tqdm import tqdm
import random
class NatorMaps:
    def __init__(self):
        pass
    class MapCities:
        def __init__(self):
            self.svg_head = '<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.2" baseProfile="tiny" width="1080" height="1080" viewBox="-43.796 22.7461 0.6940999999999988 0.3362000000000016" stroke-linecap="round" stroke-linejoin="round">'
            self.url_base = 'https://servicodados.ibge.gov.br/api/v3/malhas/municipios/'
        def to_svg(self,df_cities,path_name_file='default', stroke='gray',stroke_width="6", fill= 'black'):
            svg_head = self.svg_head[:]
            for county in tqdm(range(len(df_cities.values))):
                #faz a busca do municipio na base do ibge, pelo código do IBGE
                r_county = requests.get(self.url_base+df_cities["code"].iloc[county])
                if len(r_county.text)!=0:
                    # busca o inicio e o fim da path, com os identificadores <g> </g>
                    start,end = r_county.text.find('<g'),r_county.text.find('</g>')
                    #separa apenas o path da chamada
                    county_aux = r_county.text[start:end]+'</g>'
                    #faz um corte no parametro transforme do path, para inclusão de novos parametros
                    list_aux = county_aux.split('transform')
                    #verifica se o dataframe veio com o parametro fill, caso contrario é definido o default ou de cor única
                    if list(df_cities.columns).count('fill')>0:
                        #define a cor de um municipio, de acordo com a predefinição
                        if df_cities["fill"].iloc[county] != '':
                            list_aux.insert(1,f'fill="{df_cities["fill"].iloc[county]}"')
                        else:
                            list_aux.insert(1,f'fill="{fill}"')
                    else:
                        #define a cor do municipio, com o default ou uma cor definidas pra todos
                        list_aux.insert(1,f'fill="{fill}"')
                    #insere o strok do municipio
                    list_aux.insert(1,f'stroke="{stroke}"')
                    #insere o tamanho do stroke do municipio
                    list_aux.insert(1,f'stroke-width="{stroke_width}"')
                    #inclui a string "tranform" ao seu lugar devido 
                    list_aux[4] = 'transform'+list_aux[4]
                    #tranaforma a lista em uma string novamente
                    county_aux = ' '.join(list_aux)
                    #Salva o municipio configurado
                    svg_head += county_aux
                else:
                    print('Erro na requisição, código inválido ou API do IBGE indisponível')
            svg_head += '</svg>'
            if path_name_file == 'default':
                hash = random.getrandbits(128)
                path_name_file = "%032x" % hash
            print(f'arquivo {path_name_file}.svg salvo com sucesso')
            f = open(path_name_file+".svg", "w")
            f.write(svg_head)
            f.close()
            #return svg_head
    class MapEstates:
        def __init__(self):
            pass
        def to_svg(self,df_cities, stroke='gray',stroke_width="6", fill= 'black'):
            pass