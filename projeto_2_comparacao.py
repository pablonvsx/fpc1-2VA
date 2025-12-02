"""
Implementação da comparação gráfica das buscas desenvolvidas nos Projetos 1 e 2
Compara três métodos: Busca Sequencial, Busca Binária e Tabela Hash
"""

from lista_encadeada import ListaEncadeada
from lista_encadeada_com_indices import ListaEncadeadaIndexada
from tabela_hash import TabelaHash
import time
import matplotlib.pyplot as plot

def carregar_ids(nome_arquivo):
    """
    Carrega IDs de produtos de um arquivo de texto
    """
    ids = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            ids.append(int(linha.strip()))
    return ids

def main():
    print("Projeto 2 - Comparação de Performance: Três Métodos de Busca")
    print("_"*60)

    # Carregamento dos dados
    print("\n> Carregando dados...")
    ids_produtos = carregar_ids('projeto_2_lista_IDs_entrada.txt')
    ids_busca = carregar_ids('projeto_2_lista_IDs_busca.txt')
    print(f"   IDs de produtos carregados: {len(ids_produtos)}")
    print(f"   IDs para busca carregados: {len(ids_busca)}")

    print("\n> Criando estruturas de dados...")

    # Criando lista encadeada simples
    lista_encadeada_simples = ListaEncadeada()
    for id_produto in ids_produtos:
        lista_encadeada_simples.inserir_ordenado(id_produto)
    print(f"   Lista Encadeada Simples: {lista_encadeada_simples.tamanho} elementos")

    # Criando lista encadeada com índices (modo otimizado para grandes volumes)
    lista_encadeada_indices = ListaEncadeadaIndexada(auto_indexar=False)
    for id_produto in ids_produtos:
        lista_encadeada_indices.inserir_ordenado(id_produto)
    
    # Construir índices após todas as inserções (muito mais rápido!)
    print("   Construindo vetor de índices...")
    lista_encadeada_indices.construir_indices()
    print(f"   Lista Encadeada com Índices: {lista_encadeada_indices.tamanho} elementos")

    # Criando tabela hash
    tabela_hash = TabelaHash()
    for id_produto in ids_produtos:
        tabela_hash.inserir(id_produto)
    
    # Calcular elementos na tabela hash
    total_elementos_hash = 0
    posicoes_ocupadas = 0
    for posicao in tabela_hash.tabela:
        if posicao is not None:
            posicoes_ocupadas += 1
            atual = posicao
            while atual is not None:
                total_elementos_hash += 1
                atual = atual.proximo
    print(f"   Tabela Hash: {total_elementos_hash} elementos (tamanho: {tabela_hash.tamanho}, posições ocupadas: {posicoes_ocupadas})")

    # Medindo tempo de busca na lista encadeada simples
    print("\n> Medindo tempo de busca na Lista Encadeada Simples...")
    total_tempo_busca_sequencial = 0

    for id_busca in ids_busca:
        inicio = time.perf_counter()
        lista_encadeada_simples.buscar(id_busca)
        fim = time.perf_counter()
        tempo_busca = fim - inicio
        total_tempo_busca_sequencial += tempo_busca

    print(f"   Tempo total: {total_tempo_busca_sequencial:.10f} s")
    print(f"   Tempo médio: {total_tempo_busca_sequencial/len(ids_busca):.10f} s")

    # Medindo tempo de busca binária na lista encadeada com índices
    print("\n> Medindo tempo de busca na Lista Encadeada com Índices...")
    total_tempo_busca_binaria = 0

    for id_busca in ids_busca:
        inicio = time.perf_counter()
        lista_encadeada_indices.busca_binaria(id_busca)
        fim = time.perf_counter()
        tempo_busca = fim - inicio
        total_tempo_busca_binaria += tempo_busca
    
    print(f"   Tempo total: {total_tempo_busca_binaria:.10f} s")
    print(f"   Tempo médio: {total_tempo_busca_binaria/len(ids_busca):.10f} s")

    # Medindo tempo de busca na tabela hash
    print("\n> Medindo tempo de busca na Tabela Hash...")
    total_tempo_busca_hash = 0

    for id_busca in ids_busca:
        inicio = time.perf_counter()
        tabela_hash.buscar(id_busca)
        fim = time.perf_counter()
        tempo_busca = fim - inicio
        total_tempo_busca_hash += tempo_busca
    
    print(f"   Tempo total: {total_tempo_busca_hash:.10f} s")
    print(f"   Tempo médio: {total_tempo_busca_hash/len(ids_busca):.10f} s")

    # Calculando as diferenças
    print("\n" + "_" * 60 + "\n")
    print("COMPARAÇÃO DE DESEMPENHO" + "\n")
    print(f"Lista Encadeada Simples (Busca Sequencial): {total_tempo_busca_sequencial:.10f} s")
    print(f"Lista com Índices (Busca Binária): {total_tempo_busca_binaria:.10f} s")
    print(f"Tabela Hash: {total_tempo_busca_hash:.10f} s")
    
    # Encontrar o método mais rápido
    tempos = {
        'Busca Sequencial': total_tempo_busca_sequencial,
        'Busca Binária': total_tempo_busca_binaria,
        'Tabela Hash': total_tempo_busca_hash
    }
    metodo_mais_rapido = min(tempos, key=tempos.get)
    tempo_mais_rapido = tempos[metodo_mais_rapido]
    
    print(f"\nMétodo mais rápido: {metodo_mais_rapido}")
    print("\nComparações:")
    for metodo, tempo in tempos.items():
        if metodo != metodo_mais_rapido:
            fator = tempo / tempo_mais_rapido
            print(f"  {metodo_mais_rapido} foi {fator:.2f}x mais rápido que {metodo}")
    print()
    
    # Gerando gráfico de desempenho
    print("> Gerando gráfico de desempenho...")
    
    categorias = [
        'Lista Encadeada\n(Busca Sequencial)', 
        'Lista com Índices\n(Busca Binária)',
        'Tabela Hash'
    ]
    tempos_totais = [
        total_tempo_busca_sequencial * 1000,
        total_tempo_busca_binaria * 1000,
        total_tempo_busca_hash * 1000
    ]  # Converter para ms para melhor visualização
    
    plot.figure(figsize=(12, 6))
    barras = plot.bar(categorias, tempos_totais, color=['#FF6B6B', '#4ECDC4', '#95E1D3'], width=0.6)
    
    # Adicionar valores nas barras
    for barra in barras:
        altura = barra.get_height()
        plot.text(barra.get_x() + barra.get_width()/2., altura,
                 f'{altura:.6f} ms',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plot.xlabel('Método de Busca', fontsize=12, fontweight='bold')
    plot.ylabel('Tempo Total de Busca (ms)', fontsize=12, fontweight='bold')
    plot.title('Comparação de Desempenho: Busca Sequencial vs Busca Binária vs Tabela Hash', 
              fontsize=14, fontweight='bold', pad=20)
    plot.grid(axis='y', alpha=0.3, linestyle='--')
    plot.tight_layout()
    
    nome_arquivo_grafico = 'projeto_2_comparacao_desempenho.png'
    plot.savefig(nome_arquivo_grafico, dpi=300, bbox_inches='tight')
    plot.close()
    
    print(f"   Gráfico gerado: {nome_arquivo_grafico}")
    
    print("\n" + "_" * 60)
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")

if __name__ == "__main__":
    main()
