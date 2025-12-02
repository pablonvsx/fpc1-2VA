"""
Validador de Resultados do Projeto 3
Verifica se os resultados estão no formato correto
"""

import os
from pathlib import Path

def validar_arquivo_resultado(nome_arquivo):
    """Valida estrutura de um arquivo de resultado"""
    
    if not os.path.exists(nome_arquivo):
        return False, f"Arquivo não encontrado: {nome_arquivo}"
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        if len(linhas) == 0:
            return False, "Arquivo vazio"
        
        if len(linhas) != 10000:
            return False, f"Arquivo contém {len(linhas)} linhas, esperado 10000"
        
        # Validar primeira linha
        primeira_linha = linhas[0].strip()
        partes = [p.strip() for p in primeira_linha.split('|')]
        
        if len(partes) != 6:
            return False, f"Primeira linha tem {len(partes)} campos, esperado 6"
        
        id_prod, nome, preco, estoque, popularidade, data = partes
        
        # Validar formato do ID
        if not id_prod.startswith('ID'):
            return False, f"ID inválido: {id_prod}"
        
        # Validar formato de preço (deve ter formato X.XX)
        try:
            preco_val = float(preco)
            if preco_val < 0 or preco_val > 10000:
                return False, f"Preço fora do intervalo esperado: {preco_val}"
        except ValueError:
            return False, f"Preço não é número: {preco}"
        
        # Validar estoque
        try:
            estoque_val = int(estoque)
            if estoque_val < 0 or estoque_val > 500:
                return False, f"Estoque fora do intervalo: {estoque_val}"
        except ValueError:
            return False, f"Estoque não é número: {estoque}"
        
        # Validar data
        from datetime import datetime
        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            return False, f"Data em formato inválido: {data}"
        
        return True, "OK"
    
    except Exception as e:
        return False, f"Erro ao validar: {str(e)}"


def main():
    print("="*70)
    print("VALIDAÇÃO DE RESULTADOS - PROJETO 3")
    print("="*70 + "\n")
    
    # Arquivos esperados
    arquivos_esperados = [
        'projeto_3_resultado_insercao_preco.txt',
        'projeto_3_resultado_intercalacao_preco.txt',
        'projeto_3_resultado_insercao_estoque.txt',
        'projeto_3_resultado_intercalacao_estoque.txt',
        'projeto_3_resultado_insercao_popularidade.txt',
        'projeto_3_resultado_intercalacao_popularidade.txt',
        'projeto_3_resultado_insercao_data.txt',
        'projeto_3_resultado_intercalacao_data.txt',
        'projeto_3_resultado_insercao_nome.txt',
        'projeto_3_resultado_intercalacao_nome.txt',
    ]
    
    resultados_validos = 0
    resultados_invalidos = 0
    
    for arquivo in arquivos_esperados:
        valido, mensagem = validar_arquivo_resultado(arquivo)
        
        status = "✓" if valido else "✗"
        print(f"{status} {arquivo:<45} {mensagem}")
        
        if valido:
            resultados_validos += 1
            # Obter tamanho do arquivo
            tamanho = os.path.getsize(arquivo)
            tamanho_kb = tamanho / 1024
            print(f"  └─ Tamanho: {tamanho_kb:.1f} KB")
        else:
            resultados_invalidos += 1
    
    print("\n" + "="*70)
    print(f"RESUMO: {resultados_validos} arquivos válidos, {resultados_invalidos} inválidos")
    print("="*70)
    
    # Verificar arquivos de suporte
    print("\n" + "="*70)
    print("ARQUIVOS DE SUPORTE")
    print("="*70 + "\n")
    
    arquivos_suporte = [
        ('projeto_3_lista_produtos_entrada.txt', 'Entrada com 10.000 produtos'),
        ('projeto_3_requisicoes_listagem.txt', 'Arquivo de requisições'),
        ('projeto_3.py', 'Código principal'),
        ('gerar_dados_projeto_3.py', 'Gerador de dados'),
        ('gerar_graficos_projeto_3.py', 'Gerador de gráficos'),
        ('projeto_3_comparacao_desempenho.png', 'Gráfico de comparação'),
        ('projeto_3_speedup.png', 'Gráfico de speedup'),
        ('PROJETO_3_RELATORIO.md', 'Relatório de análise'),
    ]
    
    for arquivo, descricao in arquivos_suporte:
        existe = "✓" if os.path.exists(arquivo) else "✗"
        print(f"{existe} {arquivo:<40} {descricao}")
    
    print("\n" + "="*70)
    print("VALIDAÇÃO COMPLETA")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
