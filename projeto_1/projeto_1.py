"""
Projeto 1 - Comparação Completa entre Busca Sequencial e Busca Binária
Implementação, execução, geração de arquivos de resultados e gráficos comparativos
"""

import sys
import os
# Adicionar o diretório pai ao path para importar estruturas_dados
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estruturas_dados.lista_encadeada import ListaEncadeada
from estruturas_dados.lista_encadeada_com_indices import ListaEncadeadaIndexada
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
    print("Projeto 1 - Comparação de Performance: Busca Sequencial vs Busca Binária")
    print("_"*60)

    # Carregamento dos dados
    print("\n> Carregando dados...")
    ids_produtos = carregar_ids('projeto_1/projeto_1_lista_IDs_entrada.txt')
    ids_busca = carregar_ids('projeto_1/projeto_1_lista_IDs_busca.txt')
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

    # LISTA ENCADEADA COM ÍNDICES (BUSCA BINÁRIA)
    print("\n> Criando Lista Encadeada com Índices...")
    lista_encadeada_indices = ListaEncadeadaIndexada()
    
    print("   Inserindo IDs na lista...")
    itens_inseridos_bin = 0
    itens_duplicados_bin = 0
    for id_produto in ids_produtos:
        resultado = lista_encadeada_indices.inserir_ordenado(id_produto)
        if resultado == 1:
            itens_inseridos_bin += 1
        else:
            itens_duplicados_bin += 1
    
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

    # Comparação e resultados
    print("\n" + "_" * 60 + "\n")
    print("COMPARAÇÃO DE DESEMPENHO" + "\n")
    print(f"Lista Encadeada Simples (Busca Sequencial): {total_tempo_busca_sequencial:.10f} s")
    print(f"Lista com Índices (Busca Binária): {total_tempo_busca_binaria:.10f} s")
    
    if total_tempo_busca_binaria > 0:
        if total_tempo_busca_sequencial > total_tempo_busca_binaria:
            fator = total_tempo_busca_sequencial / total_tempo_busca_binaria
            print(f"\nA busca binária foi {fator:.2f}x mais rápida")
        else:
            fator = total_tempo_busca_binaria / total_tempo_busca_sequencial
            print(f"\nA busca sequencial foi {fator:.2f}x mais rápida")
    print()

    # Salvar arquivos de resultado
    print("> Salvando arquivos de resultado...")
    
    with open('projeto_1/projeto_1_resultado_busca_sequencial.txt', 'w') as arquivo:
        for id_busca, resultado in resultados_busca_sequencial:
            arquivo.write(f"{resultado}\n")
    print("   Arquivo gerado: projeto_1_resultado_busca_sequencial.txt")
    
    with open('projeto_1/projeto_1_resultado_busca_binaria.txt', 'w') as arquivo:
        for id_busca, resultado in resultados_busca_binaria:
            arquivo.write(f"{resultado}\n")
    print("   Arquivo gerado: projeto_1_resultado_busca_binaria.txt")
    
    # Geração de gráfico comparativo
    print("\n> Gerando gráfico de desempenho...")
    
    categorias = ['Lista Encadeada\n(Busca Sequencial)', 'Lista com Índices\n(Busca Binária)']
    tempos_totais = [total_tempo_busca_sequencial * 1000, total_tempo_busca_binaria * 1000]  # Converter para ms
    
    plot.figure(figsize=(10, 7))
    barras = plot.bar(categorias, tempos_totais, color=['#001F5C', '#808080'], width=0.6)
    
    # Calcular fator comparativo
    if total_tempo_busca_sequencial > total_tempo_busca_binaria:
        fator = total_tempo_busca_sequencial / total_tempo_busca_binaria
    else:
        fator = total_tempo_busca_binaria / total_tempo_busca_sequencial
    
    # Adicionar valores nas barras com fator comparativo
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        if i == 0 and total_tempo_busca_sequencial > total_tempo_busca_binaria:  # Busca Sequencial (mais lenta)
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.6f} ms\n({fator:.1f}x t(binária))',
                     ha='center', va='bottom', fontsize=9, fontweight='bold')
        elif i == 1 and total_tempo_busca_binaria > total_tempo_busca_sequencial:  # Busca Binária (mais lenta)
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.6f} ms\n({fator:.1f}x t(sequencial))',
                     ha='center', va='bottom', fontsize=9, fontweight='bold')
        else:
            plot.text(barra.get_x() + barra.get_width()/2., altura,
                     f'{altura:.6f} ms',
                     ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Ajustar limites do eixo Y para dar mais espaço
    y_max = max(tempos_totais) * 1.15
    plot.ylim(0, y_max)
    
    plot.xlabel('Tipo de Lista', fontsize=12, fontweight='bold')
    plot.ylabel('Tempo Total de Busca (ms)', fontsize=12, fontweight='bold')
    plot.title('Comparação de Desempenho: Busca Sequencial vs Busca Binária', 
              fontsize=14, fontweight='bold', pad=20)
    plot.grid(axis='y', alpha=0.3, linestyle='--')
    plot.tight_layout()
    
    nome_arquivo_grafico = 'projeto_1/projeto_1_comparacao_desempenho.png'
    plot.savefig(nome_arquivo_grafico, dpi=300, bbox_inches='tight')
    plot.close()
    
    print(f"   Gráfico gerado: {nome_arquivo_grafico}")
    
    print("\n" + "_" * 60)
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")

if __name__ == "__main__":
    main()


