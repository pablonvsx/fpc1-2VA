"""
Pacote com implementações de estruturas de dados:
- ListaEncadeada: Lista encadeada ordenada com busca sequencial
- ListaEncadeadaIndexada: Lista encadeada ordenada com vetor de índices para busca binária
- TabelaHash: Tabela hash com encadeamento separado
"""

from .lista_encadeada import ListaEncadeada, No
from .lista_encadeada_com_indices import ListaEncadeadaIndexada
from .tabela_hash import TabelaHash

__all__ = ['ListaEncadeada', 'ListaEncadeadaIndexada', 'TabelaHash', 'No']
