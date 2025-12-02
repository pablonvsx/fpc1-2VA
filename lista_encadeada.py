"""

Projeto 1 - Implementação de Lista Encadeada Ordenada para Gerenciamento de IDs de Produtos
Sistema de e-commerce com busca sequencial em lista encadeada"""

import time

class No:
    # Construtor do nó
    def __init__(self, id_produto):
        self.id_produto = id_produto
        self.proximo = None

class ListaEncadeada:
    # Construtor da lista
    def __init__(self):
        self.ponta = None
        self.tamanho = 0

    def inserir_ordenado(self, id_produto):
        # Insere um ID de produto na lista de forma ordenada e retorna
        # 1 se inserido com sucesso e -1 se já existe
        novo_no = No(id_produto)

        # Caso da lista vazia
        if self.ponta is None:
            self.ponta = novo_no
            self.tamanho += 1
            return 1
        
        # Caso de inserção no início
        if id_produto < self.ponta.id_produto:
            novo_no.proximo = self.ponta
            self.ponta = novo_no
            self.tamanho += 1
            return 1
        
        # ID já existe no início
        if id_produto == self.ponta.id_produto:
            return -1
        
        # Procurar posição correta
        atual = self.ponta
        while atual.proximo is not None and atual.proximo.id_produto < id_produto:
            atual = atual.proximo

        # Verificar se o ID já existe
        if atual.proximo is not None and atual.proximo.id_produto == id_produto:
            return -1
        
        # Inserir na posição correta
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        self.tamanho += 1
        return 1

    def buscar(self, id_produto):
        # Busca um ID de produto na lista e retorna 1 se encontrado e -1 se não encontrado
        atual = self.ponta
        while atual is not None:
            if atual.id_produto == id_produto:
                return 1
            atual = atual.proximo
        return -1
    
    def exibir(self):
        # Exibe todos os IDs de produtos na lista
        atual = self.ponta
        ids = []
        while atual is not None:
            ids.append(str(atual.id_produto))
            atual = atual.proximo
        return " -> ".join(ids) if ids else "Lista vazia"
    
    def obter_todos_ids(self):
        # Retorna uma lista com todos os IDs de produtos
        ids = []
        atual = self.ponta
        while atual is not None:
            ids.append(atual.id_produto)
            atual = atual.proximo
        return ids

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
    print("Projeto 1 - Lista Encadeada")
    lista_encadeada = ListaEncadeada()
    # Carregar IDs do arquivo de entrada
    print("\n> Carregando IDs do arquivo de entrada...")
    ids_entrada = carregar_ids('projeto_1_lista_IDs_entrada.txt')

    # Inserir Ids na lista
    print("\n> Inserindo IDs na lista encadeada ordenada...")
    itens_inseridos = 0
    itens_duplicados = 0
    for id_produto in ids_entrada:
        resultado_insercao = lista_encadeada.inserir_ordenado(id_produto)
        if resultado_insercao == 1:
            itens_inseridos += 1
        else:
            itens_duplicados += 1
    
    print(f"   Total de IDs inseridos: {itens_inseridos}")
    print(f"   IDs duplicados ignorados: {itens_duplicados}")
    
    print(f"\n> Tamanho da lista encadeada: {lista_encadeada.tamanho} elementos")

    # Carregar IDs para busca
    print("\n> Carregando IDs para busca...")
    ids_busca = carregar_ids('projeto_1_lista_IDs_busca.txt')
    print(f"   Total de IDs carregados para busca: {len(ids_busca)}")

    # Realizar buscas e medir tempo
    print("\n> Realizando buscas na lista encadeada...")

    resultados_busca = []
    tempo_total = 0.0
    itens_encontrados = 0

    for id_busca in ids_busca:
        tempo_inicio = time.perf_counter()
        resultado = lista_encadeada.buscar(id_busca)
        tempo_fim = time.perf_counter()
        tempo = tempo_fim - tempo_inicio
        tempo_total += tempo

        resultados_busca.append((id_busca, resultado))
        if resultado == 1:
            itens_encontrados += 1
    print("   Buscas concluídas")
    
    # Exibir resumo final
    print("_" * 60+'\n')
    print("> RESUMO DA BUSCA\n")
    print(f"Itens buscados: {len(ids_busca)}")
    print(f"Itens encontrados: {itens_encontrados}")
    print(f"Tempo total de busca: {tempo_total:.10f} s")
    if len(ids_busca) > 0:
        print(f"Tempo médio por busca: {tempo_total / len(ids_busca):.10f} s")
    print(f"{'_'*60}")
    
    # Gerar arquivo de saída
    with open('projeto_1_resultado_busca_sequencial.txt', 'w') as arquivo_saida:
        for id_busca, resultado in resultados_busca:
            arquivo_saida.write(f"{resultado}\n")
    print("\n> Arquivo com resultados gerado: projeto_1_resultado_busca_sequencial.txt")
    
    print("_" * 60+'\n')
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")
    print( "_" * 60)


if __name__ == "__main__":
    main()

