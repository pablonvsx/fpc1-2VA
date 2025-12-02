"""
Projeto 3 - Comparação de Algoritmos de Ordenação para Produtos
Implementa e compara Insertion Sort vs Merge Sort para ordenação de produtos
por diferentes critérios (preço, estoque, popularidade, data, nome)
"""

import time
from datetime import datetime
from typing import List, Dict, Tuple


class OrdenadorProdutos:
    """Classe responsável por ordenar produtos usando diferentes algoritmos"""
    
    def __init__(self):
        self.tempo_execucao = 0
    
    def _comparar_elementos(self, elem1: any, elem2: any, criterio: str) -> int:
        """
        Compara dois elementos baseado no critério especificado.
        Retorna:
            -1 se elem1 < elem2
             0 se elem1 == elem2
             1 se elem1 > elem2
        """
        if criterio == "data_cadastro":
            # Converter strings de data para objetos datetime
            data1 = datetime.strptime(elem1, "%Y-%m-%d")
            data2 = datetime.strptime(elem2, "%Y-%m-%d")
            if data1 < data2:
                return -1
            elif data1 > data2:
                return 1
            else:
                return 0
        else:
            if elem1 < elem2:
                return -1
            elif elem1 > elem2:
                return 1
            else:
                return 0
    
    def _insertion_sort(self, lista: List[Dict], criterio: str) -> List[Dict]:
        """
        Implementa o algoritmo Insertion Sort para ordenar produtos.
        
        Args:
            lista: Lista de dicionários (produtos)
            criterio: Campo pelo qual ordenar
            
        Returns:
            Nova lista ordenada
        """
        # Criar uma cópia para não modificar a original
        resultado = lista.copy()
        n = len(resultado)
        
        # Começar a partir do segundo elemento
        for i in range(1, n):
            chave = resultado[i][criterio]
            j = i - 1
            
            # Comparar com elementos anteriores
            while j >= 0 and self._comparar_elementos(resultado[j][criterio], chave, criterio) > 0:
                resultado[j + 1] = resultado[j]
                j -= 1
            
            resultado[j + 1] = resultado[i]
        
        return resultado
    
    def _merge(self, esquerda: List[Dict], direita: List[Dict], criterio: str) -> List[Dict]:
        """
        Combina duas sublistas ordenadas em uma única lista ordenada.
        
        Args:
            esquerda: Sublista esquerda ordenada
            direita: Sublista direita ordenada
            criterio: Campo pelo qual ordenar
            
        Returns:
            Lista combinada e ordenada
        """
        resultado = []
        i = j = 0
        
        while i < len(esquerda) and j < len(direita):
            if self._comparar_elementos(esquerda[i][criterio], direita[j][criterio], criterio) <= 0:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        
        # Adicionar elementos restantes
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        
        return resultado
    
    def _merge_sort_recursivo(self, lista: List[Dict], criterio: str) -> List[Dict]:
        """
        Implementa o algoritmo Merge Sort recursivamente.
        
        Args:
            lista: Lista de dicionários a ordenar
            criterio: Campo pelo qual ordenar
            
        Returns:
            Lista ordenada
        """
        if len(lista) <= 1:
            return lista
        
        # Dividir a lista no meio
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        
        # Ordenar recursivamente as duas metades
        esquerda_ordenada = self._merge_sort_recursivo(esquerda, criterio)
        direita_ordenada = self._merge_sort_recursivo(direita, criterio)
        
        # Combinar as duas metades ordenadas
        return self._merge(esquerda_ordenada, direita_ordenada, criterio)
    
    def _merge_sort(self, lista: List[Dict], criterio: str) -> List[Dict]:
        """
        Wrapper para Merge Sort que preserva a lista original.
        
        Args:
            lista: Lista de dicionários a ordenar
            criterio: Campo pelo qual ordenar
            
        Returns:
            Lista ordenada
        """
        return self._merge_sort_recursivo(lista.copy(), criterio)
    
    def ordenar_produtos(self, lista_produtos: List[Dict], criterio: str, algoritmo: str) -> List[Dict]:
        """
        Ordena uma lista de produtos usando o algoritmo e critério especificados.
        Mede automaticamente o tempo de execução.
        
        Args:
            lista_produtos: Lista de dicionários representando produtos
            criterio: Campo para ordenação ("preco", "estoque", "popularidade", "data", "nome")
            algoritmo: Algoritmo a usar ("insercao" ou "intercalacao")
            
        Returns:
            Lista de produtos ordenada
            
        Raises:
            ValueError: Se critério ou algoritmo inválidos
        """
        # Validar critério e mapear para campo real
        criterios_validos = {"preco", "estoque", "popularidade", "data", "nome"}
        if criterio not in criterios_validos:
            raise ValueError(f"Critério inválido: {criterio}. Válidos: {criterios_validos}")
        
        # Mapear "data" para "data_cadastro"
        campo_ordenacao = "data_cadastro" if criterio == "data" else criterio
        
        # Validar algoritmo
        algoritmos_validos = {"insercao", "intercalacao"}
        if algoritmo not in algoritmos_validos:
            raise ValueError(f"Algoritmo inválido: {algoritmo}. Válidos: {algoritmos_validos}")
        
        # Medir tempo de execução
        tempo_inicio = time.time()
        
        if algoritmo == "insercao":
            resultado = self._insertion_sort(lista_produtos, campo_ordenacao)
        else:  # intercalacao
            resultado = self._merge_sort(lista_produtos, campo_ordenacao)
        
        tempo_final = time.time()
        self.tempo_execucao = tempo_final - tempo_inicio
        
        return resultado


def carregar_produtos(nome_arquivo: str) -> List[Dict]:
    """
    Carrega produtos de um arquivo de texto.
    
    Formato esperado: id | nome | preco | estoque | popularidade | data_cadastro
    
    Args:
        nome_arquivo: Caminho do arquivo
        
    Returns:
        Lista de dicionários com produtos
    """
    produtos = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.rstrip('\n')
                if linha:  # Ignorar linhas vazias
                    partes = [p.strip() for p in linha.split('|')]
                    if len(partes) == 6:
                        try:
                            produto = {
                                'id': partes[0],
                                'nome': partes[1],
                                'preco': float(partes[2]),
                                'estoque': int(partes[3]),
                                'popularidade': int(partes[4]),
                                'data_cadastro': partes[5]
                            }
                            produtos.append(produto)
                        except (ValueError, IndexError) as e:
                            continue
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return []
    
    return produtos


def carregar_requisicoes(nome_arquivo: str) -> List[Tuple[str, str]]:
    """
    Carrega requisições de ordenação de um arquivo.
    
    Formato esperado: criterio | algoritmo
    
    Args:
        nome_arquivo: Caminho do arquivo
        
    Returns:
        Lista de tuplas (criterio, algoritmo)
    """
    requisicoes = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:  # Ignorar linhas vazias
                    partes = linha.split('|')
                    if len(partes) == 2:
                        criterio = partes[0].strip()
                        algoritmo = partes[1].strip()
                        requisicoes.append((criterio, algoritmo))
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []
    
    return requisicoes


def salvar_resultado(produtos: List[Dict], criterio: str, algoritmo: str, tempo_execucao: float) -> str:
    """
    Salva produtos ordenados em um arquivo de resultado.
    
    Formato: id | nome | preco | estoque | popularidade | data_cadastro
    Nome do arquivo: projeto_3_resultado_ALGORITMO_CRITERIO.txt
    
    Args:
        produtos: Lista de produtos ordenados
        criterio: Critério utilizado
        algoritmo: Algoritmo utilizado
        tempo_execucao: Tempo de execução em segundos
        
    Returns:
        Nome do arquivo criado
    """
    nome_arquivo = f"projeto_3_resultado_{algoritmo}_{criterio}.txt"
    
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for produto in produtos:
                # Formatar com padding (zeros à esquerda)
                preco_fmt = f"{produto['preco']:010.2f}"
                estoque_fmt = f"{produto['estoque']:05d}"
                popularidade_fmt = f"{produto['popularidade']:05d}"
                
                linha = f"{produto['id']} | {produto['nome']:<40} | {preco_fmt} | {estoque_fmt} | {popularidade_fmt} | {produto['data_cadastro']}\n"
                arquivo.write(linha)
        
        return nome_arquivo
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")
        return ""


def main():
    """Função principal que executa o Projeto 3"""
    
    print("="*70)
    print("PROJETO 3 - COMPARAÇÃO DE ALGORITMOS DE ORDENAÇÃO")
    print("="*70)
    
    # Carregar produtos
    print("\n> Carregando produtos...")
    produtos = carregar_produtos('projeto_3_lista_produtos_entrada.txt')
    
    if not produtos:
        print("Erro: Nenhum produto foi carregado.")
        return
    
    print(f"✓ {len(produtos)} produtos carregados com sucesso")
    
    # Carregar requisições
    print("\n> Carregando requisições de ordenação...")
    requisicoes = carregar_requisicoes('projeto_3_requisicoes_listagem.txt')
    
    if not requisicoes:
        print("Erro: Nenhuma requisição foi carregada.")
        return
    
    print(f"✓ {len(requisicoes)} requisições carregadas com sucesso")
    
    # Processar cada requisição
    print("\n" + "="*70)
    print("PROCESSANDO REQUISIÇÕES")
    print("="*70)
    
    ordenador = OrdenadorProdutos()
    resultados_tempo = []
    
    for idx, (criterio, algoritmo) in enumerate(requisicoes, 1):
        print(f"\n[{idx}/{len(requisicoes)}] Ordenando por {criterio} usando {algoritmo}...")
        
        try:
            # Ordenar produtos
            produtos_ordenados = ordenador.ordenar_produtos(produtos, criterio, algoritmo)
            tempo = ordenador.tempo_execucao
            
            # Salvar resultado
            nome_arquivo = salvar_resultado(produtos_ordenados, criterio, algoritmo, tempo)
            
            if nome_arquivo:
                print(f"      ✓ Resultado salvo em: {nome_arquivo}")
                print(f"      ✓ Tempo de execução: {tempo*1000:.4f} ms ({tempo:.6f} s)")
                resultados_tempo.append({
                    'criterio': criterio,
                    'algoritmo': algoritmo,
                    'tempo': tempo
                })
            
        except ValueError as e:
            print(f"      ✗ Erro: {e}")
        except Exception as e:
            print(f"      ✗ Erro inesperado: {e}")
    
    # Resumo final
    print("\n" + "="*70)
    print("RESUMO DOS RESULTADOS")
    print("="*70)
    print(f"\nTotal de requisições processadas: {len(resultados_tempo)}")
    
    if resultados_tempo:
        print("\nTempo de execução por requisição:")
        print("-" * 70)
        print(f"{'Algoritmo':<15} | {'Critério':<15} | {'Tempo (ms)':<15} | {'Tempo (s)':<12}")
        print("-" * 70)
        
        for resultado in resultados_tempo:
            tempo_ms = resultado['tempo'] * 1000
            tempo_s = resultado['tempo']
            print(f"{resultado['algoritmo']:<15} | {resultado['criterio']:<15} | {tempo_ms:>14.4f} | {tempo_s:>11.6f}")
        
        # Comparação Insertion vs Merge para mesmo critério
        print("\n" + "-" * 70)
        print("COMPARAÇÃO ENTRE ALGORITMOS (para mesmo critério):")
        print("-" * 70)
        
        criterios_unicos = set(r['criterio'] for r in resultados_tempo)
        
        for criterio in sorted(criterios_unicos):
            tempos_criterio = [r for r in resultados_tempo if r['criterio'] == criterio]
            
            if len(tempos_criterio) == 2:
                insercao = next((r for r in tempos_criterio if r['algoritmo'] == 'insercao'), None)
                intercalacao = next((r for r in tempos_criterio if r['algoritmo'] == 'intercalacao'), None)
                
                if insercao and intercalacao:
                    diferenca = insercao['tempo'] - intercalacao['tempo']
                    percentual = (diferenca / intercalacao['tempo']) * 100 if intercalacao['tempo'] > 0 else 0
                    
                    print(f"\nCritério: {criterio}")
                    print(f"  Insertion: {insercao['tempo']*1000:.4f} ms")
                    print(f"  Merge:     {intercalacao['tempo']*1000:.4f} ms")
                    
                    if diferenca > 0:
                        print(f"  → Merge é {abs(percentual):.2f}% mais rápido")
                    else:
                        print(f"  → Insertion é {abs(percentual):.2f}% mais rápido")
    
    print("\n" + "="*70)
    print("Projeto 3 finalizado com sucesso!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
