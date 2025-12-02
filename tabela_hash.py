"""
Projeto 2 - Tabela Hash com Encadeamento Separado
Implementação de uma tabela hash com tratamento de colisões por encadeamento separado.
Cada posição da tabela contém uma lista encadeada para armazenar os elementos que colidem.
"""

class No:
    # Nó da lista encadeada que armazena um ID de produto
    def __init__(self, id_produto):
        self.id_produto = id_produto
        self.proximo = None

class TabelaHash:
    # Tabela hash com encadeamento separado
    def __init__(self, tamanho = 7000):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def _hash(self, id_produto):
        # Função hash simples usando o operador módulo
        return id_produto % self.tamanho

    def inserir(self, id_produto):
        # Insere um ID de produto na tabela hash
        indice = self._hash(id_produto)
        novo_no = No(id_produto)

        # Caso da posição vazia
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_no
            return 1
        
        # Inserção no início da lista encadeada
        atual = self.tabela[indice]
        if atual.id_produto == id_produto:
            return -1  # ID já existe

        while atual.proximo is not None:
            if atual.proximo.id_produto == id_produto:
                return -1  # ID já existe
            atual = atual.proximo

        atual.proximo = novo_no
        return 1

    def buscar(self, id_produto):
        # Busca um ID de produto na tabela hash
        indice = self._hash(id_produto)
        atual = self.tabela[indice]

        while atual is not None:
            if atual.id_produto == id_produto:
                return 1  # ID encontrado
            atual = atual.proximo

        return -1  # ID não encontrado
""" 
# --- Área de Teste Rápido ---
# Vamos testar se a lógica básica funciona antes de ler os arquivos
tabela = TabelaHash()

# Inserindo alguns valores
tabela.inserir(10)
tabela.inserir(7010) # 7010 % 7000 = 10 (vai colidir com o 10 na posição 10)
tabela.inserir(5)

# Buscando
print(f"Busca 10: {tabela.buscar(10)}")   # Esperado: 1
print(f"Busca 7010: {tabela.buscar(7010)}") # Esperado: 1
print(f"Busca 99: {tabela.buscar(99)}")   # Esperado: -1   
""" 
def carregar_ids(nome_arquivo):
    # Carrega IDs de produtos de um arquivo texto
    lista_de_ids = []
    try:
        with open(nome_arquivo, 'r') as arquivo_entrada:
            for linha in arquivo_entrada:
                id_produto = linha.strip()
                if id_produto:
                   lista_de_ids.append(int(id_produto))
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    return lista_de_ids

def main():
    import time
    
    print("Projeto 2 - Tabela Hash com Encadeamento Separado")
    tabela_hash = TabelaHash()
    
    # Carregar IDs do arquivo de entrada
    print("\n> Carregando IDs do arquivo de entrada...")
    ids_entrada = carregar_ids('projeto_1_lista_IDs_entrada.txt')
    
    # Inserir IDs na tabela hash
    print("\n> Inserindo IDs na tabela hash...")
    itens_inseridos = 0
    itens_duplicados = 0
    for id_produto in ids_entrada:
        resultado_insercao = tabela_hash.inserir(id_produto)
        if resultado_insercao == 1:
            itens_inseridos += 1
        else:
            itens_duplicados += 1
    
    print(f"   Total de IDs inseridos: {itens_inseridos}")
    print(f"   IDs duplicados ignorados: {itens_duplicados}")
    
    # Calcular quantos elementos existem na tabela
    total_elementos = 0
    posicoes_ocupadas = 0
    for posicao in tabela_hash.tabela:
        if posicao is not None:
            posicoes_ocupadas += 1
            atual = posicao
            while atual is not None:
                total_elementos += 1
                atual = atual.proximo
    
    print(f"\n> Tamanho da tabela hash: {tabela_hash.tamanho} posições")
    print(f"> Posições ocupadas: {posicoes_ocupadas}")
    print(f"> Total de elementos armazenados: {total_elementos}")

    # Carregar IDs para busca
    print("\n> Carregando IDs para busca...")
    ids_busca = carregar_ids('projeto_1_lista_IDs_busca.txt')
    print(f"   Total de IDs carregados para busca: {len(ids_busca)}")

    # Realizar buscas e medir tempo
    print("\n> Realizando buscas na tabela hash...")

    resultados_busca = []
    tempo_total = 0.0
    itens_encontrados = 0

    for id_busca in ids_busca:
        tempo_inicio = time.perf_counter()
        resultado = tabela_hash.buscar(id_busca)
        tempo_fim = time.perf_counter()
        tempo = tempo_fim - tempo_inicio
        tempo_total += tempo

        resultados_busca.append((id_busca, resultado))
        if resultado == 1:
            itens_encontrados += 1
    
    print("   Buscas concluídas!")
    
    # Exibir resumo final
    print("\n" + "_" * 60)
    print("RESUMO DA BUSCA")
    print("_" * 60)
    print(f"Itens buscados: {len(ids_busca)}")
    print(f"Itens encontrados: {itens_encontrados}")
    print(f"Tempo total de busca: {tempo_total:.10f} s")
    if len(ids_busca) > 0:
        print(f"Tempo médio por busca: {tempo_total / len(ids_busca):.10f} s")
    print("_" * 60)
    
    # Gerar arquivo de saída
    with open('projeto_2_lista_IDs_resultado.txt', 'w') as arquivo_saida:
        for id_busca, resultado in resultados_busca:
            arquivo_saida.write(f"{resultado}\n")
    print("\n> Arquivo gerado: projeto_2_lista_IDs_resultado.txt")
    
    print("\n" + "_" * 60)
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")


if __name__ == "__main__":
    main()

