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


