"""
Gerador de dados para Projeto 3
Cria arquivo de entrada com 10000 produtos no formato correto
"""

import random
from datetime import datetime, timedelta

def gerar_dados_projeto_3():
    """Gera arquivo de entrada com 10000 produtos"""
    
    nomes_base = [
        "Processador", "Memória RAM", "SSD", "HD", "Placa de Vídeo",
        "Placa-mãe", "Fonte", "Cooler", "Gabinete", "Monitor",
        "Teclado", "Mouse", "Webcam", "Headset", "Microfone",
        "Caixa de Som", "Adaptador Bluetooth", "Roteador", "Switch", "Hub USB",
        "Impressora", "Scanner", "Projetor", "Tablet", "Smartphone",
        "Notebook", "Carregador", "Bateria", "Controle", "Cabo USB"
    ]
    
    modelos = [f"Modelo {i}" for i in range(1000, 10000)]
    
    # Data inicial
    data_inicio = datetime(2022, 1, 1)
    
    produtos = []
    
    print("Gerando 10000 produtos...")
    
    for i in range(10000):
        produto_id = f"ID{i:06d}"
        nome = f"{random.choice(nomes_base)} {random.choice(modelos)}"
        preco = round(random.uniform(20.50, 9999.99), 2)
        estoque = random.randint(0, 500)
        popularidade = random.randint(0, 50000)
        
        # Data aleatória entre 2022-01-01 e 2025-12-31
        dias_aleatorios = random.randint(0, 1460)
        data_cadastro = data_inicio + timedelta(days=dias_aleatorios)
        data_str = data_cadastro.strftime("%Y-%m-%d")
        
        # Formatar com padding (zeros à esquerda)
        preco_fmt = f"{preco:010.2f}"      # 0000020.57
        estoque_fmt = f"{estoque:05d}"     # 00000
        popularidade_fmt = f"{popularidade:05d}"  # 00000
        
        # Construir linha
        linha = f"{produto_id} | {nome:<40} | {preco_fmt} | {estoque_fmt} | {popularidade_fmt} | {data_str}\n"
        produtos.append(linha)
    
    # Salvar arquivo
    with open('projeto_3_lista_produtos_entrada.txt', 'w', encoding='utf-8') as f:
        f.writelines(produtos)
    
    print(f"✓ {len(produtos)} produtos salvos em projeto_3_lista_produtos_entrada.txt")

if __name__ == "__main__":
    gerar_dados_projeto_3()
