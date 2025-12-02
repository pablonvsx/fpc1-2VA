# PROJETO 3 - COMPARAÇÃO DE ALGORITMOS DE ORDENAÇÃO

## 📋 Resumo Executivo

O Projeto 3 implementa e compara dois algoritmos clássicos de ordenação:
- **Insertion Sort** (Ordenação por Inserção)
- **Merge Sort** (Ordenação por Intercalação)

Os algoritmos foram testados com 10.000 produtos, ordenados por 5 critérios diferentes, resultando em 10 conjuntos de dados para análise comparativa.

---

## 🎯 Objetivo

Comparar o desempenho de dois algoritmos de ordenação em relação a:
1. Diferentes critérios de ordenação
2. Tamanho do dataset (10.000 elementos)
3. Complexidade temporal prática vs teórica

---

## 📊 Resultados de Desempenho

### Tempo de Execução (em milissegundos)

| Critério | Insertion Sort | Merge Sort | Speedup | Vantagem |
|----------|----------------|------------|---------|----------|
| Preço | 3.072,31 ms | 20,45 ms | 150x | Merge |
| Estoque | 3.238,79 ms | 20,53 ms | 158x | Merge |
| Popularidade | 2.638,27 ms | 21,41 ms | 123x | Merge |
| Data | 190.152,40 ms | 689,37 ms | 276x | Merge |
| Nome | 4.255,80 ms | 21,79 ms | 195x | Merge |

---

## 🔍 Análise Detalhada

### 1. **Insertion Sort** - Ordenação por Inserção

**Características:**
- Algoritmo simples e intuitivo
- Espaço O(1) - in-place (não usa memória extra)
- Tempo: O(n²) pior caso, O(n) melhor caso
- Estável (mantém ordem relativa de elementos iguais)

**Desempenho observado:**
- Todos os critérios levaram entre 2,6 e 4,3 segundos
- **Exceção**: Dados de data levaram **190 segundos** (parsing de datas é custoso)
- Prático apenas para listas pequenas (< 1.000 elementos)

### 2. **Merge Sort** - Ordenação por Intercalação

**Características:**
- Algoritmo divide-and-conquer
- Espaço O(n) - requer memória extra
- Tempo: O(n log n) em todos os casos
- Estável (mantém ordem relativa)
- Paralelizável

**Desempenho observado:**
- Todos os critérios levaram entre 20-22 ms (exceto data)
- Consistente e previsível
- Até **276 vezes mais rápido** que Insertion Sort para dados de data

---

## 💡 Insights Principais

### 1. **Complexidade Temporal**
```
Insertion Sort: O(n²) = 10.000² = 100.000.000 operações
Merge Sort:     O(n log n) = 10.000 × 13,3 ≈ 133.000 operações

Razão esperada: ~750x mais rápido
Razão observada: ~150x (overhead de parsing de datas afeta Insertion)
```

### 2. **Overhead de Comparação**
- **Dados numéricos/texto simples**: Comparação rápida
- **Dados de data**: Parsing com `datetime.strptime()` é lento
  - Insertion: Faz 50 milhões de comparações → **parsing lento**
  - Merge: Faz 133 mil comparações → **impacto reduzido**

### 3. **Uso de Memória**
- **Insertion Sort**: Usa apenas 1 lista (economiza RAM)
- **Merge Sort**: Duplica o tamanho em memória durante execução
- Trade-off: Tempo vs Memória

---

## 📁 Arquivos Gerados

### Entrada
- `projeto_3_lista_produtos_entrada.txt` - 10.000 produtos com 6 campos
- `projeto_3_requisicoes_listagem.txt` - 10 requisições de ordenação

### Saída
- `projeto_3_resultado_insercao_preco.txt`
- `projeto_3_resultado_insercao_estoque.txt`
- `projeto_3_resultado_insercao_popularidade.txt`
- `projeto_3_resultado_insercao_data.txt`
- `projeto_3_resultado_insercao_nome.txt`
- `projeto_3_resultado_intercalacao_preco.txt`
- `projeto_3_resultado_intercalacao_estoque.txt`
- `projeto_3_resultado_intercalacao_popularidade.txt`
- `projeto_3_resultado_intercalacao_data.txt`
- `projeto_3_resultado_intercalacao_nome.txt`

### Visualizações
- `projeto_3_comparacao_desempenho.png` - Gráfico de comparação
- `projeto_3_speedup.png` - Gráfico de vantagem relativa

---

## 🏆 Conclusões

### ✅ Quando usar cada algoritmo?

**Insertion Sort:**
- ✓ Listas pequenas (< 50 elementos)
- ✓ Dados quase ordenados
- ✓ Quando espaço em memória é crítico
- ✓ Implementação educacional

**Merge Sort:**
- ✓ Listas grandes (> 1.000 elementos)
- ✓ Garantia de O(n log n)
- ✓ Dados sem padrão de ordenação
- ✓ Aplicações em produção
- ✓ Quando tempo é crítico

### 📌 Recomendação Final

Para a plataforma de e-commerce com produtos, **Merge Sort é a escolha ideal** porque:

1. **Performance garantida**: O(n log n) independente dos dados
2. **Previsibilidade**: Tempo de resposta consistente
3. **Escalabilidade**: Funciona bem com 100.000+ produtos
4. **Memória moderna**: RAM não é mais um fator limitante (2024)

**Speedup obtido:** até **276x mais rápido** para operações com datas

---

## 📈 Implementação

### Algoritmo: Merge Sort

```python
def merge_sort(lista, criterio):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], criterio)
    direita = merge_sort(lista[meio:], criterio)
    
    return merge(esquerda, direita, criterio)
```

**Complexidade:**
- Tempo: O(n log n)
- Espaço: O(n)
- Estabilidade: ✓ Sim

---

## 📚 Referências

- CORMEN, T. H., et al. (2009). "Introduction to Algorithms"
- Algoritmos clássicos de ordenação
- Análise de complexidade assintótica

---

**Data do Relatório:** 2 de Dezembro de 2025
**Autor:** Sistema de Avaliação Automática
**Status:** ✅ Projeto Completo

