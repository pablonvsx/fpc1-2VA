"""
Implementação da comparação entre busca sequencial em lista encadeada e 
busca binária em lista encadeada com índices gerando gráfico de desempenho
"""

from lista_encadeada import ListaEncadeada
from lista_encadeada_com_indices import ListaEncadeadaIndexada
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
    print("Projeto 1 - Comparação de Performance")
    print("_"*60)

    # Carregamento dos dados
    print("\n> Carregando dados...")
    ids_produtos = carregar_ids('projeto_1_lista_IDs_entrada.txt')
    ids_busca = carregar_ids('projeto_1_lista_IDs_busca.txt')
    print(f"   IDs de produtos carregados: {len(ids_produtos)}")
    print(f"   IDs para busca carregados: {len(ids_busca)}")

    print("\n> Criando listas...")

    # Criando lista encadeada simples
    lista_encadeada_simples = ListaEncadeada()
    for id_produto in ids_produtos:
        lista_encadeada_simples.inserir_ordenado(id_produto)
    print(f"   Lista Encadeada Simples: {lista_encadeada_simples.tamanho} elementos")

    # Criando lista encadeada com índices
    lista_encadeada_indices = ListaEncadeadaIndexada()
    for id_produto in ids_produtos:
        lista_encadeada_indices.inserir_ordenado(id_produto)
    print(f"   Lista Encadeada com Índices: {lista_encadeada_indices.tamanho} elementos")

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

    # Calculando a diferença:
    print("\n" + "_" * 60 + "\n")
    print("COMPARAÇÃO DE DESEMPENHO" + "\n")
    print(f"Lista Encadeada Simples: {total_tempo_busca_sequencial:.10f} s")
    print(f"Lista com Índices: {total_tempo_busca_binaria:.10f} s")
    
    if total_tempo_busca_binaria > 0:
        if total_tempo_busca_sequencial > total_tempo_busca_binaria:
            fator = total_tempo_busca_sequencial / total_tempo_busca_binaria
            print(f"\nA busca com índices foi {fator:.2f}x mais rápida\n")
        else:
            fator = total_tempo_busca_binaria / total_tempo_busca_sequencial
            print(f"\nA busca sequencial foi {fator:.2f}x mais rápida\n")
    
    # Gerando gráfico de desempenho    
    categorias = ['Lista Encadeada\n(Busca Sequencial)', 'Lista com Índices\n(Busca Binária)']
    tempos_totais = [total_tempo_busca_sequencial * 1000, total_tempo_busca_binaria * 1000]  # Converter para ms para melhor visualização
    
    plot.figure(figsize=(10, 6))
    barras = plot.bar(categorias, tempos_totais, color=['#FF6B6B', '#4ECDC4'], width=0.6)
    
    # Adicionar valores nas barras
    for barra in barras:
        altura = barra.get_height()
        plot.text(barra.get_x() + barra.get_width()/2., altura,
                 f'{altura:.6f} ms',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plot.xlabel('Tipo de Lista', fontsize=12, fontweight='bold')
    plot.ylabel('Tempo Total de Busca (ms)', fontsize=12, fontweight='bold')
    plot.title('Comparação de Desempenho: Busca Sequencial vs Busca Binária', 
              fontsize=14, fontweight='bold', pad=20)
    plot.grid(axis='y', alpha=0.3, linestyle='--')
    plot.tight_layout()
    
    nome_arquivo_grafico = 'projeto_1_comparacao_desempenho.png'
    plot.savefig(nome_arquivo_grafico, dpi=300, bbox_inches='tight')
    plot.close()
    
    print(f"> Gráfico gerado: {nome_arquivo_grafico}")
    
    print("_" * 60 + "\n")
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!" + "\n")

if __name__ == "__main__":
    main()
    

