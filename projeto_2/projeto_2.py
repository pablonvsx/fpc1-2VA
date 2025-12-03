"""
Projeto 2 - Comparação Completa de Três Métodos de Busca
Implementação, execução, geração de arquivos de resultados e gráficos comparativos
Compara: Busca Sequencial, Busca Binária e Tabela Hash
"""

import sys
import os
# Adicionar o diretório pai ao path para importar estruturas_dados
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from estruturas_dados.lista_encadeada import ListaEncadeada
from estruturas_dados.lista_encadeada_com_indices import ListaEncadeadaIndexada
from estruturas_dados.tabela_hash import TabelaHash
import time
import matplotlib.pyplot as plot

def carregar_ids(nome_arquivo):
    """
    Carrega IDs de produtos de um arquivo de texto
    """
    ids = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    ids.append(int(linha))
    except FileNotFoundError:
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
    return ids

def main():
    print("Projeto 2 - Comparação de Performance: Três Métodos de Busca")
    print("_"*60)

    # Carregamento dos dados
    print("\n> Carregando dados...")
    ids_produtos = carregar_ids('projeto_2/projeto_2_lista_IDs_entrada.txt')
    ids_busca = carregar_ids('projeto_2/projeto_2_lista_IDs_busca.txt')
    print(f"   IDs de produtos carregados: {len(ids_produtos)}")
    print(f"   IDs para busca carregados: {len(ids_busca)}")

    # ========== LISTA ENCADEADA SIMPLES (BUSCA SEQUENCIAL) ==========
    print("\n> Criando Lista Encadeada Simples...")
    lista_encadeada_simples = ListaEncadeada()
    
    print("   Inserindo IDs na lista...")
    itens_inseridos_seq = 0
    itens_duplicados_seq = 0
    for id_produto in ids_produtos:
        resultado = lista_encadeada_simples.inserir_ordenado(id_produto)
        if resultado == 1:
            itens_inseridos_seq += 1
        else:
            itens_duplicados_seq += 1
    
    print(f"   Total de IDs inseridos: {itens_inseridos_seq}")
    print(f"   IDs duplicados ignorados: {itens_duplicados_seq}")
    print(f"   Tamanho da lista: {lista_encadeada_simples.tamanho} elementos")

    print("\n> Realizando buscas sequenciais...")
    resultados_busca_sequencial = []
    total_tempo_busca_sequencial = 0
    itens_encontrados_seq = 0

    for id_busca in ids_busca:
        inicio = time.perf_counter()
        resultado = lista_encadeada_simples.buscar(id_busca)
        fim = time.perf_counter()
        tempo_busca = fim - inicio
        total_tempo_busca_sequencial += tempo_busca
        
        resultados_busca_sequencial.append((id_busca, resultado))
        if resultado == 1:
            itens_encontrados_seq += 1

    print(f"   Buscas concluídas!")
    print(f"   Tempo total: {total_tempo_busca_sequencial:.10f} s")
    print(f"   Tempo médio: {total_tempo_busca_sequencial/len(ids_busca):.10f} s")
    print(f"   IDs encontrados: {itens_encontrados_seq}/{len(ids_busca)}")

    # Lista Encadeada com Índices (Busca Binária)
    print("\n> Criando Lista Encadeada com Índices...")
    lista_encadeada_indices = ListaEncadeadaIndexada(auto_indexar=False)
    
    print("   Inserindo IDs na lista...")
    itens_inseridos_bin = 0
    itens_duplicados_bin = 0
    for id_produto in ids_produtos:
        resultado = lista_encadeada_indices.inserir_ordenado(id_produto)
        if resultado == 1:
            itens_inseridos_bin += 1
        else:
            itens_duplicados_bin += 1
    
    print("   Construindo vetor de índices...")
    lista_encadeada_indices.construir_indices()
    
    print(f"   Total de IDs inseridos: {itens_inseridos_bin}")
    print(f"   IDs duplicados ignorados: {itens_duplicados_bin}")
    print(f"   Tamanho da lista: {lista_encadeada_indices.tamanho} elementos")
    print(f"   Tamanho do vetor de índices: {len(lista_encadeada_indices.vetor_indices)} elementos")

    print("\n> Realizando buscas binárias...")
    resultados_busca_binaria = []
    total_tempo_busca_binaria = 0
    itens_encontrados_bin = 0

    for id_busca in ids_busca:
        inicio = time.perf_counter()
        resultado = lista_encadeada_indices.busca_binaria(id_busca)
        fim = time.perf_counter()
        tempo_busca = fim - inicio
        total_tempo_busca_binaria += tempo_busca
        
        resultados_busca_binaria.append((id_busca, resultado))
        if resultado == 1:
            itens_encontrados_bin += 1
    
    print(f"   Buscas concluídas!")
    print(f"   Tempo total: {total_tempo_busca_binaria:.10f} s")
    print(f"   Tempo médio: {total_tempo_busca_binaria/len(ids_busca):.10f} s")
    print(f"   IDs encontrados: {itens_encontrados_bin}/{len(ids_busca)}")

    # Tabela Hash
    print("\n> Criando Tabela Hash...")
    tabela_hash = TabelaHash()
    
    print("   Inserindo IDs na tabela hash...")
    itens_inseridos_hash = 0
    itens_duplicados_hash = 0
    for id_produto in ids_produtos:
        resultado = tabela_hash.inserir(id_produto)
        if resultado == 1:
            itens_inseridos_hash += 1
        else:
            itens_duplicados_hash += 1
    
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
    
    print(f"   Total de IDs inseridos: {itens_inseridos_hash}")
    print(f"   IDs duplicados ignorados: {itens_duplicados_hash}")
    print(f"   Tamanho da tabela hash: {tabela_hash.tamanho} posições")
    print(f"   Posições ocupadas: {posicoes_ocupadas}")
    print(f"   Total de elementos armazenados: {total_elementos_hash}")

    print("\n> Realizando buscas na tabela hash...")
    resultados_busca_hash = []
    total_tempo_busca_hash = 0
    itens_encontrados_hash = 0

    for id_busca in ids_busca:
        inicio = time.perf_counter()
        resultado = tabela_hash.buscar(id_busca)
        fim = time.perf_counter()
        tempo_busca = fim - inicio
        total_tempo_busca_hash += tempo_busca
        
        resultados_busca_hash.append((id_busca, resultado))
        if resultado == 1:
            itens_encontrados_hash += 1
    
    print(f"   Buscas concluídas!")
    print(f"   Tempo total: {total_tempo_busca_hash:.10f} s")
    print(f"   Tempo médio: {total_tempo_busca_hash/len(ids_busca):.10f} s")
    print(f"   IDs encontrados: {itens_encontrados_hash}/{len(ids_busca)}")

    # Comparação e resultados
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

    # Salvar arquivo de resultado (apenas Tabela Hash - os outros já foram gerados no Projeto 1)
    print("> Salvando arquivo de resultado...")
    
    with open('projeto_2/projeto_2_resultado_tabela_hash.txt', 'w') as arquivo:
        for id_busca, resultado in resultados_busca_hash:
            arquivo.write(f"{resultado}\n")
    print("   Arquivo gerado: projeto_2_resultado_tabela_hash.txt")
    
    # Geração de gráfico comparativo
    print("\n> Gerando gráfico de desempenho...")
    
    categorias = [
        'Lista Encadeada\n(Busca Sequencial)', 
        'Lista com Índices\n(Busca Binária)',
        'Tabela Hash'
    ]
    tempos_totais = [
        total_tempo_busca_sequencial * 1000,
        total_tempo_busca_binaria * 1000,
        total_tempo_busca_hash * 1000
    ]  # Converter para ms
    
    plot.figure(figsize=(12, 7))
    barras = plot.bar(categorias, tempos_totais, color=['#FF6B6B','#4ECDC4', '#95E1D3'], width=0.6)
    
    # Calcular fatores comparativos em relação ao mais rápido
    tempo_min = min(tempos_totais)
    fatores = [t / tempo_min for t in tempos_totais]
    
    # Adicionar valores nas barras com fator comparativo
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        if fatores[i] > 1.01:  # Se for significativamente mais lento
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.6f} ms\n({fatores[i]:.1f}x t({metodo_mais_rapido.lower()}))',
                     ha='center', va='bottom', fontsize=9, fontweight='bold')
        else:  # É o mais rápido
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.6f} ms',
                     ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Ajustar limites do eixo Y para dar mais espaço
    y_max = max(tempos_totais) * 1.15
    plot.ylim(0, y_max)
    
    plot.xlabel('Método de Busca', fontsize=12, fontweight='bold')
    plot.ylabel('Tempo Total de Busca (ms)', fontsize=12, fontweight='bold')
    plot.title('Comparação de Desempenho: Busca Sequencial vs Busca Binária vs Tabela Hash', 
              fontsize=14, fontweight='bold', pad=20)
    plot.grid(axis='y', alpha=0.3, linestyle='--')
    plot.tight_layout()
    
    nome_arquivo_grafico = 'projeto_2/projeto_2_comparacao_desempenho.png'
    plot.savefig(nome_arquivo_grafico, dpi=300, bbox_inches='tight')
    plot.close()
    
    print(f"   Gráfico gerado: {nome_arquivo_grafico}")
    
    print("\n" + "_" * 60)
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")

if __name__ == "__main__":
    main()

