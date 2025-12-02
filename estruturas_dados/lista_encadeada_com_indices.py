"""
Projeto 1 - Implementação de Lista Encadeada Ordenada para Gerenciamento de IDs de Produtos
Sistema de e-commerce com busca binária usando vetor de índices
"""

class No:
    # Nó da lista encadeada que armazena um ID de produto
    def __init__(self, id_produto):
        self.id_produto = id_produto
        self.proximo = None

class ListaEncadeadaIndexada:
    # Lista encadeada com vetor de índices para busca binária
    # Armazena tuplas no vetor_indices (id, referência_para_nó)
    def __init__(self, auto_indexar=True):
        self.ponta = None
        self.tamanho = 0
        self.vetor_indices = []
        self.auto_indexar = auto_indexar  # Se True, atualiza índices a cada inserção

    def inserir_ordenado(self, id_produto):
        # Insere um ID de produto na lista mantendo a ordem crescente
        # Atualiza o vetor de índices e retorna 1 se inserido com sucesso, -1 se já existe
        novo_no = No(id_produto)

        # Caso da lista vazia
        if self.ponta is None:
            self.ponta = novo_no
            self.tamanho += 1
            if self.auto_indexar:
                self._reajustar_indices()
            return 1
        
        # Caso de inserção no início
        if id_produto < self.ponta.id_produto:
            novo_no.proximo = self.ponta
            self.ponta = novo_no
            self.tamanho += 1
            if self.auto_indexar:
                self._reajustar_indices()
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
        if self.auto_indexar:
            self._reajustar_indices()
        return 1
    
    def _reajustar_indices(self):
        # Reconstrói o vetor de índices (usado quando auto_indexar=True)
        self.vetor_indices = []
        atual = self.ponta
        while atual is not None:
            self.vetor_indices.append((atual.id_produto, atual))
            atual = atual.proximo
    
    def construir_indices(self):
        # Constrói o vetor de índices após todas as inserções
        # Deve ser chamado uma única vez após inserir todos os elementos (quando auto_indexar=False)
        self.vetor_indices = []
        atual = self.ponta
        while atual is not None:
            self.vetor_indices.append((atual.id_produto, atual))
            atual = atual.proximo
    
    def busca_binaria(self, id_produto):
        # Realiza busca binária no vetor de índices
        esquerda = 0
        direita = len(self.vetor_indices) - 1
        
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            meio_id = self.vetor_indices[meio][0]
            
            if meio_id == id_produto:
                return 1  # Encontrado
            elif meio_id < id_produto:
                esquerda = meio + 1
            else:
                direita = meio - 1
        
        return -1  # Não encontrado
    
    def exibir(self):
        # Exibe os IDs de produtos na lista
        atual = self.ponta
        ids = []
        while atual is not None:
            ids.append(str(atual.id_produto))
            atual = atual.proximo
        return " -> ".join(ids) if ids else "Lista vazia"
    
    def exibir_vetor_indices(self):
        # Exibe o vetor de índices
        return [id_produto for id_produto, _ in self.vetor_indices]
    
    def obter_todos_ids(self):
        # Retorna uma lista com todos os IDs de produtos
        return [id_produto for id_produto, _ in self.vetor_indices]


