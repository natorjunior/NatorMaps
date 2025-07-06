# nator_maps/decorators.py
import functools
from .NatorMaps import NatorMaps

def map_output(func):
    """
    
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[NatorMaps] Generating map with {func.__name__}...")
        if not isinstance(result, str):
            raise TypeError(
                f"{func.__name__} should return a str, got {type(result).__name__}"
            )
        print(f"[NatorMaps] Map generated: {result}")
        return result
    return wrapper

def nator_maps_svg(db_path="natorMaps.db", estado="CE", str1="Legenda de cima", str2="de baixo", faixa=None, legenda=False):
    """
    Decorador para gerar mapas SVG usando NatorMaps.
    A função decorada deve retornar um dicionário de cores onde:
    - chaves são códigos IBGE dos municípios
    - valores são cores em formato hexadecimal (ex: "#FF0000")
    
    Args:
        db_path (str): Caminho para o banco de dados
        estado (str): Código do estado para gerar o mapa
        str1 (str): Legenda superior
        str2 (str): Legenda inferior
        faixa (dict): Dicionário com as faixas de valores para a legenda
        legenda (bool): Se deve incluir a legenda no SVG
    
    Returns:
        str: SVG gerado pelo NatorMaps
        
    Exemplo de uso:
        @nator_maps_svg("natorMaps.db", "CE", 
                       str1="População Municipal", 
                       str2="Dados 2024",
                       faixa={1: "Baixa", 2: "Média", 3: "Alta", 4: "Muito Alta"})
        def cores_populacao():
            return {
                230440: "#FFE8D6",  # Fortaleza
                230750: "#FFA366",  # Juazeiro do Norte
                # ... mais municípios
            }
    """
    if faixa is None:
        faixa = {
            1: "Inexistente.",
            2: "0 < x ≤ 1,4",
            3: "1,4 < x ≤ 2,8",
            4: "x > 2,8"
        }
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Executa a função original para obter as cores
            cores = func(*args, **kwargs)
            
            print(f"[NatorMaps] Generating map with {func.__name__}...")
            
            # Verifica se a função retornou um dicionário de cores
            if not isinstance(cores, dict):
                raise TypeError(
                    f"{func.__name__} should return a dict with IBGE codes as keys and colors as values, "
                    f"got {type(cores).__name__}"
                )
            
            # Inicializa o NatorMaps com as configurações de legenda
            nator_maps = NatorMaps(
                db_path, 
                str1=str1, 
                str2=str2, 
                faixa=faixa
            )
            
            # Gera o SVG passando as cores retornadas pela função
            svg = nator_maps.get_svg(estado, cores=cores, legenda=legenda)
            
            print(f"[NatorMaps] Map generated for state: {estado} with {len(cores)} colored municipalities")
            
            return svg
                
        return wrapper
    return decorator

def simple_nator_svg(db_path, estado="CE", legenda=True, **nator_kwargs):
    """
    Decorador simples para gerar SVG com NatorMaps.
    A função decorada deve retornar um dicionário de cores.
    
    Args:
        db_path (str): Caminho para o banco de dados
        estado (str): Código do estado
        legenda (bool): Se deve incluir a legenda no SVG
        **nator_kwargs: Argumentos adicionais para NatorMaps (str1, str2, faixa)
    
    Exemplo de uso:
        @simple_nator_svg("natorMaps.db", "CE", 
                         str1="Título do Mapa", 
                         str2="Subtítulo",
                         faixa={1: "Baixo", 2: "Alto"})
        def minha_funcao():
            return {230440: "#FF0000", 230750: "#00FF00"}  # cores por código IBGE
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Executa a função original para obter as cores
            cores = func(*args, **kwargs)
            
            print(f"[NatorMaps] Processing {func.__name__} and generating SVG...")
            
            # Verifica se a função retornou um dicionário de cores
            if not isinstance(cores, dict):
                raise TypeError(
                    f"{func.__name__} should return a dict with IBGE codes as keys and colors as values, "
                    f"got {type(cores).__name__}"
                )
            
            # Configurações padrão
            default_config = {
                'str1': "Legenda de cima",
                'str2': "de baixo",
                'faixa': {
                    1: "Inexistente.",
                    2: "0 < x ≤ 1,4",
                    3: "1,4 < x ≤ 2,8",
                    4: "x > 2,8"
                }
            }
            
            # Mescla configurações padrão com as fornecidas
            config = {**default_config, **nator_kwargs}
            
            # Inicializa o NatorMaps
            nator_maps = NatorMaps(db_path, **config)
            
            # Gera o SVG com as cores fornecidas
            svg = nator_maps.get_svg(estado, cores=cores, legenda=legenda)
            
            print(f"[NatorMaps] SVG generated successfully for {estado} with {len(cores)} colored municipalities")
            
            return svg
            
        return wrapper
    return decorator