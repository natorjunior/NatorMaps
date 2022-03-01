# NatorMaps
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Baixe o arquivo [natorMaps.py](https://github.com/natorjunior/NatorMaps/blob/main/natorMaps.py) e mantenha ele em seu diretório, em seguida faça o import do arquivo e seu modulo.

```sh
from natorMaps import NatorMaps
```

O próximo passo é preparar o DataFrame, com os parâmetros esperados, sendo `"code"`, que é o código do IBGE do município e o `"fill"`, que pode ser definido individualmente ou geral.

```sh
import pandas as pd
from natorMaps import NatorMaps
df1 = pd.read_html('http://cat.oriontec.com.br/~thotau/help/2.0/Thotau/CEARA.html')[2]
df1 = df1.rename(columns=df1.iloc[0].to_dict()).iloc[1:]
df2 = df1[['CÓDIGO IBGE','NOME DO MUNICÍPIO']]
df2 = df2.rename(columns={'CÓDIGO IBGE':'code','NOME DO MUNICÍPIO':'city'}).drop_duplicates()
df2['fill']       = '#51A3A3'
df2['city'] = df2['city'].apply(lambda x: x.encode('utf8').decode('iso-8859-1'))
mapCities = NatorMaps.MapCities()
mapCities.to_svg(df_cities=df2,path_name_file='ceara1',viewBox='viewBox="-41.4233 2.7843 4.1706 5.0733"')
```
<p align="center"> 
  <img src="https://github.com/natorjunior/NatorMaps/blob/main/exemplos/ceara1.svg" width="300" height="300" alt>
</p>
<p align="center">
     <em>Figura gerada no exemplo 1 para o mapa do Ceará</em>
</p>

Outro exemplo pode ser adotado, agora para uma visualização do mapa do piauí
```sh
import pandas as pd
from natorMaps import NatorMaps
df1 = pd.read_html('http://cat.oriontec.com.br/~thotau/help/2.0/Thotau/PIAUI.html')[2]
df1 = df1.rename(columns=df1.iloc[0].to_dict()).iloc[1:]
df2 = df1[['CÓDIGO IBGE','NOME DO MUNICÍPIO']]
df2 = df2.rename(columns={'CÓDIGO IBGE':'code','NOME DO MUNICÍPIO':'city'}).drop_duplicates()
df2['fill']       = '#51A3A3'
df2['city'] = df2['city'].apply(lambda x: x.encode('utf8').decode('iso-8859-1'))
mapCities = NatorMaps.MapCities()
mapCities.to_svg(df_cities=df2,path_name_file='piaui1',viewBox='viewBox="-46.0282 2.7499 5.657699999999998 8.1789"')
```
<p align="center"> 
  <img src="https://github.com/natorjunior/NatorMaps/blob/main/exemplos/piaui1.svg" width="300" height="300" alt>
</p>
<p align="center">
     <em>Figura gerada no exemplo 2 para o mapa do Piauí</em>
</p>

Outro exemplo pode ser adotado, agora para uma visualização do mapa do Piauí e Ceará juntos
```sh
import pandas as pd
from natorMaps import NatorMaps
dfce = pd.read_html('http://cat.oriontec.com.br/~thotau/help/2.0/Thotau/CEARA.html')[2]
dfce = dfce.rename(columns=dfce.iloc[0].to_dict()).iloc[1:]
dfce = dfce[['CÓDIGO IBGE','NOME DO MUNICÍPIO']]
dfce = dfce.rename(columns={'CÓDIGO IBGE':'code','NOME DO MUNICÍPIO':'city'}).drop_duplicates()
dfce['fill']       = '#51A3A3'
dfce['city'] = dfce['city'].apply(lambda x: x.encode('utf8').decode('iso-8859-1'))

dfpi = pd.read_html('http://cat.oriontec.com.br/~thotau/help/2.0/Thotau/PIAUI.html')[2]
dfpi = dfpi.rename(columns=dfpi.iloc[0].to_dict()).iloc[1:]
dfpi = dfpi[['CÓDIGO IBGE','NOME DO MUNICÍPIO']]
dfpi = dfpi.rename(columns={'CÓDIGO IBGE':'code','NOME DO MUNICÍPIO':'city'}).drop_duplicates()
dfpi['fill']       = '#5C2751'
dfpi['city'] = dfpi['city'].apply(lambda x: x.encode('utf8').decode('iso-8859-1'))
df_ce_pi = dfce.append(dfpi)

mapCities = NatorMaps.MapCities()
mapCities.to_svg(df_cities=df_ce_pi,path_name_file='ce-pi',viewBox='viewBox="-46.0282 2.7499 5.657699999999998 12.1789"')
```
<p align="center"> 
  <img src="https://github.com/natorjunior/NatorMaps/blob/main/exemplos/ce-pi.svg" width="500" height="500" alt>
</p>
<p align="center">
     <em>Figura gerada no exemplo 3 para o mapa do Piauí e Ceará juntos</em>
</p>

As malhas podem ser encontradas em: 
https://servicodados.ibge.gov.br/api/docs/malhas?versao=3#api-Malhas-estadosIdGet
