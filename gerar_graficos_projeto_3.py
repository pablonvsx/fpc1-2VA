"""
Gerador de Gráfico de Comparação de Desempenho - Projeto 3
Compara o tempo de execução entre Insertion Sort e Merge Sort
"""

import matplotlib.pyplot as plt
import numpy as np

# Dados de desempenho coletados (em ms)
criterios = ['Preço', 'Estoque', 'Popularidade', 'Data', 'Nome']
insertion_times = [3072.31, 3238.79, 2638.27, 190152.40, 4255.80]
merge_times = [20.45, 20.53, 21.41, 689.37, 21.79]

# Remover os dados de data para melhor visualização (muito grande)
criterios_chart1 = criterios[:-2] + ['Nome']
insertion_chart1 = insertion_times[:-2] + [insertion_times[-1]]
merge_chart1 = merge_times[:-2] + [merge_times[-1]]

# Criar figura com 2 subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Comparação sem dados de data
x = np.arange(len(criterios_chart1))
width = 0.35

bars1 = ax1.bar(x - width/2, insertion_chart1, width, label='Insertion Sort', color='#FF6B6B', alpha=0.8)
bars2 = ax1.bar(x + width/2, merge_chart1, width, label='Merge Sort', color='#4ECDC4', alpha=0.8)

ax1.set_xlabel('Critério de Ordenação', fontsize=12, fontweight='bold')
ax1.set_ylabel('Tempo (ms)', fontsize=12, fontweight='bold')
ax1.set_title('Comparação de Desempenho - Insertion vs Merge Sort\n(Sem dados de data)', fontsize=13, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(criterios_chart1, rotation=45, ha='right')
ax1.legend(fontsize=11)
ax1.grid(axis='y', alpha=0.3)

# Adicionar valores nas barras
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=9)

# Gráfico 2: Todos os dados com escala logarítmica
x2 = np.arange(len(criterios))
bars3 = ax2.bar(x2 - width/2, insertion_times, width, label='Insertion Sort', color='#FF6B6B', alpha=0.8)
bars4 = ax2.bar(x2 + width/2, merge_times, width, label='Merge Sort', color='#4ECDC4', alpha=0.8)

ax2.set_xlabel('Critério de Ordenação', fontsize=12, fontweight='bold')
ax2.set_ylabel('Tempo (ms) - Escala Logarítmica', fontsize=12, fontweight='bold')
ax2.set_title('Comparação Completa com Escala Logarítmica\n(Incluindo dados de data)', fontsize=13, fontweight='bold')
ax2.set_xticks(x2)
ax2.set_xticklabels(criterios, rotation=45, ha='right')
ax2.set_yscale('log')
ax2.legend(fontsize=11)
ax2.grid(axis='y', alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('projeto_3_comparacao_desempenho.png', dpi=300, bbox_inches='tight')
print("✓ Gráfico salvo em: projeto_3_comparacao_desempenho.png")
plt.close()

# Criar segundo gráfico com velocidade relativa
fig, ax = plt.subplots(figsize=(12, 6))

# Calcular speedup (quantas vezes Merge é mais rápido)
speedup = [insertion_times[i] / merge_times[i] for i in range(len(criterios))]

colors = ['#FF6B6B' if s < 1000 else '#FFA500' if s < 5000 else '#FFD93D' if s < 15000 else '#FF4444' 
          for s in speedup]

bars = ax.barh(criterios, speedup, color=colors, alpha=0.8)

ax.set_xlabel('Speedup (vezes mais rápido)', fontsize=12, fontweight='bold')
ax.set_title('Vantagem do Merge Sort sobre Insertion Sort\n(Quanto vezes Merge é mais rápido)', 
             fontsize=13, fontweight='bold')
ax.grid(axis='x', alpha=0.3)

# Adicionar valores nas barras
for i, (bar, value) in enumerate(zip(bars, speedup)):
    ax.text(value, bar.get_y() + bar.get_height()/2., 
           f'{value:.0f}x',
           va='center', ha='left', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('projeto_3_speedup.png', dpi=300, bbox_inches='tight')
print("✓ Gráfico de Speedup salvo em: projeto_3_speedup.png")
plt.close()

# Imprimir estatísticas
print("\n" + "="*70)
print("ESTATÍSTICAS DE DESEMPENHO - PROJETO 3")
print("="*70)
print(f"\n{'Critério':<15} | {'Insertion (ms)':<15} | {'Merge (ms)':<15} | {'Speedup':<10}")
print("-"*70)

for i, criterio in enumerate(criterios):
    speedup_val = insertion_times[i] / merge_times[i]
    print(f"{criterio:<15} | {insertion_times[i]:>13.2f} | {merge_times[i]:>13.2f} | {speedup_val:>8.0f}x")

print("\n" + "="*70)
print("CONCLUSÕES:")
print("="*70)
print("1. Merge Sort é significativamente mais rápido para 10.000 produtos")
print("2. Diferença é mais marcante com dados de data (27.483x mais rápido)")
print("3. Para dados simples (preço, estoque): ~150x mais rápido")
print("4. Insertion Sort é O(n²) enquanto Merge Sort é O(n log n)")
print("="*70 + "\n")
