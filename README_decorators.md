# Decoradores NatorMaps

Este módulo fornece decoradores para facilitar a geração de mapas SVG usando a biblioteca NatorMaps.

## Decoradores Disponíveis

### `@nator_maps_svg`

Decorador completo para gerar mapas SVG com configuração detalhada de legenda.

**Parâmetros:**
- `db_path` (str): Caminho para o banco de dados
- `estado` (str): Código do estado (ex: "CE", "PI")
- `str1` (str): Título da legenda
- `str2` (str): Subtítulo da legenda  
- `faixa` (dict): Dicionário com as faixas de valores para legenda
- `legenda` (bool): Se deve incluir a legenda no SVG

**A função decorada deve retornar:** Um dicionário onde as chaves são códigos IBGE dos municípios e os valores são cores em formato hexadecimal.

### `@simple_nator_svg`

Decorador simples para geração rápida de mapas SVG.

**Parâmetros:**
- `db_path` (str): Caminho para o banco de dados
- `estado` (str): Código do estado
- `legenda` (bool): Se deve incluir a legenda
- `**nator_kwargs`: Argumentos adicionais (str1, str2, faixa)

## Exemplos de Uso

### Exemplo Básico

```python
from lib.decorators import simple_nator_svg

@simple_nator_svg("natorMaps.db", "CE")
def cores_municipios():
    return {
        230440: "#FF0000",  # Fortaleza - vermelho
        230750: "#00FF00",  # Juazeiro do Norte - verde
        230730: "#0000FF",  # Sobral - azul
    }

# Uso
svg = cores_municipios()
```

### Exemplo com Legenda Personalizada

```python
@nator_maps_svg(
    db_path="natorMaps.db",
    estado="CE",
    str1="População Municipal", 
    str2="Dados do Censo 2024",
    faixa={
        1: "Até 50.000 hab",
        2: "50.001 - 200.000 hab", 
        3: "200.001 - 500.000 hab",
        4: "Mais de 500.000 hab"
    }
)
def cores_por_populacao():
    # Sua lógica para calcular cores baseadas na população
    populacao = consultar_populacao_municipios()
    
    cores = {}
    for codigo_ibge, pop in populacao.items():
        if pop <= 50000:
            cores[codigo_ibge] = "#F1F0F0"
        elif pop <= 200000:
            cores[codigo_ibge] = "#FFE8D6"
        elif pop <= 500000:
            cores[codigo_ibge] = "#FFA366"
        else:
            cores[codigo_ibge] = "#E85011"
    
    return cores
```

### Exemplo sem Legenda

```python
@simple_nator_svg("natorMaps.db", "PI", legenda=False)
def mapa_simples():
    return {
        221100: "#E85011",  # Teresina
        220570: "#FFA366",  # Parnaíba
    }
```

## Cores Sugeridas

Para manter consistência visual, use estas cores padrão:

- `#F1F0F0` - Cinza claro (valores baixos)
- `#FFE8D6` - Laranja muito claro
- `#FFA366` - Laranja médio  
- `#E85011` - Vermelho alaranjado (valores altos)

## Códigos IBGE

Para usar os decoradores, você precisa dos códigos IBGE dos municípios. Alguns exemplos:

**Ceará:**
- 230440 - Fortaleza
- 230750 - Juazeiro do Norte
- 230730 - Sobral
- 230420 - Caucaia

**Piauí:**
- 221100 - Teresina
- 220570 - Parnaíba
- 220300 - Floriano
- 220200 - Campo Maior

## Dicas de Uso

1. **Performance**: Para mapas com muitos municípios coloridos, considere otimizar as consultas ao banco de dados.

2. **Cores**: Use cores com bom contraste para facilitar a visualização.

3. **Legenda**: Customize as faixas da legenda de acordo com seus dados específicos.

4. **Salvando**: Para salvar o SVG gerado:
   ```python
   svg = minha_funcao_decorada()
   with open("meu_mapa.svg", "w", encoding="utf-8") as f:
       f.write(svg)
   ```

5. **Debugging**: Os decoradores imprimem informações de debug sobre a geração do mapa.
