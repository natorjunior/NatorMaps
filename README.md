# NatorMaps
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Baixe o arquivo [natorMaps.py](https://github.com/natorjunior/NatorMaps/blob/main/natorMaps.py) e mantenha ele em seu diretório, em seguida faça o import do arquivo e seu modulo.

```sh
from natorMaps import NatorMaps
```

O próximo passo é preparar o DataFrame, com os parâmetros esperados, sendo `"code"`, que é o código do IBGE do município e o `"fill"`, que pode ser definido individualmente ou geral.

```sh
from natorMaps import NatorMaps
import pandas as pd
counties = pd.DataFrame([
    {'code':'3303500','fill':'green'},
    {'code':'3304557','fill':'blue'},
    {'code':'3301702','fill':'gray'}
])
mapCities = NatorMaps.MapCities()
mapCities.to_svg(df_cities=counties,path_name_file='exemplo1')
```
<p align="center"> 
  <img src="https://github.com/natorjunior/NatorMaps/blob/main/imagens/exemplo1.svg" width="300" height="300" alt>
</p>
<p align="center">
     <em>Figura gerada no exemplo 1</em>
</p>

No exemplo, é possível visualizar que o `fill` foi definido de forma individual, ou seja cada municipio tem uma cor diferente, caso a coluna não exista, o `fill` é definido como `black` ou pode se incluido na função `to_svg(df_cities=counties,path_name_file='exemplo2',fill="#F8F8F8")`, como demostrado abaixo.


```sh
from natorMaps import NatorMaps
import pandas as pd
counties = pd.DataFrame([
    {'code':'3303500'},
    {'code':'3304557'},
    {'code':'3301702'}
])
mapCities = NatorMaps.MapCities()
mapCities.to_svg(df_cities=counties,path_name_file='exemplo2',fill='#F6F6F6')
```
<p align="center"> 
  <img src="https://github.com/natorjunior/NatorMaps/blob/main/imagens/exemplo2.svg" width="300" height="300" alt>
</p>
<p align="center">
     <em>Figura gerada no exemplo 2</em>
</p>

```sh
from natorMaps import NatorMaps
import pandas as pd
counties = pd.DataFrame([
    {'code':'3303500'},
    {'code':'3304557'},
    {'code':'3301702'}
])
mapCities = NatorMaps.MapCities()
mapCities.to_svg(df_cities=counties,path_name_file='exemplo3')
```

<p align="center"> 
  <img src="https://github.com/natorjunior/NatorMaps/blob/main/imagens/exemplo3.svg" width="300" height="300" alt>
</p>
<p align="center">
     <em>Figura gerada no exemplo 3</em>
</p>
