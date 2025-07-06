#!/usr/bin/env python3
"""
Exemplo de uso dos decoradores NatorMaps ajustados
As funções decoradas devem retornar dicionários de cores
onde as chaves são códigos IBGE e os valores são cores hexadecimais
"""

from lib.decorators import nator_maps_svg, simple_nator_svg

# Configuração do banco de dados
DB_PATH = "natorMaps.db"

# Exemplo 1: Usando o decorador completo
@nator_maps_svg(
    db_path=DB_PATH,
    estado="CE",
    str1="População por Município",
    str2="Dados do Censo 2024",
    faixa={
        1: "Até 50.000 hab",
        2: "50.001 - 200.000 hab",
        3: "200.001 - 500.000 hab", 
        4: "Mais de 500.000 hab"
    },
    legenda=True
)
def cores_populacao_ceara():
    """Retorna cores baseadas na população dos municípios do Ceará"""
    print("Calculando cores baseadas na população...")
    
    # Exemplo de cores por código IBGE
    # Na prática, você faria consultas ao banco de dados aqui
    cores_municipios = {
        230440: "#E85011",  # Fortaleza (mais de 500k) - vermelho escuro
        230750: "#FFA366",  # Juazeiro do Norte (200k-500k) - laranja
        230730: "#FFE8D6",  # Sobral (50k-200k) - laranja claro
        230420: "#F1F0F0",  # Caucaia (até 50k) - cinza claro
        # Adicione mais municípios conforme necessário
    }
    
    return cores_municipios

# Exemplo 2: Usando o decorador simples
@simple_nator_svg(
    DB_PATH, 
    "PI",
    str1="Índice de Desenvolvimento",
    str2="Piauí 2024",
    faixa={
        1: "Muito Baixo (0-0.5)",
        2: "Baixo (0.5-0.65)", 
        3: "Médio (0.65-0.8)",
        4: "Alto (0.8-1.0)"
    },
    legenda=True
)
def cores_desenvolvimento_piaui():
    """Retorna cores baseadas no índice de desenvolvimento do Piauí"""
    print("Calculando índices de desenvolvimento...")
    
    # Simulação de dados de desenvolvimento
    cores_municipios = {
        221100: "#E85011",  # Teresina - Alto desenvolvimento
        220570: "#FFA366",  # Parnaíba - Médio desenvolvimento
        220300: "#FFE8D6",  # Floriano - Baixo desenvolvimento
        220200: "#F1F0F0",  # Campo Maior - Muito baixo desenvolvimento
    }
    
    return cores_municipios

# Exemplo 3: Decorador com configurações mínimas (sem legenda)
@simple_nator_svg(DB_PATH, "CE", legenda=False)
def cores_basicas_ceara():
    """Gera mapa básico do Ceará sem legenda"""
    print("Gerando cores básicas...")
    
    # Apenas algumas cores simples
    return {
        230440: "#FF0000",  # Fortaleza - vermelho
        230750: "#00FF00",  # Juazeiro - verde
        230730: "#0000FF",  # Sobral - azul
    }

# Exemplo 4: Função que processa dados e retorna cores
@nator_maps_svg(
    db_path=DB_PATH,
    estado="CE", 
    str1="Densidade Populacional",
    str2="hab/km²",
    faixa={
        1: "< 50 hab/km²",
        2: "50-200 hab/km²",
        3: "200-1000 hab/km²",
        4: "> 1000 hab/km²"
    }
)
def calcular_densidade_populacional():
    """Calcula densidade populacional e retorna cores correspondentes"""
    print("Calculando densidade populacional...")
    
    # Simulação de cálculo de densidade
    # Na prática, você faria consultas ao banco e cálculos aqui
    densidades = {
        230440: 7800,  # Fortaleza - alta densidade
        230750: 350,   # Juazeiro - média densidade
        230730: 180,   # Sobral - baixa-média densidade
        230420: 45,    # Caucaia - baixa densidade
    }
    
    # Converte densidade em cores
    cores = {}
    for codigo_ibge, densidade in densidades.items():
        if densidade < 50:
            cores[codigo_ibge] = "#F1F0F0"  # Cinza claro
        elif densidade < 200:
            cores[codigo_ibge] = "#FFE8D6"  # Laranja claro
        elif densidade < 1000:
            cores[codigo_ibge] = "#FFA366"  # Laranja
        else:
            cores[codigo_ibge] = "#E85011"  # Vermelho escuro
    
    return cores

if __name__ == "__main__":
    print("=== Exemplo 1: População Ceará ===")
    svg1 = cores_populacao_ceara()
    print(f"SVG gerado: {len(svg1) > 0}")
    
    print("\n=== Exemplo 2: Desenvolvimento Piauí ===")
    svg2 = cores_desenvolvimento_piaui()
    print(f"SVG gerado: {len(svg2) > 0}")
    
    print("\n=== Exemplo 3: Cores Básicas (sem legenda) ===")
    svg3 = cores_basicas_ceara()
    print(f"SVG gerado: {len(svg3) > 0}")
    
    print("\n=== Exemplo 4: Densidade Populacional ===")
    svg4 = calcular_densidade_populacional()
    print(f"SVG gerado: {len(svg4) > 0}")
    
    # Salvando um exemplo em arquivo
    with open("exemplo_mapa.svg", "w", encoding="utf-8") as f:
        f.write(svg1)
    print("\nMapa salvo como 'exemplo_mapa.svg'")
