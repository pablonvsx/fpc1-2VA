"""
Projeto 1 - Implementação de Lista Encadeada Ordenada para Gerenciamento de IDs de Produtos
Sistema de e-commerce com busca sequencial em lista encadeada
"""

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
    
    def inserir_inicio(self, id_produto):
        # Insere um ID de produto no início da lista (usado quando a ordem não importa)
        novo_no = No(id_produto)
        novo_no.proximo = self.ponta
        self.ponta = novo_no
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


