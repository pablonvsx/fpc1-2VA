"""
Projeto 3 - Comparação Completa de Algoritmos de Ordenação
Implementação, execução, geração de arquivos de resultados e gráficos comparativos
dos algoritmos de Inserção e Intercalação (Merge Sort)
"""

import sys
import os
# Adicionar o diretório pai ao path (não é necessário para este projeto, mas mantém consistência)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import matplotlib.pyplot as plot

# Carregamento de Dados
def carregar_produtos(nome_arquivo):
    """
    Carrega produtos de um arquivo de texto para uma lista de dicionários.
    Cada linha do arquivo deve conter um ID de produto
    Formato: id | nome | preço | estoque | popularidade | data_cadastro

    """
    produtos = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split('|')
                if len(partes) == 6:
                    # Criando o dicionário e convertendo os tipos necessários
                    produto = {
                        "id": partes[0].strip(),
                        "nome": partes[1].strip(),
                        "preco": float(partes[2].strip()),      # Importante converter para float
                        "estoque": int(partes[3].strip()),      # Importante converter para int
                        "popularidade": int(partes[4].strip()), # Importante converter para int
                        "data_cadastro": partes[5].strip()      # Data formato YYYY-MM-DD (ordena como string)
                    }
                    produtos.append(produto)
    except FileNotFoundError:
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
    return produtos

def carregar_requisicoes(nome_arquivo):
    """
    Carrega a lista de critérios de ordenação a serem testados.
    """
    requisicoes = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                criterio = linha.strip()
                if criterio:
                    requisicoes.append(criterio)
    except FileNotFoundError:
        print(f"Aviso: Arquivo {nome_arquivo} não encontrado. Usando lista padrão.")
        return ["preco", "estoque", "popularidade", "data_cadastro", "nome"]
    return requisicoes

def salvar_resultado(nome_arquivo, lista_produtos):
    """
    Salva a lista ordenada no arquivo de saída no formato com colunas alinhadas.
    Formato: ID com 10 chars | Nome com 40 chars | Preço com 10 chars | Estoque com 5 chars | Popularidade com 5 chars | Data
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for p in lista_produtos:
            # Formata cada campo com largura fixa e preenchimento adequado
            id_formatado = p['id'].ljust(10)  # ID alinhado à esquerda, 10 caracteres
            nome_formatado = p['nome'].ljust(40)  # Nome alinhado à esquerda, 40 caracteres
            preco_formatado = f"{p['preco']:010.2f}"  # Preço com zeros à esquerda, 10 caracteres total
            estoque_formatado = f"{p['estoque']:05d}"  # Estoque com zeros à esquerda, 5 dígitos
            popularidade_formatada = f"{p['popularidade']:05d}"  # Popularidade com zeros à esquerda, 5 dígitos
            data_formatada = p['data_cadastro']  # Data já está no formato correto
            
            # Monta a linha com o formato esperado
            linha = f"{id_formatado} | {nome_formatado} | {preco_formatado} | {estoque_formatado} | {popularidade_formatada} | {data_formatada}\n"
            arquivo.write(linha)

# Algoritmos de Ordenação

def insertion_sort(lista, criterio):
    # Cria uma cópia da lista para não modificar a original
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)

    for i in range(1, n):
        elemento_atual = lista_ordenada[i]
        j = i - 1
        
        # Compara o valor do critério (ex: elemento_atual['preco'] < lista[j]['preco'])
        while j >= 0 and elemento_atual[criterio] < lista_ordenada[j][criterio]:
            lista_ordenada[j + 1] = lista_ordenada[j]
            j -= 1
        lista_ordenada[j + 1] = elemento_atual

    return lista_ordenada

def merge_sort(lista, criterio):
    # Caso base da recursão
    if len(lista) <= 1:
        return lista
    
    # Divisão
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], criterio)
    direita = merge_sort(lista[meio:], criterio)
    
    # Intercalação (Conquista)
    return merge(esquerda, direita, criterio)

def merge(esquerda, direita, criterio):
    lista_ordenada = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        # Comparação baseada no critério dinâmico
        if esquerda[i][criterio] <= direita[j][criterio]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1
            
    # Adicionar os elementos restantes
    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])
    
    return lista_ordenada

def ordenar_produtos(lista_produtos, criterio, algoritmo):
    """
    Função wrapper que escolhe o algoritmo e retorna a lista ordenada.
    algoritmo: "insercao" ou "intercalacao"
    """
    if algoritmo == "insercao":
        return insertion_sort(lista_produtos, criterio)
    elif algoritmo == "intercalacao":
        return merge_sort(lista_produtos, criterio)
    else:
        print("Algoritmo desconhecido.")
        return []

def main():
    print("Projeto 3 - Comparação de Algoritmos de Ordenação")
    print("_"*60)

    # Carregamento dos dados
    print("\n> Carregando dados...")
    produtos_entrada = 'projeto_3/projeto_3_lista_produtos_entrada.txt'
    produtos_requisicoes = 'projeto_3/projeto_3_requisicoes_listagem.txt'
    produtos = carregar_produtos(produtos_entrada)
    print(f"   Produtos carregados: {len(produtos)}")

    print("\n> Carregando requisições...")
    requisicoes = carregar_requisicoes(produtos_requisicoes)
    print(f"   Total de requisições: {len(requisicoes)}")
    print(f"   Critérios: {', '.join(requisicoes)}")

    # Dicionário para armazenar os tempos de cada algoritmo
    resultados = {}
    
    # Lista de algoritmos a testar
    algoritmos_teste = ["insercao", "intercalacao"]
    
    for algoritmo in algoritmos_teste:
        print(f"\n> Executando ordenações com algoritmo: {algoritmo.upper()}")
        
        resultados[algoritmo] = {}
        tempo_total_algoritmo = 0
        
        # Executa todas as requisições para este algoritmo
        for req in requisicoes:
            tempo_inicio = time.perf_counter()
            
            # Ordena
            resultado = ordenar_produtos(produtos, req, algoritmo)
            
            tempo_fim = time.perf_counter()
            tempo_criterio = tempo_fim - tempo_inicio
            
            # Armazena o tempo para este critério
            resultados[algoritmo][req] = tempo_criterio
            tempo_total_algoritmo += tempo_criterio
            
            # Gera nome do arquivo: projeto_3_resultado_insercao_preco.txt
            nome_saida = f"projeto_3/projeto_3_resultado_{algoritmo}_{req}.txt"
            
            # Salva
            salvar_resultado(nome_saida, resultado)
        
        print(f"   Ordenações concluídas!")
        print(f"   Tempo total: {tempo_total_algoritmo:.6f} s")
        print(f"   Tempo médio por critério: {tempo_total_algoritmo/len(requisicoes):.6f} s")

    # Comparação final
    print("\n" + "_" * 60 + "\n")
    print("COMPARAÇÃO DE DESEMPENHO")
    print("_" * 60)
    
    # Comparação por critério
    print("\nTempo por Critério:")
    print(f"  {'Critério':<20} {'Inserção (s)':<15} {'Intercalação (s)':<18} {'Mais Rápido'}")
    print("  " + "-" * 70)
    
    for req in requisicoes:
        tempo_insercao = resultados['insercao'][req]
        tempo_intercalacao = resultados['intercalacao'][req]
        mais_rapido = "Inserção" if tempo_insercao < tempo_intercalacao else "Intercalação"
        
        print(f"  {req:<20} {tempo_insercao:<15.6f} {tempo_intercalacao:<18.6f} {mais_rapido}")
    
    # Comparação geral
    tempo_total_insercao = sum(resultados['insercao'].values())
    tempo_total_intercalacao = sum(resultados['intercalacao'].values())
    tempo_medio_insercao = tempo_total_insercao / len(requisicoes)
    tempo_medio_intercalacao = tempo_total_intercalacao / len(requisicoes)
    
    print("\n" + "_" * 60 +"\n")
    print("RESUMO GERAL")
    print("_" * 60)
    print(f"Algoritmo de Inserção:")
    print(f"  Tempo total: {tempo_total_insercao:.6f} s")
    print(f"  Tempo médio: {tempo_medio_insercao:.6f} s")
    print(f"\nAlgoritmo de Intercalação:")
    print(f"  Tempo total: {tempo_total_intercalacao:.6f} s")
    print(f"  Tempo médio: {tempo_medio_intercalacao:.6f} s" + "\n")
    
    # Determinar o vencedor geral
    print("\n" + "_" * 60 + "\n")
    if tempo_total_insercao < tempo_total_intercalacao:
        diferenca = tempo_total_intercalacao - tempo_total_insercao
        fator = tempo_total_intercalacao / tempo_total_insercao
        print("Algoritmo mais rápido: INSERÇÃO")
        print(f"  Diferença: {diferenca:.6f} s")
        print(f"  Fator: {fator:.2f}x mais rápido")
    else:
        diferenca = tempo_total_insercao - tempo_total_intercalacao
        fator = tempo_total_insercao / tempo_total_intercalacao
        print("Algoritmo mais rápido: INTERCALAÇÃO")
        print(f"  Diferença: {diferenca:.6f} s")
        print(f"  Fator: {fator:.2f}x mais rápido")
    print("_" * 60)

    print("\n> Arquivos de resultado gerados: projeto_3_resultado_[algoritmo]_[criterio].txt")
    
    # Gerar gráficos
    print("\n> Gerando gráficos...")
    
    # Gráfico 1: Comparação por critério
    criterios_labels = [req.replace('_', ' ').title() for req in requisicoes]
    tempos_insercao = [resultados['insercao'][req] * 1000 for req in requisicoes]  # Converter para ms
    tempos_intercalacao = [resultados['intercalacao'][req] * 1000 for req in requisicoes]
    
    import numpy as np
    x = np.arange(len(criterios_labels))
    largura = 0.35
    
    plot.figure(figsize=(14, 6))
    barras1 = plot.bar(x - largura/2, tempos_insercao, largura, label='Inserção', color='#FF6B6B')
    barras2 = plot.bar(x + largura/2, tempos_intercalacao, largura, label='Intercalação', color='#4ECDC4')
    
    # Adicionar valores nas barras de Inserção com fator de comparação
    for i, barra in enumerate(barras1):
        altura = barra.get_height()
        fator = tempos_insercao[i] / tempos_intercalacao[i]
        plot.text(barra.get_x() + barra.get_width()/2., altura,
                 f'{altura:.2f}\n({fator:.1f}x t(inter))',
                 ha='center', va='bottom', fontsize=7, fontweight='bold')
    
    # Adicionar valores nas barras de Intercalação
    for barra in barras2:
        altura = barra.get_height()
        plot.text(barra.get_x() + barra.get_width()/2., altura,
                 f'{altura:.2f}',
                 ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    plot.xlabel('Critério de Ordenação', fontsize=12, fontweight='bold')
    plot.ylabel('Tempo de Execução (ms)', fontsize=12, fontweight='bold')
    plot.title('Comparação de Desempenho por Critério de Ordenação', 
              fontsize=14, fontweight='bold', pad=20)
    plot.xticks(x, criterios_labels, rotation=15, ha='right')
    plot.legend(fontsize=10)
    plot.grid(axis='y', alpha=0.3, linestyle='--')
    plot.tight_layout()
    
    nome_grafico1 = 'projeto_3/projeto_3_comparacao_por_criterio.png'
    plot.savefig(nome_grafico1, dpi=300, bbox_inches='tight')
    plot.close()
    print(f"   Gráfico gerado: {nome_grafico1}")
    
    # Gráfico 2: Comparação geral (tempo total)
    plot.figure(figsize=(10, 7))
    categorias = ['Inserção', 'Intercalação']
    tempos_totais = [tempo_total_insercao * 1000, tempo_total_intercalacao * 1000]  # Converter para ms
    
    barras = plot.bar(categorias, tempos_totais, color=['#FF6B6B', '#4ECDC4'], width=0.6)
    
    # Adicionar valores nas barras com fator de comparação
    fator_geral = (tempo_total_insercao * 1000) / (tempo_total_intercalacao * 1000)
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        if i == 0:  # Inserção
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.2f} ms\n({fator_geral:.1f}x t(inter))',
                     ha='center', va='bottom', fontsize=10, fontweight='bold')
        else:  # Intercalação
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.2f} ms',
                     ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Ajustar limites do eixo Y para dar mais espaço acima das barras
    y_max = max(tempos_totais) * 1.15
    plot.ylim(0, y_max)
    
    plot.xlabel('Algoritmo de Ordenação', fontsize=12, fontweight='bold')
    plot.ylabel('Tempo Total de Execução (ms)', fontsize=12, fontweight='bold')
    plot.title('Comparação Geral de Desempenho: Inserção vs Intercalação', 
              fontsize=14, fontweight='bold', pad=20)
    plot.grid(axis='y', alpha=0.3, linestyle='--')
    plot.tight_layout()
    
    nome_grafico2 = 'projeto_3/projeto_3_comparacao_geral.png'
    plot.savefig(nome_grafico2, dpi=300, bbox_inches='tight')
    plot.close()
    print(f"   Gráfico gerado: {nome_grafico2}")
    
    # Gráfico 3: Tempo médio por critério
    plot.figure(figsize=(10, 7))
    tempo_medio_insercao_ms = tempo_medio_insercao * 1000
    tempo_medio_intercalacao_ms = tempo_medio_intercalacao * 1000
    
    barras = plot.bar(categorias, [tempo_medio_insercao_ms, tempo_medio_intercalacao_ms], 
                     color=['#FF6B6B', '#4ECDC4'], width=0.6)
    
    # Adicionar valores nas barras com fator de comparação
    fator_medio = tempo_medio_insercao_ms / tempo_medio_intercalacao_ms
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        if i == 0:  # Inserção
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.2f} ms\n({fator_medio:.1f}x t(inter))',
                     ha='center', va='bottom', fontsize=10, fontweight='bold')
        else:  # Intercalação
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.2f} ms',
                     ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Ajustar limites do eixo Y para dar mais espaço acima das barras
    y_max = max(tempo_medio_insercao_ms, tempo_medio_intercalacao_ms) * 1.15
    plot.ylim(0, y_max)
    
    plot.xlabel('Algoritmo de Ordenação', fontsize=12, fontweight='bold')
    plot.ylabel('Tempo Médio por Critério (ms)', fontsize=12, fontweight='bold')
    plot.title('Tempo Médio de Execução por Critério de Ordenação', 
              fontsize=14, fontweight='bold', pad=20)
    plot.grid(axis='y', alpha=0.3, linestyle='--')
    plot.tight_layout()
    
    nome_grafico3 = 'projeto_3/projeto_3_comparacao_media.png'
    plot.savefig(nome_grafico3, dpi=300, bbox_inches='tight')
    plot.close()
    print(f"   Gráfico gerado: {nome_grafico3}")
    
    print("\n" + "_"*60)
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")


if __name__ == "__main__":
    main()
