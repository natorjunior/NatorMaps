import requests
import pandas as pd
from tqdm.auto import tqdm
import random
import time
from bs4 import BeautifulSoup
#bs = BeautifulSoup(open(xml_file), 'xml')
#pretty_xml = bs.prettify()
#print(pretty_xml)
class NatorMaps:
    def __init__(self):
        pass
    class MapCities:
        def __init__(self):
            self.svg_head = '<svg xmlns="http://www.w3.org/2000/svg" version="1.2" baseProfile="tiny" width="1080" height="1080" viewBox="-46.0282 2.7499 5.657699999999998 8.1789" stroke-linecap="round" stroke-linejoin="round">'
            self.url_base = 'https://servicodados.ibge.gov.br/api/v3/malhas/municipios/'
        def to_svg(self,df_cities,path_name_file='default', stroke='gray',stroke_width="6", fill= 'black',viewBox=''):
            svg_head = ''
            head = ''
            min_x,min_y,width, height = 90000000,90000000,0,0
            for county in tqdm(range(len(df_cities.values))):
                test = True
                while test:
                    try:
                        #faz a busca do municipio na base do ibge, pelo código do IBGE
                        r_county = requests.get(self.url_base+df_cities["code"].iloc[county])
                        test = False
                    except Exception as e:
                        test = True
                        time.sleep(5)

                if len(r_county.text)!=0:
                    ab = r_county.text.split('<g')[0]
                    x,y  = ab.find('viewBox'),ab.find('stroke')-1
                    viewport = ab[x:y]
                    viewport_values = viewport[viewport.find('"'):].replace('"','').split(' ')
                    viewport_values = list(map(float,viewport_values))
                    min_x_aux,min_y_aux,width_aux, height_aux = viewport_values[0],viewport_values[1],width+viewport_values[2],height+viewport_values[3]
                    if min_x_aux <= min_x:
                        min_x = min_x_aux
                    if min_y_aux <= min_y:
                        min_y = min_y_aux
                    if width_aux >= width:
                        width = width_aux
                    if height_aux >= height:
                        height = height_aux
                    #print(f'viewBox="{min_x} {min_y} {width} {height} "')
                    if viewBox != '':
                        head = self.svg_head.replace('viewBox="-46.0282 2.7499 5.657699999999998 8.1789"',viewBox)
                    else:
                        head = self.svg_head.replace('viewBox="-46.0282 2.7499 5.657699999999998 8.1789"',f'viewBox="{min_x} {min_y} {width} {height}"')
                    #print(head)
                    # busca o inicio e o fim da path, com os identificadores <g> </g>
                    start,end = r_county.text.find('<g'),r_county.text.find('</g>')
                    if list(df_cities.columns).count('city')>0:
                        if df_cities["city"].iloc[county] != '':
                            #separa apenas o path da chamada
                            county_aux = r_county.text[start:end]+f'<title>{df_cities["city"].iloc[county]}</title>'+'</g>'
                        else:
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
                    #print(f'Erro na requisição, código ({county}) inválido ou API do IBGE indisponível',end=',')
                    print(f'{county})',end=',')
            svg_head += '</svg>'
            if path_name_file == 'default':
                hash = random.getrandbits(128)
                path_name_file = "%032x" % hash
            bs = BeautifulSoup(svg_head, 'html.parser')
            pretty_xml = bs.prettify()
            #print(pretty_xml)
            print(f'arquivo {path_name_file}.svg salvo com sucesso')
            f = open(path_name_file+".svg", "w", encoding="utf-8")
            f.write(head+pretty_xml+'</svg>')
            f.close()
            #return svg_head
    class MapEstates:
        def __init__(self):
            pass
        def to_svg(self,df_cities, stroke='gray',stroke_width="6", fill= 'black'):
            pass